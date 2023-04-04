# open countries.json and group them on the basis of continent

import json
import time

dict ={
    "Asia": [],
    "Africa": [],
    "Europe": [],
    "Americas": [],
    "Oceania": []
}

with open('countries.json') as f:
    data = json.load(f)
    for i in data:
        if i['region'] in dict:
            dict[i['region']].append(i['alpha-2'])
    print("All done")

print(dict)