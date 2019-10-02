import numpy as np
from numpy import asarray

embeddings = dict()
def load_embeddings(embeddings_file):
    global embeddings
    with open(embeddings_file, 'rb') as f:
        for line in f:
            values = line.split()
            word = values[0].decode('utf-8')
            coefs = asarray(values[1:], dtype='float32')
            embeddings[word] = coefs
    return embeddings

load_embeddings('../glove.6B/glove.6B.' + str(50) + 'd.txt')

def embedPhrase(phrase):

    words = phrase.split(" ")

    embedding = []
    for word in words:
        if word in embeddings.keys():
            emb1 = embeddings[word]
            embedding = np.concatenate(( embeddings[word], embedding))
        else:
            return None
    # if phrase == "number number":
    #     print(phrase)
    #     print(embedding)
    return embedding

# with open("../ml-results/phraseVocab.txt", "w") as vocab:
#     vocabulary = set()
#     with open("validationSet", "r") as f:
#         line = f.readline()
#         while line:
#             phrases = line.split(",")
#             phrase1 = phrases[0].strip()
#             phrase2 = phrases[1].strip()
#             if phrase1 not in vocabulary:
#                 vocabulary.add(phrase1)
#                 emb = embedPhrase(phrase1)
#                 if emb is not None:
#                     emb = [str(e) for e in emb]
#                     vocab.write(phrase1 + " " + " ".join(emb)+"\n")
#             if phrase2 not in vocabulary:
#                 vocabulary.add(phrase2)
#                 emb2 = embedPhrase(phrase2)
#                 if emb2 is not None:
#                     emb2 = [str(e) for e in emb2]
#                     vocab.write(phrase2 + " " + " ".join(emb2)+"\n")
#             line = f.readline()

phrases = ["woman captain", "female superior", "male superior", "male captain", "woman superior"]
with open("../ml-results/phraseVocab.txt", "a") as vocab:
    for phrase in phrases:
        emb = embedPhrase(phrase)
        if emb is not None:
            print(phrase)
            emb = [str(e) for e in emb]
            vocab.write(phrase+" "+ " ".join(emb)+"\n")
