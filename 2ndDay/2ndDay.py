"""  
Chapter - 2
Today Cover Some Python Topics are,
Strings & Conditionals Statement.

 """

# Type of some string's
string1 = 'this is a string'
string2 = "this is a string"
string3 = """this is a string"""

# Get a line break use the \n function
string4 = "very bad team in the bangladesh \nteam on the 2024 T20 World Cup Team"

# Get A String length use the len() function
print("Get Length = ", len(string4))

# Indexing [Like, Its total JS Index]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
congratulation = "Hello Bangladesh Team Best off luck."
findIndex = congratulation[10]
print("findIndex = ", findIndex)

# Slicing
strSlice = "Hello Bangladesh Team Best off luck."
findSlice = strSlice[5:16]
print("Get slice = ", findSlice)

# Get a last index
lastIndex1 = strSlice[5:]
lastIndex2 = strSlice[5: len(strSlice)]
print('Get Last Idx = ', lastIndex1, lastIndex2)

# Negative index Slicing
nStr = "I love you  Python"
getN = nStr[-12 :-8]
print("Get Negative Idx", getN)
