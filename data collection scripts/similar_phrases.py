from lexicon import WNLexicon
import itertools, gcsapi, json, os
import time

import elasticsearchHelper as es
# queries per 100 secs per user are limited to 100
PAUSE_AFTER = 100
PAUSE = 10

def computeScore(phrase, index):
    # res = index.multiFieldSearchPhrase(["title", "revision"], phrase=phrase)
    res = index.searchPhrase("revision", phrase=phrase)
    score = {
        "freq": res["hits"]["total"],
        "max": res["hits"]["max_score"]
    }
    return score

def _generate_phrases_file(siblings, file_name, error_file=""):
    esIndex = es.IndexHelper("wiki-revision")
    result_number, index = 1,0
    file = open(file_name, "w")
    if os.path.exists(error_file):
        mode = "a"
    else:
        if error_file == "":
            error_file = file_name + "_api_errors"
        mode = "w"
    for phrase in itertools.product(*siblings):
        query = ' '.join(phrase).replace("_", " ")
        index += 1
        result = {query : None}
        # if index % PAUSE_AFTER == 0:
        #     time.sleep(PAUSE)
        #     print("pause ended " + str(index) + " - query " + query)
        if result_number % 20000==0:
            file.close()
            file = open(file.name+"-"+str(result_number/20000), "w")
        try:
            # score = gcsapi.google_search_frequency(query)
            score = computeScore(query, esIndex)
            result[query] = score
            # if index %100 == 0:
            #     print(index, query, score)
            if score["max"] > 0:
                # print(query, score)
                json.dump(result,file)
                file.write("\n")
                result_number += 1
        except:
            error_file_handler = open(error_file, mode)
            json.dump(result, error_file_handler)
            error_file_handler.close()
    file.write(str(result_number-1) + "\n")
    file.close()
    return result_number-1

def similar_phrases_wn_file(phrase, file):
    wn = WNLexicon()
    words = phrase.split()
    siblings = [[word] for word in words]
    for i,word in enumerate(words):
        siblings[i] += wn.get_similar(word)
    # print("siblings: " + str(siblings))
    return(_generate_phrases_file(siblings, file))


class Similar:
    def __init__(self, phrase):
        self.phrase = phrase
        self.similar_phrases = []
        self.full_results = []

    def _generate_phrases(self, siblings):
        esIndex = es.IndexHelper("wiki-revision")
        result_number, index = 1,0
        for phrase in itertools.product(*siblings):
            query = ' '.join(phrase).replace("_", " ")
            index += 1
            result = {query : None}
            score = computeScore(query, esIndex)
            result[query] = score
            if score['max'] and score['max'] > 0 and score["freq"]>0:
                self.similar_phrases.append(query)
                self.full_results.append(result)
    def similar_phrases_wn(self):
        wn = WNLexicon()
        words = self.phrase.split()
        siblings = [[word] for word in words]
        for i,word in enumerate(words):
            siblings[i] += wn.get_similar(word)
        self._generate_phrases(siblings)
        return self.similar_phrases


# now = time.time()
#
# path = "results/business_expenses.txt"
# f = open(path, "w")
# similar_phrases_wn("aorta blood co2", f)
# print(similar_phrases_wn("blue eyes", f))
# print(similar_phrases_wn("business expenses", f))
# total_time = time.strftime("%H:%M:%S", time.gmtime(time.time()-now))
# print(total_time)
# with open(path, "a") as f:
#     print(total_time, file=f)
