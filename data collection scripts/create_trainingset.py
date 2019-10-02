from textblob import TextBlob
import elasticsearchHelper as esh
import similar_phrases as sp
import string, re, json, os
import time
import numpy as np

class Article:
    def __init__(self, text):
        self.text = text

    def remove_punctuation(self):
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        self.text = regex.sub(' ', self.text)

    def extractNP(self):
        return TextBlob(self.text).noun_phrases

def check_end_of_file(counter, max, file_name, file_handler=None):
    if file_handler == None:
        file_handler = open(file_name, "w")
    if counter % max == 0 and counter:
        file_name += "-" + str(counter / max)
        mode = "a"
        file_handler.close()
        file_handler = open(file_name, mode)
    return (file_name, file_handler)

def save_similar_phrases(id, phrases, temp_file, phrases_file_name,
                        phrases_per_file, training_data_file_name):
    prag = 1000
    (phrases_file_name, phrases_f) = \
        check_end_of_file(id, phrases_per_file, phrases_file_name)
    with open(training_data_file_name, "w") as training:
        for phrase in phrases:
            phrases_f.write(str(id) + " " + phrase + "\n")
            id_match_1 = id
            sp.similar_phrases_wn_file(phrase, temp_file)
            with open(temp_file) as file:
                for line in file:
                    similar_obj = json.loads(line)
                    if not type(similar_obj)==int:
                        for match in similar_obj:
                            id += 1
                            (phrases_file_name, phrases_f) = \
                                check_end_of_file(id, phrases_per_file, phrases_file_name, phrases_f)
                            phrases_f.write(str(id) + " " + match + "\n")
                            training.write(str(id_match_1) + "," + str(id) + "\n")
                            break
            id += 1
            if id >prag:
                print(id)
                prag += 1000
    return (id, phrases_file_name)

def filterPhrases(phrases, es):
    """
    Keep 2-words phrases that have an exact match in the corpus
    :param phrases:
    :return:
    """
    return [phrase for phrase in phrases if len(phrase.split())==2 and es.searchPhrase("revision", phrase)]

def savePhrases(phrases, file, id):
    with(open(file, "ab")) as f:
        for phrase in phrases:
            f.write((str(id) + ",").encode('utf-8'))
            f.write((phrase + "\n").encode('utf-8'))
            # f.write("\n")
            id+=1
    return id

def create_trainingset(index_name, output_dir, phrases_file_name,
                       phrases_per_file, training_data_file_name, temp_file="temp"):
    temp_file = os.path.join(output_dir, temp_file)
    training_data_file_name = os.path.join(output_dir, training_data_file_name)
    phrases_file_name = os.path.join(output_dir, phrases_file_name)

    articles = esh.IndexHelper(index_name)
    max_slices = 1000
    id = 0
    for i in range(max_slices):
        if i %10==0:
            print("i", i)
        list_of_articles = articles.getArticlesPaginated(i,max_slices)
        length = len(list_of_articles)
        for article in list_of_articles:
            art = Article(article["_source"]["revision"])
            try:
                if art.text:
                    art.remove_punctuation()
                    # extract phrases from indexed articles
                    phrases = filterPhrases(art.extractNP(), articles)
                    # print(len(phrases))
            except Exception as e:
                print(e)
                print(art.text)
            # save the phrases and their similar correspondants
            # and give them ids


            id = savePhrases(phrases, phrases_file_name, id)

            # (id, phrases_file_name) = save_similar_phrases(id, phrases, temp_file, phrases_file_name,
            #                             phrases_per_file, training_data_file_name)

# t1 = time.time()
# create_trainingset("wiki-revision","embeddings","phrases-2words",20000,"trainSet")
# t2 = time.time()
# print("Exe time ", t2-t1, "s")
# print("Exe time ", (t2-t1)/60, "min")

def load_phrases(phrases_file):
    phrases = dict()
    touples = []
    count = 0
    with open(phrases_file, "r", errors="ignore") as f:
        line = f.readline()
        while line:
            phrase_id, phrase, score = line.split("\n")[0].split(",")
            phrase_id = int(phrase_id)
            touples.append((phrase_id, phrase))
            if phrase in phrases.keys():
                print("phrase already there {} {}".format(phrases[phrase],phrase_id))
            phrases[phrase] = phrase_id
            line = f.readline()
            count+=1
            if count %10000 == 0:
                print("Loaded %s phrases" % count)
    print("[FINISH] Loaded %s phrases" % len(phrases.keys()))
    return phrases, touples

def generate_id_pairs_of_similar_phrases_wn(phrases_file, output_file, from_id, to):
    # index_name="wiki-revision"
    # es = esh.IndexHelper(index_name)

    with open("siblings/phrases-2words-append-2", "a", errors="ignore") as nf:
        progress = 0
        similar_number = []
        not_found = []
        running_times = []
        times = []
        numbers = []
        phrases_db, touples = load_phrases(phrases_file)
        nf_id = max([int(x) for x in phrases_db.values()]) + 1
        t = time.time()
        with open(output_file, "w") as f:
            print("{} phrases".format(len(phrases_db.items())))
            for id, phrase in touples[from_id:to]:
                phrase = phrase.strip()
                if progress % 10 == 0:
                    t2 = time.time()
                    print("****************************")
                    print("{}-{} item {} elapsed {} min {} s {} s".format(from_id, to, progress, (t2 - t) // 60, t2 - t - ((t2-t)//60)*60, t2-t))
                    print("****************************")
                progress += 1
                # print("Generating similarities for id %s" % id)
                t1 = time.time()
                similarities = sp.Similar(phrase).similar_phrases_wn()
                tt = time.time()
                times.append(float(tt-t1))

                # similars_found_in_db = 0
                similarities = list(set(similarities))
                filtered_nr_similars = 0
                for similar_phrase in similarities:
                    similar_phrase = similar_phrase.strip()
                    if similar_phrase == phrase:
                        continue
                    nf.write(phrase + "," + similar_phrase + "\n")
                    filtered_nr_similars += 1
                    nf_id += 1
                    similar_id = nf_id
                    # similar_id = phrases_db.get(similar_phrase)
                    # if similar_id and similar_id != id:
                    #     similars_found_in_db += 1
                    # else:
                    #     res = es.searchPhrase("revision", similar_phrase)
                    #     nf.write(phrase + "," + similar_phrase + "\n")
                    #     nf_id += 1
                    #     similar_id = nf_id
                    #     not_found.append(similar_phrase)
                    # print(id, ",", similar_id, file=f)
                    #if phrase != similar_phrase:
                    print(phrase+ ","+ similar_phrase, file=f)
                similar_number.append(filtered_nr_similars)
                t2 = time.time()
                running_times.append(t2-t1)
                # if similars_found_in_db != len(similarities):
                #     print("{} phrases found in db out of {} generated".format(similars_found_in_db, len(similarities)))
                print("id {} took {} min {} s".format(id, (t2-t1)//60, t2-t1-(t2-t1)//60*60))
    # print("Not found: {}", not_found)
    print("Avg no of similarities per phrase is %s" % np.mean(np.array(similar_number)))
    print("Avg time per phrase is {} s".format(np.mean(running_times)))
    return times, np.array(similar_number)


suffix = "500-1000"
t1 = time.time()
# generate_id_pairs_of_similar_phrases_wn("embeddings/phrases-2words", "trainingSet/wn-id-pairs-1800-20001", 1800, 2000)
exet, number = generate_id_pairs_of_similar_phrases_wn("siblings/valid-phrases", "siblings/wn-filtered-pairs-"+suffix, 500, 1000)
t2 = time.time()
def formattime(t):
    return str(t // 3600) + "h "\
                 + str((t - t // 3600 * 3600) // 60) + "min "\
    + str(t - t // 3600 * 3600 - (t - t // 3600 * 3600) // 60 * 60) + "s"
import pickle
with open("siblings/timenumber-filtered-"+suffix+".h", "wb") as f:
    pickle.dump(exet, f)
    pickle.dump(number, f)

with open("siblings/metrics-filtered-"+suffix,"w") as f:
    print("Exe time ", t2-t1, "s", file=f)
    print("Exe time ", (t2-t1-(t2-t1)//3600*3600)//60, "min", file=f)
    print("Exe time ", (t2-t1)//3600, "h", file=f)
    mintime = np.min(exet)
    print("Min time per phrase " +  formattime(mintime), file=f)

    maxtime = np.max(exet)
    print("Max time per phrase " +  formattime(maxtime), file=f)

    avgtime = np.mean(exet)
    print("Avg time per phrase " +  formattime(avgtime), file=f)

    print(number)
    minno = np.min(number)
    print("Min no of sim ph per phrase " + str(minno), file=f)

    maxno = np.max(number)
    print("Max no of sim ph per phrase " + str(maxno), file=f)

    avgno = np.mean(number)
    print("Avg no of sim ph per phrase " + str(avgno), file=f)

# with open("siblings/lists-"+suffix, "w") as f:
    print(exet, file=f)
    print(number, file=f)
#
# import pickle
# with open("siblings/timenumber-1-100.h", "rb") as f:
#     lst=pickle.load(f)
#     print(lst)

