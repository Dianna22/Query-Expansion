import numpy as np
def metrics(file_suffix):
    results = []
    with open("wn-id-pairs-" + file_suffix) as f:
        nr_similars = 0
        phrase1 = f.readline().split(",")[0]
        phrase2 = f.readline().split(",")[0]
        while phrase2:
            nr_similars = 1
            while phrase2 and phrase2 == phrase1:
                nr_similars += 1
                phrase2 = f.readline().split(",")[0]
            results.append(int(nr_similars))
            phrase1 = phrase2
            phrase2 = f.readline().split(",")[0]
    with open("wn-id-pairs-" + file_suffix) as f:
        line = f.readline()
        while line:
            line = line.split(",")
            if line[0].strip() == line[1].strip():
                print("!!!!!!!!!!!!!!!!!!!!!!")
                print(line)
                print("!!!!!!!!!!!!!!!!!!!!!!")
            line = f.readline()
    return results


results = metrics("1-500")
results += metrics("500-1000")
results += metrics("1000-1500")
results += metrics("1500-2000")
# print(results)
results = np.array(results)
print("%%%%%%%")
print("results")
print(len(results))
print(np.max(results))
print(np.min(results))
print(np.mean(results))
print("%%%%%%%")
print(results)

import pickle

def metrics(suffix):
    with open("timenumber-" + suffix+".h", "rb") as f:
        exe_time = pickle.load(f)
        number = pickle.load(f)
    return np.array(exe_time), np.array(number)
exe, nr = [],[]
exetemp, nrtemp = metrics("1-500")
exe = np.concatenate((exetemp, exe))
nr = np.concatenate((nrtemp, nr))

exetemp, nrtemp = metrics("500-1000")
exe = np.concatenate((exetemp, exe))
nr = np.concatenate((nrtemp, nr))

exetemp, nrtemp = metrics("1000-1500")
exe = np.concatenate((exetemp, exe))
nr = np.concatenate((nrtemp, nr))

exetemp, nrtemp = metrics("1500-2000")
exe = np.concatenate((exetemp, exe))
nr = np.concatenate((nrtemp, nr))

indexes = [i for i in range(len(nr)) if nr[i]==1]
nr = [nr[x] for x in range(len(nr)) if x not in indexes]
exe = [exe[x] for x in range(len(exe)) if x not in indexes]
exemax = np.max(exe)
print(exemax)
exe = [a for a in exe if a != exemax]
print(np.max(exe))
print(nr)
print(len(nr))
print("%%%%%%%%%%%%")
print("exe time")
exet = np.array(exe)
print(len(exet))
print(np.max(exe))
print(np.min(exe))
print(np.mean(exe))

print("%%%%%%%%%%%%")

print("%%%%%%%%%%%%")
print("Number")
nr = np.array(nr)
print(len(nr))
print(np.max(nr))
print(np.min(nr))
print(np.mean(nr))
print("%%%%%%%%%%%%")
import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
print(compare(nr, results))
print(np.sum(exe))
import matplotlib as plot
from matplotlib import pyplot as plt
# n,hist, patches = plt.hist(results)
plt.plot([i for i in range(len(exet))], exet, 'o-')
# plt.axis([1, len(results), np.min(results)-5, np.max(results)])
plt.title("Execution time for similar phrase generation (for " + str(len(exe)+1) + " phrases)")
plt.show()
# with open("metrics-1-500-siblings and children", "w") as f:
#     print("Phrases " + str(len(results)), file=f)
#     print("Avg " + str(np.mean(results)), file=f)
#     print("Max " + str(np.max(results)), file=f)
#     print("Min " + str(np.min(results)), file=f)
