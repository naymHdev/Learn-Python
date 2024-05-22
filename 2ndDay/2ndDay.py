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
getN = nStr[-12:-8]
print("Get Negative Idx", getN)


# String Function's

# Check string ending's
check = "Hello Bangladesh Team Best off luck."
cEnd = check.endswith("ck.")
print('Check Ending', cEnd)

# Create a new string the  capitalize() function
print(check.capitalize())

# Replacing function
# The function replace the value ... get a new string
replace = check.replace("luck", "mara kau⏂")
print(replace)

# Find function
# the function also check the value which number index are available...
getFind = check.find("t")
print(getFind)

# Count function
# this function check how many time the value exists...
getCount = check.count("a")
print(getCount)


# Let's Practice's

# P1. WAP to input user’s first name & print its length.
practice1 = input("First: ")
getInputLength = len(practice1)
print("getInputLength", getInputLength)

# P2. WAP to find the occurrence of ‘$’ in a String.
practice2 = "Hi i am get a 200$. and my bill 10$ and i am by a cricket ball to 20$."
getResult = practice2.count("$")
print("$ = :", getResult, "Time")


# Conditionals Statement
age = 23

if (age >= 10):
    {
        print("Applying a voter Id")
    }
else:
    {
        print("Not applying")
    }

amount = 200

if (amount < 100):
    print("Buy a PiaZZa")
elif (amount <= 500):
    print("Buy a cricket bat")
elif (amount == 200):
    print("Buy a car")
else:
    print("Don't buy anything, saving")
