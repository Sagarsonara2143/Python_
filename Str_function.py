str = "Python Programming"

print(str)

print(str.capitalize())         # First Word Capetilize -- Python programming --
print(str.casefold())           # Lower case - python programming --
print(str.lower())              # Lower case - python programming --
print(str.upper())              # Upper case - Capital all char in str
print(str.center(40))           # Print string in Center aling space of 40 char
print(str.center(40, "*"))      # same as above with space occupied with *
print(str.count("P"))           # Count Char in str (Result - 2)
print(str.startswith("Pro"))    # Str check and result will be in Boolean (False)
print(str.endswith("ing"))      # Str check and result will be in Boolean (True)
print(str.find("o"))            # str check char and result will be index of first found
print(str.find("o",5))          # str check char from 5th index and result will be index of first found
print(str.find("o",5,1))        # reverse counting from 5th index
print(str.index("o"))           # find index of specified Char
print(str.index("o",3))         # find index of specified Char after 3rd index
print(str.swapcase())           # capital char will be small and small will be capital char
print(str.title())              # first char of word will be capital in all word in str
print("Sagar2156".isalnum())    # Is str have char or number in digit - result - True
print("2156".isalnum())         # Is str have char or number in digit - result - True
print("Sagar".isalnum())        # Is str have char or number in digit - result - True

print("Sagar".isalpha())        # Is str have char only - result - True
print("Sagar21".isalpha())      # Is str have char only result - False
print("Sagar S".isalpha())      # Is str have char only result - False for space entered in str

print("Sagar2143".isnumeric())  # Is str have digits only - result - False
print("2143".isnumeric())       # Is str have digit only result - True
print("2143.52".isnumeric())    # Is str have digit only result - False for . entered in str

print(" ".isspace())            # Is str have space only result - True
print(" S S".isspace())         # Is str have space only result - False

print(str.replace("Python","java"))









