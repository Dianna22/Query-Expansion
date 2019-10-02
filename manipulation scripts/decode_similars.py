phrases = dict()
with open("../no_dublicates/phrases", "rb") as f:
    line = f.readline()
    while line:
        id, phrase = line.decode().split(",")
        phrases[int(id)] = phrase
        line = f.readline()
return phrases


def decode(suffix, output_file):

    with open("wn-id-pairs-" + suffix, "r") as f:
