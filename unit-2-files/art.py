import json

with open('asian-20181028.json') as artfile:
    art = json.load(artfile)
    print(art['description'])
