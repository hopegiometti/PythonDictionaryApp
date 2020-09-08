import json
#python standard libraries
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("files/data.json"))
# print(data["rain"])
# print(get_close_matches("rainn", list(data.keys())))

def returnaword(w):
    fixedword = w.lower()
    if fixedword in data:
        return data[fixedword]
    elif len(get_close_matches(fixedword, list(data.keys()), cutoff=0.8)) > 0:
        close_ws = get_close_matches(fixedword, list(data.keys()), cutoff=0.8)
        closest = close_ws[0]
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % closest)
        if yn == "Y":
            return data[closest]
    else:
        return "This word does not exist. Please double check your spelling!"

word = input("Enter word: ")

print(returnaword(word))


