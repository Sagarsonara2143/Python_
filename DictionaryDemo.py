'''
Dictionaries are used to store data values in key:value pairs.
Dict Changable and not allowed Duplicates Value.
'''

dict = {12:"Sagar",15:"Raj",20:"Sanjay",25:"Manish"}


print(dict)         #Dictionary Print in Curly bracket

#dict.clear()       # Clear Dict

d=dict.copy()       # Copy Dict to d
d1 = dict           # Assign whole key:values to d1
print(d)
print(d1)

print(dict.get(15)) # Value of Key 15
print(dict.items()) # Dictionary Values in list with keys
print(dict.keys())  # print only Dictionary Keys only 
print(dict.values())# print only Dictionary values only


dict.pop(20)        # it will remove keys and its value from dictionary
print(dict)

dict.popitem()      # it will remove last keys and its value
print(dict)

dict.update(d)      # it will add full dictionary of d in dict (Duplicates Keys not allowed)
print(dict)

dict[40]="Sunil"    # it will add in last of dict
print(dict)

for i in dict:
    print(i,":",dict[i])
