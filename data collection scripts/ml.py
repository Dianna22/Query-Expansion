from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Embedding, Flatten
from keras.models import load_model
import time, json
import numpy as np
from numpy import asarray
import pickle, time

emb_dim = 50

# "aorta co2"
# "pulmonary co2"
# "leg blood"
# "arm blood"
# "aorta arm"
# DICT_SIZE = 5
# X = [[1,1,0,0,0], [0,0,1,1,0]]
# Y = [1,1]
# Xtest = [[1,0,0,0,1], [0,0,1,0,1], [0,0,1,1,0], [1,1,0,0,0]]
# Ytest = [0,0,1,1]
#
#
# X = [[1,0,0,0,0], [0,0,1,0,0]]
# Y = [[0,1,0,0,0], [0,0,0,1,0]]
# Xtest = [[1,0,0,0,0], [0,0,1,0,0], [0,0,0,0,1]]
# Ytest = [[0,1,0,0,0], [0,0,0,1,0], [0,0,0,0,0]]
dataset = dict()
def load_data_set(file):
    X, Y = [], []
    index = 0
    with open(file, "r") as f:
        line = f.readline()
        while line:
            (id1, id2) = line.split(",")
            id2 = id2.strip()
            X.append(id1)
            Y.append(id2)
            if id1 in dataset.keys():
                dataset[id1].append(id2)
            else:
                dataset[id1] = [id2]
            line = f.readline()
    return (X, Y)
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

load_embeddings('glove.6B/glove.6B.' + str(emb_dim) + 'd.txt')

def embed(phrases):
    global embeddings
    results = [(phrase,embedPhrase(phrase)) for phrase in phrases if embedPhrase(phrase) is not None]
    return list(zip(*results))[0], list(zip(*results))[1]

def embedPhrase(phrase):
    words = phrase.split(" ")
    embedding = []
    for word in words:
        if word in embeddings.keys():
            embedding = np.concatenate((embeddings[word], embedding))
        else:
            return None
    return embedding

def embedDataSet(x, y):
    xresult = []
    yresult = []
    phrases = []
    print(len(x))
    print(len(y))
    for i in range(len(x)):
        if i %10000 ==0:
            print(i)
        if len(y[i].split(" ")) != 2:
            continue
        xembed = embedPhrase(x[i])
        yembed = embedPhrase(y[i])
        # if np.shape(yembed)[1] != 100:
        #     print(yembed, y[i])
        if xembed is not None and yembed is not None:
            xresult.append(list(xembed))
            yresult.append(list(yembed))
            phrases.append(x[i])
        #    print(np.shape(xresult))
        # print(np.shape(yresult))
    # print(np.shape(np.array(xresult)))
    # np.reshape1(yresult, np.shape(xresult))
    return phrases, xresult, yresult

def containsNonZero(arr):
    for el in arr:
        if el != 0:
            return True
    return False

def findEmbedding(db, embedding):
    threshold = 999999
    id = None
    for index, value in enumerate(db):
        euclidean_distance = np.linalg.norm(np.subtract(embedding, value))
        if euclidean_distance < threshold and containsNonZero(value):
            id = index
            threshold = euclidean_distance
            print(embedding)
            print(value)
            print(id)
            print("a")
    print("threshold {} for id {}".format(threshold, id))
    return id

def distance(emb1, emb2):
    return np.linalg.norm(emb1-emb2)

def testmodel(model):
    Xtest, Ytest = load_data_set("siblings/validationSet")

    print("Loaded dataset")
    with open("ml-results/model-300-tanh-mse-sgd/correct-network", "w") as f:
        xphrases, x, y = embedDataSet(Xtest,Ytest)
        predictions = model.predict(x)
        total, correct = len(predictions), 0
        # for i in range(1, len(predictions)):
        #     print(predictions[i])
        distance_results = []
        found_distances = []
        found_pairs = []
        for index, prediction in enumerate(predictions):
            if index %1000==0:
                print(index)
            phrase1 = xphrases[index]
            embed2 = prediction
            phrases, correct_embeddings = embed(dataset[phrase1])
            distances = [distance(embed1, embed2) for embed1 in correct_embeddings]

            distance_results.append(distances)
            min_dist = 9999
            found = False
            min_phrase = ""
            for index, cemb in enumerate(correct_embeddings):
                dist = distance(embed2, cemb)
                if dist < 4.7 and dist < min_dist:
                    min_dist = dist
                    min_phrase = phrase1 + "," + phrases[index]+"\n"
                    f.write(min_phrase)
                    found = True
            if found == True:
                correct += 1
                found_distances.append(min_dist)
                found_pairs.append(min_phrase)

                    # norm = np.linalg.norm(np.subtract(prediction, y[index]))
                # print("norm {}".format(norm))
                # id = findEmbedding(embeddings, x[index])
                # closest_id = findEmbedding(embeddings, prediction)
                # true_id = findEmbedding(embeddings, y[index])
                # print("id {} prediction {} true sibling {}".format(id, closest_id, true_id))
                # # check pair
                # f.write(str(id)+ "," + str(closest_id)+"\n")
        with open("ml-results/model-300-tanh-mse-sgd/distances.h", 'wb') as f:
            pickle.dump(distance_results, f)
        # print(distance_results)
        print(np.mean(found_distances))
        print(np.max(found_distances))
        print(np.min(found_distances))
        print(correct)
        return correct * 100 / total

def createModel():
    Xid, Yid = load_data_set("siblings/trainingSet")
    X, Y = Xid.copy(), Yid.copy()
    Xtest, Ytest = load_data_set("siblings/validationSet")

    print("Loaded dataset")
    print(len(X), len(Y))
    print(len(Xtest), len(Ytest))
    # embeddings = load_embedding("embeddings/2word-embeddings-json-data")

    trainPhrases, X,Y = embedDataSet(X,Y)
    print("embeded training dataset:")
    print(len(X), len(Y))

    print("X", np.shape(X))
    print("Y", np.shape(Y))
    testPhrases, Xtest, Ytest = embedDataSet(Xtest,Ytest)
    print("embeded test dataset:")
    print(len(Xtest), len(Ytest))

    print("Emb", np.shape(embeddings))
    model = Sequential()
    # e = Embedding(len(X), 200, weights=[embeddings], input_length=1, trainable=False)
    model.add(Dense(500, input_shape=(100,), activation='tanh'))
    model.add(Dense(100, activation='tanh'))
    # model.add(e)
    # model.add(Flatten())
    # model.add(Dense(200))

    # Compile model
    model.compile(loss='mean_squared_error', optimizer='sgd')
    print("Model compiled")
    # model.fit(X, Y, epochs=3, batch_size=10)
    t1 = time.time()

    # model = load_model("embeddings/model400.h5")
    model.fit(list(X), list(Y), epochs=1000, batch_size=50)
    print("Model fit")
    t2 = time.time()
    print("training time ", t2 - t1, "s")


    model.save("ml-results/model-300-tanh-mse-sgd/modelbatch50-500n.h")

    # evaluate the model
    # scores = model.evaluate(Xtest, Ytest)
    # print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
    # predictions = model.predict(Xtest)
    # print(predictions)
    # return model.metrics_names[1], scores[1] * 100

    # accuracy = testmodel(model, testPhrases, Xtest, Ytest)
    # print(accuracy)

t1 = time.time()
model = load_model("ml-results/model-300-tanh-mse-sgd/modelbatch50-500n.h")
accuracy = testmodel(model)
print(accuracy)
# createModel()
t2 = time.time()
print("Exe time ", t2-t1, "s")
print("Exe time ", (t2-t1)//60, "min")
print("Exe time ", (t2 - t1) // 60, "min ", (t2 - t1) - ((t2 - t1) // 60) * 60, "s")
# print("Training hidden units 200, in/out 100, relu, sigmoid, binary_crossentropy, adam, accuracy")



# with open("ml-results.txt", "w") as f:
#     print("Exe time ", (t2-t1)//60, "min ", (t2-t1)-((t2-t1)//60)*60, "s", file=f)
#     print("Training hidden units 200, in/out 100, relu, sigmoid, binary_crossentropy, adam, accuracy", file=f)
    # print(pred, file=f)
# import matplotlib.pyplot as plt
# with open("ml-results/model-300-tanh-mse-sgd/distances.h", "rb") as f:
#     distances = pickle.load(f)
#     print(len(distances))
#     print(np.min(distances))
#     print(np.max(distances))
#     print(np.mean(distances))
#     plt.plot(list(zip(*distances))[0])
#     plt.show()
