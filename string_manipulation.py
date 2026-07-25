#Tracking individual letters
name = "Rodeena"
print(name[0])  # R, we start counting from 0
print(name[-1])  # a, when we count left to right we can use negative numbers to count from the end of the string
print(name[3])  # e

#Using String Methods
town = "New York"
print(town.upper())  # NEW YORK, converts all letters to uppercase
print(town.lower())  # new york, converts all letters to lowercase
print(town.capitalize())  # New york, converts the first letter to uppercase and the rest to lowercase
print(town.title())  # New York, converts the first letter of each word to uppercase and the rest to lowercase

text = "   Hello, World!   "
month = "  January Festival  " 
print(text.strip())  # Hello, World!, removes whitespace from the beginning and end of the string
print(month.upper())  # JANUARY FESTIVAL, converts all letters to uppercase
print(month.strip())  # January Festival, removes whitespace from the beginning and end of the string

