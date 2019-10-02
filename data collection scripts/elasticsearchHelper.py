from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from elasticsearch import helpers
import json

class IndexHelper:
    def __init__(self, name="default",
                 es=Elasticsearch([{'host': 'localhost',
                                    'port': 9200}])):
        self.name = name
        self.es = es
        self.indicesClient = IndicesClient(client = es)
        self.type = "doc"
        self._buffer = []
        # prepare object for bulk indexing
        self._bulkFrame = {"_index":self.name,"_source": "",
               "_type" : self.type}
        # field to be updated for indexing
        self._bulkField ="_source"
        # number of items to be indexed at once
        self._bulkFlushNumber = 20000

    def exists(self):
        return self.indicesClient.exists(index=self.name)

    def setType(self, type):
        self.type = type
        return self

    def getId(self):
        self.indicesClient.get(self.name)

    def create(self):
        """
        Create an index given a specific mapping
        :param mapping:
        {"field":{"type": "text/keyword/date/long/double/boolean/ip
        /object/nested (-> JSON)
        /geo_point/geo_shape/completion"}
        }
        """
        self.indicesClient.create(index=self.name)
        return self

    def put_mapping(self, mapping):
        self.indicesClient.put_mapping(mapping)

    def delete(self):
        self.indicesClient.delete(index=self.name)

    def _getContents(self, paths, frame, field):
        contents = []
        copy = frame.copy()
        for path in paths:
            with open(path,"r") as f:
                for obj in f.readlines():
                    frame = copy.copy()
                    frame[field] = json.loads(obj)
                    contents.append(frame)
        return contents

    def addJSONDocuments(self, paths):
        content = self._getContents(paths, self._bulkFrame, self._bulkField)
        resp = helpers.bulk(self.es, content,
                     index=self.name)
        print(resp)

    def _flush(self):
        helpers.bulk(self.es, self._buffer, index=self.name)

    def addJSONBuffering(self, json, flush_number = None):
        if flush_number is None:
            flush_number = self._bulkFlushNumber
        obj = self._bulkFrame.copy()
        obj[self._bulkField] = json
        self._buffer.append(obj)
        if len(self._buffer)>=flush_number:
            print("Indexing {} articles...".format(len(self._buffer)))
            self._flush()
            self._buffer = []

    def searchKeyword(self, field, keyword):
        query = {"query":{
            "match": {field: keyword}
        }}
        return self.es.search(index=self.name, body=query)

    def searchPhrase(self, field, phrase):
        query = {"query":{
            "match_phrase": {field: phrase}
        }}
        return self.es.search(index=self.name, body=query)

    def looseSearch(self, field, phrase, slop=1):
        """

        :param field:
        :param phrase:
        :param slop: factor telling how far the words can be from each other
                in terms of permutation moves that need to be performed
        :return:
        """
        query = {
            "query": {
                "match_phrase": {
                    field: {
                        "query": phrase,
                        "slop": slop
                    }
                }
            }
        }
        return self.es.search(index=self.name, body=query)

    def multiFieldSearchPhrase(self, fields, phrase):
        query = {
            "query": {
                "multi_match" : {
                  "query": phrase,
                  "type": "phrase",
                  "fields": fields
                }
            }
        }
        return self.es.search(index=self.name, body=query)

    def getArticlesPaginated(self, slice_number, max_slices):
        query ={
            "slice": {
                "id": slice_number,
                "max": max_slices
            }
        }
        scroll_id = self.es.search(index=self.name,body=query, scroll="1m")["_scroll_id"]
        return self.es.scroll(scroll_id, scroll="10m")["hits"]["hits"]