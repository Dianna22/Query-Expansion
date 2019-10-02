import urllib.request

class Solr():
    # def __init__(self, collection_name="techproducts"):
    def __init__(self, collection_name="wiki_dumps"):
        self.collection_name = collection_name
        self.endpoint = "http://localhost:8983/solr/"
    def phrase_search(self, phrase):
        search_url = self.endpoint + self.collection_name+ "/select?q=\""
        search_url += "+".join(phrase.split()) + "\""
        print(search_url)
        print(urllib.request.urlopen(search_url).read())
search = Solr()

# search.phrase_search("good girl")
# search.phrase_search("CAS latency")
# search.phrase_search("foundation")

import wikipedia
print(wikipedia.search("sweet remote-control"))