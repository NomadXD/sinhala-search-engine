import glob
import json
from typing import cast
from mtranslate import translate

files = glob.glob("corpus/en/*")

for file in files:
    data = open(file)
    politician = json.load(data)
    print(politician["_values"])
    politician_json = politician["_values"]
    
    if politician_json["career"] != None: 
        politician_json["career"] = translate(politician_json["career"], "si", "en")

    if politician_json["civil_status"] != None: 
        politician_json["civil_status"] = translate(politician_json["civil_status"], "si", "en")

    if politician_json["committees"] != None:
        committees_si = []
        for committee in politician_json["committees"]:
            committee_si = translate(committee, "si", "en")
            committees_si.append(committee_si)
        politician_json["committees"] = committees_si

    if politician_json["electoral"] != None: 
        politician_json["electoral"] = translate(politician_json["electoral"], "si", "en")

    if politician_json["name"] != None: 
        politician_json["name"] = translate(politician_json["name"], "si", "en")

    if politician_json["occupation"] != None: 
        politician_json["occupation"] = translate(politician_json["occupation"], "si", "en")

    if politician_json["party"] != None: 
        politician_json["party"] = translate(politician_json["party"], "si", "en")

    if politician_json["portfolio"] != None: 
        politician_json["portfolio"] = translate(politician_json["portfolio"], "si", "en")

    if politician_json["religion"] != None: 
        politician_json["religion"] = translate(politician_json["religion"], "si", "en")
    output = open("corpus/si/{file}".format(file= file.split("/")[-1]), "w+")
    json.dump(politician_json, output)


# data = open("corpus/en/3449.json")
# politician = json.load(data)
# print(politician["_values"])
# politician_json = politician["_values"]
# print(politician_json["committees"])

# if politician_json["career"] != None: 
#     politician_json["career"] = translate(politician_json["career"], "si", "en")

# if politician_json["civil_status"] != None: 
#     politician_json["civil_status"] = translate(politician_json["civil_status"], "si", "en")

# if politician_json["committees"] != None:
#     committees_si = []
#     for committee in politician_json["committees"]:
#         committee_si = translate(committee, "si", "en")
#         committees_si.append(committee_si)
#     politician_json["committees"] = committees_si

# if politician_json["electoral"] != None: 
#     politician_json["electoral"] = translate(politician_json["electoral"], "si", "en")

# if politician_json["name"] != None: 
#     politician_json["name"] = translate(politician_json["name"], "si", "en")

# if politician_json["occupation"] != None: 
#     politician_json["occupation"] = translate(politician_json["occupation"], "si", "en")

# if politician_json["party"] != None: 
#     politician_json["party"] = translate(politician_json["party"], "si", "en")

# if politician_json["portfolio"] != None: 
#     politician_json["portfolio"] = translate(politician_json["portfolio"], "si", "en")

# if politician_json["religion"] != None: 
#     politician_json["religion"] = translate(politician_json["religion"], "si", "en")
# print(politician_json)
# output = open("corpus/si/3449.json", "w+")
# json.dump(politician_json, output)


        

