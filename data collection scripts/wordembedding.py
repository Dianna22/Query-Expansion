from numpy import asarray
from numpy import zeros, array
import time, pickle, json

VOCAB_SIZE = 216098
words_per_phrase = 2

t1= time.time()

# load the whole embedding into memory
embeddings_index = dict()
f = open('glove.6b/glove.6B.50d.txt', 'rb')
for line in f:
    values = line.split()
    word = values[0].decode('utf-8')
    coefs = asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()
t2 = time.time()
print('Loaded %s word vectors.' % len(embeddings_index))
print("Exe time ", t2-t1, "s")
print("Exe time ", (t2-t1)/60, "min")
print("Exe time ", (t2-t1)//60, "min ", (t2-t1)-((t2-t1)//60)*60, "s")

def embed_phrases(phrase_file, embedding_file):
    print("embedding")
    print(embeddings_index.keys())
    phrase_embeddings = zeros((VOCAB_SIZE, words_per_phrase * 50))
    with open(phrase_file, "rb") as f:
        with open(embedding_file, "w", encoding="utf8") as out:
            line = f.readline()
            while line:
                id, phrase = line.decode().split(",")
                # concatenate word embeddings
                id = int(id)
                embedding_vector = zeros((words_per_phrase, 50))
                for index, word in enumerate(phrase.split()):
                    word = word.strip()
                    embedding_word_vector = embeddings_index.get(word)
                    if embedding_word_vector is not None:
                        embedding_vector[index] = embedding_word_vector
                embedding_vector = array(embedding_vector).flatten()
                phrase_embeddings[id] = embedding_vector
                # entry = {id: embedding_vector}
                # json.dump(entry, fp=out)
                # print(str(id)+ "; ", embedding_vector, file=out)
                if id % 10000 == 0:
                    print(id)
                line = f.readline()
            print("dumping")
            result = {"data" : phrase_embeddings.tolist()}
            json.dump(result, out)
            # pickle.dump(phrase_embeddings, out)
            print("dumped")
    print("returning")
    return phrase_embeddings

t1 = time.time()
embed_phrases("embeddings/phrases-2words", "embeddings/2word-embeddings-50")
t2 = time.time()
print("Embedding took")
print("Exe time ", t2-t1, "s")
print("Exe time ", (t2-t1)/60, "min")
print("Exe time ", (t2-t1)/60, "min ", (t2-t1)-((t2-t1)//60)*60, "s")
