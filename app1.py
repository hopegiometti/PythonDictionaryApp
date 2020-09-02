import json
data = json.load(open("files/data.json"))
# print(data["rain"])

def returnaword(w):
    return data[w]

print(returnaword("rain"))