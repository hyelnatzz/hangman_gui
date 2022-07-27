import json
import string


# ++++ REMOVING LIST FROM DEFINITIONS
def delist(val):
    """create numbered definitions"""
    dfn = ''
    index = 1
    for i in val:
        dfn += str(index) + '. ' + i + '\n'
        index += 1
    return dfn

word = {}

#CREATE GAME READY DICTIONARY JSON
with open('data.json','r') as data:
    content = json.load(data)

print('started...')
for k,v in content.items():
    if ' ' not in k and len(k) <= 10 and len(k) >= 4 and k[0] in string.ascii_lowercase:
        if len(v) > 1:
            word[k] = delist(v)
        else:
            word[k] = v[0]


with open('semicleaned.json', 'a+') as new:           
    json.dump(word, new)


#print('Done...')
#print(delist(content['dance']))


#sentence = '1. Simple, green, aquatic plants without stems, roots or leaves. They are found floating in the sea and fresh water, but they also grow on the surface of damp walls, rocks, the bark of trees and on soil.\\n(Source: WRIGHT)'
## +++++++++++ REMOVING 'SOURCE INFORMATION FROM DEFINITIONS
def removeSource(val):
    strt = val.find('\\n(Source:')
    end = val.find(')', strt)
    return val.replace(val[strt : end + 3], '')


with open('semicleaned.json', 'r') as data:
    content = json.load(data)


for k, v in content.items():
    word[k] = removeSource(v)

with open('withoutsource.json', 'a+') as new:
    json.dump(word, new)

print(content['cloud'])