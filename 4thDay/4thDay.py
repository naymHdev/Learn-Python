""" 4th Day || Lecture - 4 """

""" Topics || Dictionary & Set """


# Dictionary Like of JavaScript Object [ value : keys] it's a mutable and don't allow duplicate's keys
isInfo = {
    "name": "swift",
    "age": 25,
    "country": "United States",
    "role": "singer",
    "girlfriend": ["ena", "ane", "lui", "mou"]
}

# print(type(isInfo), isInfo)
# print(isInfo['girlfriend'])


""" Nested Dictionary """
myDict = {
    'name': 'kauaa kader',
    'age': 24,
    'country': 'Bangladesh',
    'collage_name': 'Bangladesh University',
    'department': 'economics',
    'subject_marks': {
        "international_eco": 3.4,
        "traditional_eco": 4,
        "environmental_eco": "Fail"
    },
    "Ranking": "None"
}
# print(myDict)

""" Dictionary Methods """


# myDict.keys( ) #returns all keys
# print(myDict.keys())
# print(list(myDict.keys()))

# Get a dict_ length
print(len(list(myDict.keys())))


# myDict.values( ) #returns all values
# print(myDict.values())
# print(list(myDict.values()))
print(len(list(myDict.values())))


# myDict.items( ) #returns all (key, val) pairs as tuples
# print(myDict.items())
pairs = list(myDict.items())
print(pairs[0])


# myDict.update( newDict ) #inserts the specified items to the dictionary

# myDict.get( “key““ ) #re
