import json

with open('test.json') as f:
    data_listofdict = json.loads(f.read())

print(data_listofdict)