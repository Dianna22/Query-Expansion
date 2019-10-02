import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
class WNLexicon:
    """
    Utility class working with WordNet NLTK corpus reader
    """
    def __init__(self):
        """
        Download wordnet if not loaded
        """
        try:
            self.get_pos("beautiful as")
            wn.synset("wall.n.01")
        except LookupError:
            nltk.download('averaged_perceptron_tagger')
        except:
            """
            Download the corpus reader
            """
            nltk.download('wordnet')

    def get_pos(self, word, tagset=None):
        """
        Use tagset='universal' to have the pos formatted as follows:
        [('John', 'NOUN'), ("'s", 'PRT'), ('big', 'ADJ'), ('idea', 'NOUN'), ('is', 'VERB'),
        ("n't", 'ADV'), ('all', 'DET'), ('that', 'DET'), ('bad', 'ADJ'), ('.', '.')]
        :param word: string for which the part of speech is requested
        :return: part of speech as a list of tuples :
                    (<word>, <pos_abbreviation>)
                    [('beautiful', 'NN')]
                    [('map', 'NN')]
                    [('go', 'VB')]
                    [('the', 'DT')]
                    [('here', 'RB')]
        """
        try:
            return nltk.pos_tag(word_tokenize(word), tagset=tagset)
        except LookupError:
            nltk.download('universal_tagset')
            return nltk.pos_tag(word_tokenize(word), tagset=tagset)

    def get_synsets(self, word):
        """
        :param word: string
        :return: a list of Synsets instances of the requested word
        """
        return wn.synsets(word)

    def get_parents(self, synset):
        """
        :param synset: Synset instance
        :return: list of hypernyms of the synset
        """
        return synset.hypernyms()

    def get_children(self, synset):
        """
        :param synset: Synset instance
        :return: list of hyponyms of the synset
        """
        return synset.hyponyms()

    def get_siblings_synsets(self, synset):
        """
        :param synset: Synset instance
        :return: list of hyponyms of all the hypernyms of the synset
        """
        siblings = []
        synset_parents = self.get_parents(synset)
        for parent in synset_parents:
            children = self.get_children(parent)
            siblings += children
        return siblings

    def get_siblings(self, word):
        """
        :param word: word
        :return: list of words (hyponyms of all the hypernyms of the concept/word)
        """
        w_synsets = self.get_synsets(word)
        c_synsets = []
        for w_synset in w_synsets:
            c_synsets += self.get_siblings_synsets(w_synset)
        siblings = []
        for synset in c_synsets:
            siblings.append(synset.name().split(".")[0])
        return siblings

    def get_similar(self, word):
        """

        :param word:
        :return: siblings and children
        """
        w_synsets = self.get_synsets(word)
        c_synsets = []
        for w_synset in w_synsets:
            c_synsets += self.get_siblings_synsets(w_synset) #+ self.get_children(w_synset)
        similar = []
        for synset in c_synsets:
            similar.append(synset.name().split(".")[0])
        return similar