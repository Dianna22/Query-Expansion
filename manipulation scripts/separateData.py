# total = 1526
# from random import shuffle
#
# lines = []
# def load():
#     with open("wn-id-pairs-1-500", "r") as g:
#         line = g.readline()
#         while line:
#             if len(line.split(",")[1].split(" ")) == 2:
#                 lines.append(line)
#             line = g.readline()
#     with open("wn-id-pairs-500-1000", "r") as g:
#         line = g.readline()
#         while line:
#             if len(line.split(",")[1].split(" ")) == 2:
#                 lines.append(line)
#             line = g.readline()
#     with open("wn-id-pairs-1000-1500", "r") as g:
#         line = g.readline()
#         while line:
#             if len(line.split(",")[1].split(" ")) == 2:
#                 lines.append(line)
#             line = g.readline()
#     with open("wn-id-pairs-1500-2000", "r") as g:
#         line = g.readline()
#         while line:
#             if len(line.split(",")[1].split(" ")) == 2:
#                 lines.append(line)
#             line = g.readline()
# load()
# print(len(lines))
# eightyperscent = 80*len(lines)//100
# shuffle(lines)
# with open("trainingSet", "w") as ts:
#     ts.write("".join(lines[:eightyperscent]))
# with open("validationSet", "w") as vs:
#     vs.write("".join(lines[eightyperscent:]))
    # print(len(written.keys()))
    # print((written.keys()))

with open("trainingSet", "r") as f:
    phrases = dict()
    line1 = f.readline()
    count=0
    while line1:
        count +=1
        phrase1 = line1.split(",")[0].strip()
        phrases[phrase1] = True
        line1 = f.readline()
    print(len(phrases.keys()))
    print(count)

with open("validationSet", "r") as f:
    phrases = dict()
    line1 = f.readline()
    count = 0
    while line1:
        count +=1
        phrase1 = line1.split(",")[0].strip()
        phrases[phrase1] = True
        line1 = f.readline()
    print(len(phrases.keys()))
    print(count)

    # print(phrases.keys())
    # print(len(set(phrases)))