
str = input("Enter String : ")

'''
wd = 1
ch = 0
num = 0
sp = 0
other = 0

for i in str:
    if i.isalpha():
        ch = ch + 1
    elif i.isnumeric():
        num = num + 1
    elif i.isspace():
        sp = sp + 1
        wd = wd + 1
    else:
        other = other + 1
    
print("Total Word are : ", wd)
print("Total Alphabetics are : ", ch)
print("Total Digits are : ", num)
print("Total Space are : ", f sp)
print("Total Special symbols are : ", other)

'''

print("Total length of string is ",len(str))

num = sum(i.isnumeric() for i in str)
ch = sum(i.isalpha() for i in str)
sp = sum(i.isspace() for i in str)
wd = sp + 1
other = len(str) - num - ch - sp


print("Total Word are : ", wd)
print("Total Alphabetics are : ", ch)
print("Total Digits are : ", num)
print("Total Space are : ", sp)
print("Total Special symbols are : ", other)
