from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import DocType, Index, Text, Date
from elasticsearch import helpers

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# es.indice.create('index')
# es.search(index="wiki-try").
# es.indices.create(index='test-index')

# import os
# class Document(DocType):
#     def setTitle(self, title):
#         title = Text(title)
#         return self
#     created_at = Date()
#     content = Text(multi=True)
#     index = 'wiki-default'
#
#     def appendContent(self, text):
#         self.content.append(text)
#         super().save()
#     # def get_chunks_of_lines(self, lines):
#
#     # def get_all_content(self):
#     #     # with open(self.path, "r") as f:
#     #     #     return f.read()
#     #     with open(self.path, "r") as f:
#     #         for line in f.readlines():
#     #             yield  line
#     #
#     # def get_chunks(self, path, lines):
#     #     with open(self.path, "r") as f:
#     #         lines = []
#     #         counter = 0
#     #         for line in f.readlines():
#     #             counter += 1
#     #             lines.append(line)
#     #             if counter == lines:
#     #                 yield lines
#     #                 lines = []
#     #                 counter = 0
# path = "P:\III\Graduation thesis\thesis\similar_phrases\index\enwiki-20180301-pages-articles-multistream.xml"
# title = os.path.basename(path)

# doc = Document().setTitle(title)



def index_doc(doc, index_name="wiki-dumps"):
    global es
    index = Index(index_name)
    index.create()

    # document = DocType()
    # document.init(index)
    # if document.save():
    #     document.


a=[{"_index":"wiki-try","_type":"_doc","_source":{"id": str(i), "author": "auth"+str(i), "title":"title"+str(i**2),
    "summary":str(i*10)}} for i in range(5)]
# helpers.bulk(es, a, index="wiki-try")
#es.create(index=, doc_type==, body={...})
res = es.search(index="wiki-try", body={"query":{
    "match_phrase":{"summary":"awesome elasticsearch api"}
}})
print(res["hits"])

# import requests

# res = requests.get('http://localhost:9200')
# print(res.content)



from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

# client = Elasticsearch()
#
# s = Search(using=client)
#
# s = s.using(client)
#
# s = Search().using(client).query("match", title="python")
#
# response = s.execute()
#
# for hit in s:
#     print(hit.title)

# s = Search()
# s = s.filter('terms', tags=['search', 'python'])
# resp = s.execute()
# print(resp)

# from datetime import datetime
# from elasticsearch import Elasticsearch
# es = Elasticsearch()
#
# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
# print(res['created'])
#
# res = es.get(index="test-index", doc_type='tweet', id=1)
# print(res['_source'])
#
# es.indices.refresh(index="test-index")
#
# res = es.search(index="test-index", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
