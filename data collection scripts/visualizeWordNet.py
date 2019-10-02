from nltk.corpus import wordnet as wn
import networkx as nx
from matplotlib import pyplot as plt
def closure_graph(word):
    seen = set()
    graph = nx.DiGraph()

    def addHyponyms(synset):
        print(synset, synset.hyponyms())
        for s in synset.hyponyms():
            if s not in seen:
                seen.add(s)
                graph.add_node(s.name())
                graph.add_edge(synset.name(), s.name())
    # for synset in wn.synsets(word):
    synset = wn.synsets(word)[0]
    print(synset.definition())
    print(synset.name())
    print(synset.hypernyms())
    print(wn.synsets(word))
    for s in synset.hypernyms():
        if s not in seen:
            seen.add(s)
            graph.add_node(s.name())
            graph.add_edge(synset.name(),s.name())
            addHyponyms(s)

    # for s in synset.hyponyms():
    #     if s not in seen:
    #         graph.add_node(s.name())
    #         graph.add_edge(synset.name(), s.name())
    #         seen.add(s)



    def recurse(s, fn):
        if not s in seen:
            seen.add(s)
            graph.add_node(s.name())
            for s1 in fn(s):
                graph.add_node(s1.name())
                graph.add_edge(s.name(), s1.name())
                recurse(s1, fn)
    def recurse2(s, fn):
        if not s in seen:
            seen.add(s)
            graph.add_node(s.name())
            for s1 in fn(s):
                graph.add_node(s1.name())
                graph.add_edge(s1.name(), s.name())
                recurse2(s1, fn)

    # recurse(synset, lambda s: s.hypernyms())
    # recurse2(synset, lambda s: s.hyponyms())
    return graph

graph = closure_graph("politician")
nx.draw_networkx(graph)


plt.show()