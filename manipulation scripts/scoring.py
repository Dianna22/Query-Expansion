from numpy import asarray
import numpy as np
embeddings = dict()
def load_embeddings(embeddings_file):
    global embeddings
    with open(embeddings_file, 'rb') as f:
        for line in f:
            values = line.split()
            word = values[0].decode('utf-8')
            coefs = asarray(values[1:], dtype='float32')
            embeddings[word] = coefs




def computeScore3(similars):
    """
    frequence of the generated phrase in the corpus
    :param phrase: 2-word phrase
    :return: score
    """
    try:
        results = []
        for phrase in similars:
            words = phrase.split(" ")
            embedding1 = embeddings.get(words[0], None)
            embedding2 = embeddings.get(words[1], None)
            if embedding1 is not None and embedding2 is not None:
                results.append((phrase, np.exp(np.dot(embedding1, embedding1))))
            else:
                results.append((phrase,0))
        sum = np.sum([score for (phrase, score) in results])
        return [(phrase,score/sum) for (phrase, score) in results]
    except:
        print(words)
        print("asd")

def computeScore(similars):
    """
    for a fixed word, rank the possibilities of the other words in the phrase
    :param phrase: 2-word phrase
    :return: score
    """
    try:
        results = []
        data =dict()
        for phrase in similars:
            words = phrase.split(" ")
            if len(words) != 2:
                continue
            if words[0] in data.keys():
                data[words[0]].append(words[1])
            else:
                data[words[0]] = [words[1]]
        for word in data.keys():
            result = []
            embedding1 = embeddings.get(word, None)
            for phraseWord in data[word]:
                embedding2 = embeddings.get(phraseWord, None)
                if embedding1 is not None and embedding2 is not None:
                    result.append((word + " " + phraseWord, np.exp(np.dot(embedding1,embedding2))))
                else:
                    result.append((phrase,0))
            sum = np.sum([score for (ph,score) in result])
            results.extend([(phrase,score/sum) for (phrase, score) in result])
        return results

    except:
        print(words)
        print("asd")


def computeScore2(similars):
    """

    :param phrase: 2-word phrase
    :return: score
    """
    try:
        results = []
        for phrase in similars:
            words = phrase.split(" ")
            embedding1 = embeddings.get(words[0], None)
            embedding2 = embeddings.get(words[1], None)
            if embedding1 is not None and embedding2 is not None:
                results.append((phrase, np.dot(embedding1, embedding1)))
            else:
                results.append((phrase,0))
        return results
    except:
        print(words)
        print("asd")

def addScoring(input):
    dataset = dict()
    with open(input, "r") as f:
        line = f.readline()
        while line:
            (phrase1, phrase2) = line.split(",")
            phrase2 = phrase2.strip()
            if phrase1 in dataset.keys():
                dataset[phrase1].append(phrase2)
            else:
                dataset[phrase1] = [phrase2]
            line = f.readline()
    for phrase, similars in dataset.items():
        dataset[phrase] = computeScore(similars)

    with open(input + "-scoring-wordbased", "w") as g:
        for phrase, scores in dataset.items():
            result = "\n".join([similar_phrase +"-"+ str(score) for (similar_phrase, score) in sorted(scores, key=lambda x: x[1], reverse=True)])
            g.write(phrase + ":\n" + result+"\n")


if __name__ == "__main__":
    load_embeddings("P:\III\Graduation thesis\\thesis\similar_phrases\glove.6B\glove.6B.300d.txt")
    addScoring("wn-id-pairs-1-100")