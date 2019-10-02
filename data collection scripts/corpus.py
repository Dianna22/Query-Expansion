import ijson, codecs, json, time, datetime
from itertools import islice
huge_path = "I:\\latest-all.json"

# huge_path = "index/doc1.json"


def retrieveFirstItems(number, from_path, to_path):
    with open(from_path, 'r') as f:
        objects = list(islice(ijson.items(f, 'item'), number))
        with codecs.open(to_path, "w", "utf-8") as w:
            # w.write(objects)
            try:
                json.dump(objects,w,indent=2)
            except:
                pass

# retrieveFirstItems(2, huge_path, "res",)

def extractDescriptions(number, from_path, to_path):
    with open(from_path, 'r') as f:
        objects = islice(ijson.items(f, 'item'), number)
        with codecs.open(to_path, "w", "utf-8") as w:
            # w.write(objects)
            for o in objects:
                obj = {"id": o["id"], "desc": str(o["descriptions"]["en"]["value"])}
                json.dump(obj,w)
                w.write(",")

def extractAllDescriptions(from_path, to_path, extension=".json", chunk_dim=50000, continue_with=0):
    count = 0
    fileNumber = 0
    with open(from_path, 'r') as f:
        parser = ijson.parse(f)
        obj = {}
        if fileNumber >= continue_with:
            w = codecs.open(to_path +"-"+ str(fileNumber) + extension, "w", "utf-8")
        for prefix, event, value in parser:

            if prefix=="item.id":
                obj["id"] = value
            elif prefix=="item.descriptions.en.value" and len(value.split())>1:
                obj["description"] = value
                if fileNumber >= continue_with:
                    json.dump(obj, w)
                obj = {}
                count+=1
                if count %chunk_dim ==0:
                    if fileNumber >= continue_with:
                        w.close()
                    fileNumber += 1
                    if fileNumber >= continue_with:
                        w = codecs.open(to_path +"-"+ str(fileNumber) + extension, "w", "utf-8")
                    print(count)
                else:
                    w.write("\n")
        w.close()
                # obj = {"id": o["id"], "desc": str(o["descriptions"]["en"]["value"])}
start_time = time.time()
extractAllDescriptions(huge_path, "F:\wiki\descriptions_all")
# extractAllDescriptions(huge_path, "descriptions_all.json")
print(time.strftime("%H:%M:%S", time.gmtime(time.time()-start_time)))