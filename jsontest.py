import json

data = ['name', [1], {'yeet':'lol'}, 69, 420, [123,456], [123,456], [78,90], {'yeet':{'i wanna die':'lol'}}, {'yeet':{'i wanna die':'lol'}}]


json_string = json.dumps(data)
print(json_string)
with open('json_data.json', 'w') as outfile:
    json.dump(json_string, outfile)