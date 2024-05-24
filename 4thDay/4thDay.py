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
# print(len(list(myDict.keys())))


# myDict.values( ) #returns all values
# print(myDict.values())
# print(list(myDict.values()))
# print(len(list(myDict.values())))


# myDict.items( ) #returns all (key, val) pairs as tuples
# print(myDict.items())
pairs = list(myDict.items())
# print(pairs[0])


# myDict.update( newDict ) #inserts the specified items to the dictionary

# myDict.get( “key““ ) #re


""" Set Methods In Python3 """
#  Duplicate value not accepted the set methods...

collection = {1, 1, 2, 3, 2, 3, 4, 5, 6, 4, 5, 6, "naym", 'nhDev', 'naym'}
# print(collection)
# print(type(collection))
# print(len(collection))

# Create a empty set function
emptySet = set()
# print(type(emptySet))

""" Some Set Methods """

# Added method collect.add()
# add method except a tuple  but don't except any list or object
emptySet.add(1)
emptySet.add((3, 2, 3, 4, "Leo"))
emptySet.remove(1)
# print(emptySet)


info = {1, 1, 2, 3, 2, 3, 4, 5, 6, 4, 5, 6, "naym", 'nhDev', 'naym'}

print(info.pop())

# print(info.clear())

""" Let‘s Practice """

""" 
Store following word meanings in a python dictionary :

table : “a piece of furniture”, “list of facts & figures”
cat : “a small animal”

You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.

”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”, “java”, “C++”,“C”
 """

""" 
WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value.

Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)
 """
