def loadPhrases(file):
    phrases = dict()
    with open(file, "rb") as f:
        line = f.readline()
        while line:
            id, phrase = line.decode().split(",")
            phrases[int(id)] = phrase
            line = f.readline()
    return phrases

def decodePredictedPhrases(predictions, db):
    with open(predictions, "r") as f:
        line = f.readline()
        while line:
            id1, id2 = line.split(",")
            id1, id2 = int(id1), int(id2)
            print(db[id1], db[id2])
            line = f.readline()

def loadTestDict(file):
    testSet = {}
    with open(file, "r") as f:
        line = f.readline()
        while line:
            id1, id2 = line.split(",")
            id1, id2 = int(id1), int(id2)
            if id1 in testSet.keys():
                testSet[id1].append(id2)
            else:
                testSet[id1] = [id2]
            line = f.readline()
    return testSet

def testModel(prediction_file, testSet):
    total, hits = 0, 0
    with open(prediction_file, "r") as f:
        line = f.readline()
        while line:
            id1, id2 = line.split(",")
            id1, id2 = int(id1), int(id2)
            if id1 in testSet.keys():
                if id2 in testSet[id1]:
                    hits += 1
            elif id2 in testSet.keys():
                if id1 in testSet[id2]:
                    hits += 1
            total += 1
            line = f.readline()
    if total == 0:
        return -1
    return hits * 100 / total

phrases = loadPhrases("embeddings/phrases-2words")

decodePredictedPhrases("embeddings/predictions", phrases)

# testDict = loadTestDict("embeddings/wn-training-id-pairs-train")
testDict = loadTestDict("embeddings/wn-testing-id-pairs")

testModel("embeddings/predictions-test",testDict)