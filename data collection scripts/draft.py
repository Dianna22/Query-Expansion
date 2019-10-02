a = [(1,2),(3,4)]
print(zip(a))
print(list(zip(*a)))
import numpy as np
print(np.min(a))

# from nltk.corpus import wordnet as wn
# import networkx as nx
# from matplotlib import pyplot as plt
# def closure_graph(synset, fn):
#     seen = set()
#     graph = nx.DiGraph()
#
#     def recurse(s):
#         if not s in seen:
#             seen.add(s)
#             graph.add_node(s.name())
#             for s1 in fn(s):
#                 graph.add_node(s1.name())
#                 graph.add_edge(s.name(), s1.name())
#                 recurse(s1)
#
#     recurse(synset)
#     return graph
#
# graph = closure_graph(wn.synsets("color")[0],lambda s: s.hypernyms())
# nx.draw_networkx(graph)
#
#
# plt.show()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# from nltk.corpus import wordnet as wn
#
# # synsets = wn.synsets("young")
# # young = synsets[0]
# # hypers = young.hypernyms()
# # siblings = [hyper.hyponyms() for hyper in hypers]
# # print(siblings)
#
#
#
# import numpy as np
#
# # print(synsets)
# # print(len(synsets))
# # for synset in synsets:
# #     print(synset)
# #     print(synset.definition())
# import nltk
# # spyware = wn.synsets("computer")[0]
# # software = wn.synsets("keyboard")[0]
# # print(spyware)
# # print(wn.synset('spyware.n.01'))
# # print(wn.synset('spyware.n.01').path_similarity(wn.synset('software.n.01')))
#
# # print(software.wup_similarity(spyware))
# # import nltk
# # nltk.download('wordnet_ic')
# from nltk.corpus import wordnet_ic
#
# # brown_ic = wordnet_ic.ic('ic-brown.dat')
# # semcor_ic = wordnet_ic.ic('ic-semcor.dat')
# # print(software.jcn_similarity(spyware, brown_ic))
# # print(software.jcn_similarity(spyware, semcor_ic))
#
# # print(cat,dog)
# # print(cat.path_similarity(dog))
#
# # import logging
# #
# # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# #
# # from gensim.models import word2vec
# # sentences = word2vec.Text8Corpus('text8')
# # model = word2vec.Word2Vec(sentences, size=200)
# #
# # print(model.most_similar(positive=['aunt', 'grandmother'], negative=['uncle'], topn=1))
# # print(model.most_similar(positive=['aunt', 'father'], negative=['uncle'], topn=1))
# # print(model.most_similar(positive=['aunt', 'brother'], negative=['uncle'], topn=1))
# # print(model.most_similar(positive=['mother', 'grandfather'], negative=['grandmother'], topn=1))
# #
# # print(model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1))
#
# # import os
# # path = "S:\II\SGBD\Labs"
# # def findPhraseRec(path, phrase, result=[]):
# #     for file in os.listdir(path):
# #         complete_path = os.path.join(path, file)
# #         if os.path.isfile(file):
# #             with open(complete_path, "r") as f:
# #                 if phrase.lower() in f.read().lower():
# #                     result.append(complete_path)
# #         else:
# #             findPhraseRec(complete_path, phrase, result)
# #     return result
# #
# # print(findPhraseRec(path, "user_table"))
#
#             # import numpy as np
#             # a = np.zeros((2,3))
#             # a[0] = [1,2,4]
#             # a[1] = [1,2,4]
#             # print(a)
#             #
#             # print(a.flatten())
#             # print(np.shape(a.flatten()))
#             # a = a.flatten()
#             # print(a)
#             # from lexicon import WNLexicon
#             # wnn = WNLexicon()
#             # res = wnn.get_synsets("carotid")
#             # par = wnn.get_parents(res[0])
#             # ch = wnn.get_children(res[0])
#             #
#             # from nltk.corpus import wordnet as wn
#             # b=wn.synsets("beautiful")
#             # b=wn.synsets("co2")
#             # b=wn.synsets("artery")
#             #
#             # # for lemma in wn.synsets("expense")[0].lemmas():
#             # #     print(lemma.name())
#             # #     print("closures")
#             # #     bb = wn.synsets(lemma.name()[0])
#             # #     print(bb)
#             # #     bb= bb[0]
#             # #     print(list(bb.closure(wnn.get_children(bb))))
#             # #     print(list(bb.closure(wnn.get_parents(bb))))
#             # #     print("children")
#             # #     print(wnn.get_children(bb))
#             # #     print("parents")
#             # #     print(wnn.get_parents(bb))
#             # #     print("sublings")
#             # #     print(wnn.get_siblings_synsets(bb))
#             # b=wn.synsets("expense")
#             # for bb in b:
#             #     print(bb)
#             #     print("closures")
#             #     print(list(bb.closure(wnn.get_children(bb))))
#             #     print(list(bb.closure(wnn.get_parents(bb))))
#             #     print("children")
#             #     print(wnn.get_children(bb))
#             #     print("parents")
#             #     print(wnn.get_parents(bb))
#             #     print("sublings")
#             #     print(wnn.get_siblings_synsets(bb))
#             #
#             #
#             #
#             # # base_path = "F:\wiki\wiki articles"
#             # # import elasticsearchHelper as es
#             # # index = es.IndexHelper("wiki-revision")
#             # # res = index.multiFieldSearchPhrase(["title", "revision"],phrase="blond girl")
#             # # print(res)
#             # # print(res["hits"]["total"])
#             # # print(res["hits"]["max_score"])
#             # # index = IndexHelper("w")
#             # # # paths = ["P:\III\Graduation thesis\\thesis\similar_phrases\index\doc1.json"]
#             # #          # "P:\III\Graduation thesis\\thesis\similar_phrases\index\doc2.json",
#             # #          # "P:\III\Graduation thesis\\thesis\similar_phrases\index\doc3.json"]
#             # # paths = []
#             # # base = "F:\wiki\descriptions_all-"
#             # # for i in range(1):
#             # #     paths.append(base + str(i) + ".json")
#             # # # index.put_mapping({"_doc":})
#             # # # print(index.getId())
#             # # # paths = ["P:\III\Graduation thesis\\thesis\similar_phrases\index\doc3.json"]
#             # # paths = ["index\wiki.json"]
#             # # print(paths)
#             #
#             # # if not index.exists():
#             # #     index.create()
#             # # index.addJSONDocuments(paths)
#             #
#             # # print(index.searchPhrase("title", "Third book"))
#             #
#             #
#             #
#             # # # import wikipedia
#             # # #
#             # # # print(wikipedia.summary("blonde girl"))
#             # # # # print(wikipedia.summary("blond blond amazon go"))
#             # # # print(wikipedia.summary("horse wait"))
#             # #
#             # # import urllib3
#             # # http = urllib3.PoolManager()
#             # # url = "https://corpus.byu.edu/wiki/"
#             # #
#             # # """Example of Python client calling Knowledge Graph Search API."""
#             # # import json
#             # # import urllib
#             # # import urllib.parse, urllib.request
#             # # api_key = "AIzaSyAT6Ge_TC9F4FMU1sdbm61XVJk5dyj6_X4"
#             # # api_key = "AIzaSyCjHNR79-H8E_WGphvnjzH7nMY_9fT1eUA"
#             # #
#             # #
#             # # api_key = "AIzaSyCpQnJQPZlrh1GDNxcbwpX-HuV3QwpFEY4"
#             # #
#             # # query = 'Taylor Swift'
#             # # query = 'Taylor Swift'
#             # # query = 'blond girl'
#             # # query = 'bird go'
#             # # service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
#             # # api_key = open('.api_key').read()
#             # # service_url = 'https://www.googleapis.com/customsearch/v1'
#             # # params = {
#             # #     # 'query': query,
#             # #     # 'limit': 10,
#             # #     # 'indent': True,
#             # #     'key': api_key,
#             # #     'cx': "017576662512468239146:omuauf_lfve",
#             # #     'q':"TA Engineering (General). Civil engineering (General)",
#             # # }
#             # # url = service_url + '?' + urllib.parse.urlencode(params)
#             # # print(url)
#             # # response = json.loads(urllib.request.urlopen(url).read())
#             # # # for element in response['itemListElement']:
#             # # #     print(element['result']['name'] + ' (' + str(element['resultScore']) + ')')
#             # # print(response["queries"]["request"][0]["totalResults"])
#             # # print(response["queries"]["request"][0])
#             # # print(response["queries"]["request"])
#             # #
#             # # with open("res", "w") as f:
#             # #     print(response, file=f)
#             # #
#             # #
#             # # # import language_check
#             # # #
#             # # # text = "blond blond admire amazon"
#             # # # text = "blond blond admire donna"
#             # # # tool = language_check.LanguageTool('en-GB')
#             # # # matches = tool.check(text)
#             # # # print(len(matches))
#             # # # print(matches)
#             # # # print(tool.correct(text))
#             # # #
#             # #
#             # #
#             # #
#             # #
#             # #
#             # #
#             # #
#             # #
#             # # # from functools import lru_cache
#             # # #
#             # # # @lru_cache(maxsize=256)
#             # #
#             # # # f = open("red_blue_eyed_girl", "w")
#             # # # similar_phrases_wn("red blue eyed girl", f)
#             # #
#             # # # f1= open("blue_door_dog", "w")
#             # # # similar_phrases_wn("blue door dog",f1)
#             # # # f2 = open("blue_door_cat", "w")
#             # # # similar_phrases_wn("blue door cat dog",f2)
#             # #
#             # # # from owlready2 import *
#             # # #
#             # # #  onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
#             # # # onto.load()
#             # # # print(list(onto.classes()))
#             # # # print(onto.search("something"))
#             # # from exceptions import InvalidWordException
#             # # from nltk.corpus.reader.wordnet import Synset
#             # #
#             # # # lexicon = WNLexicon()
#             # # # pos=lexicon.get_pos("beautiful")[0][1]
#             # # # a=lexicon.get_synsets("beautiful")
#             # # # b=lexicon.get_synsets("green")
#             # # # c=lexicon.get_synsets("here")
#             # # # d=lexicon.get_synsets("go")
#             # # # for synset in lexicon.get_synsets("car"):
#             # # #     print(synset)
#             # # #     print(lexicon.get_cousins(synset))
#             # #
#             # # # print(a,b,c,d)
#             # # # lexicon.get_synset("beautiful", lexicon.get_pos("beautiful"))
#             # # # Compute transitive closures of synsets
#             # # # noun, verb, adj = input("noun>"), input("verb>"), input("adj>")
#             # # noun, verb, adj = "walls", "are", "blue"
#             # # # n_lemma, n_pos, n_sis = wn.synset(noun, wn.NOUN)
#             # # # v_lemma, v_pos, v_sis= wn.synset(verb, wn.VERB)
#             # # # a_syn, a_pos, a_sis = wn.synset(adj, wn.ADJ)
#             # #
#             # # # print(n_sis)
#             # #
#             # # # n_sis = wn.synsets(noun)
#             # # # hypo = lambda s: s.hyponyms()
#             # # # hyper = lambda s: s.hypernyms()
#             # #
#             # # # print(list(wn.synset("wall.n.01").closure(hypo, depth=1)))
#             # # # print(list(wn.synset("wall.n.01").closure(hypo, depth=2)))
#             # # # print(list(wn.synset("wall.n.01").closure(hyper, depth=1)))
#             # # # print(list(wn.synset("wall.n.01").closure(hyper, depth=2)))
#             # # # print(list(wn.synset("wall.n.01").closure(hyper, depth=2))[0].name())
#             # # # print(list(wn.synsets("blue")[0].closure(hypo, depth=2))[0].name())
#             # # # print(list(wn.synsets("blue")))
#             # # # print(type(list(wn.synset("wall.n.01").closure(hyper, depth=2))[0]))
#             # # # print((list(wn.synset("wall.n.01").closure(hyper, depth=2))[0].name()))
#             # # # vehicle = wn.synset('vehicle.n.01')
#             # # # typesOfVehicles = list(set([w for s in vehicle.closure(lambda s:s.hyponyms()) for w in s.lemma_names]))
#             # #
#             # #
#             # # # def get_siblings(self, synset: Synset):
#             # # #     """
#             # # #     Returns up to five siblings of the synset.
#             # # #     :param synset: The synset to obtain the siblings from
#             # # #     :return: The siblings obtained from the synset
#             # # #     """
#             # # #
#             # # #     siblings = []
#             # # #     sibling_count = 0
#             # # #     parent = self.get_parent(synset)
#             # # #
#             # # #     for sibling in parent.hyponyms():
#             # # #         if sibling_count == 5:
#             # # #             break
#             # # #         if sibling != synset and self.valid_synset(sibling):
#             # # #             siblings.insert(sibling_count, sibling)
#             # # #             sibling_count += 1
#             # # #
#             # # #     return siblings
#             # #
#             # # # print(get_siblings())