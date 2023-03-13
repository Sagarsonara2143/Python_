# String is a Group of Characteristics

s = "Python programing2"

"""
for i in s:
    print(i)
"""

print(s.capitalize())       #First Character only Capitalize
print(s.casefold())         #All Character in Lowercase
print(s.lower())            #All Character in Lowercase
print(s.upper())            #All Character in Uppercase
print(s.center(40,"*"))     #Str print in Center aling 40 (Left - Right Space will filed with *)
print(s.count("P"))         # Its count How many P availabel in String
print(s.count("P",3))       # Its count How many P availabel after 3rd index
print(s.endswith("ng"))     # Its showing True or False
print(s.startswith("p"))    # Its showing True or False #Str are Case sensitive
print(s.find("n",6))        # result - Find out n with start of 6th Index and result will be in Index
print(s.index("o"))         # reslut - Index number disply for r
print(s.swapcase())         # result - Capital character will be small and small will be capital
print(s.title())            # first character of word will be capital
print("Sagar123".isalnum()) # Alphabetical or Number will be cheked and result in Boolean
print("Sagar 123".isalnum())#Space is counted in character and result will be False
print("Sagar".isalpha())    # Alphabetical checked and result in boolean
print("26413".isnumeric())  # Numbers is checked and result in boolean
print(" ".isspace())        
