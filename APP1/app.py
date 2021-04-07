import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("./data.json"))


def getWord():
    a = input("Enter a word: ")
    a = a.lower()
    return a


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def wordSuggestion(i):
    x = input(f"Did you mean: {i} ? (Y/N)")
    return x.lower()

def getMeaning(a):
        key = data.keys()
        i = get_close_matches(a, key, n=1, cutoff=0.85)
        if i:
            i = i[0]
            if similar(i, a)==1:
                return data[a]
            else:
                if wordSuggestion(i)=='y':
                    return data[i]
                else:
                    return 0
        else:
            return 0
        """for i in key:
            if(similar(i, a)==1):
                return data[a]
            if(similar(i, a)>0.8):
                if(wordSuggestion(i)=='y'):
                    return data[i]
                else:
                    return NULL
        """          
    
        
a = getWord()

value = getMeaning(a)        
print("\n")
if(value):
    for x in value:
        print(x + "\n")
else:
    print("Word Not Found\n")