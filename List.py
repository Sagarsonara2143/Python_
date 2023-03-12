'''
List :- List is a group of Mix type of data
Stored a Multiple items in a Single Variable
List are Changable, and allowed duplicates value
'''

l = [1,2,"Python",True,1.1,"Java",123]

print(l)
l.append(20)        # Add Value in last / at a time single value can add
print(l)
#l.clear()          # Clear the List

l1 = l.copy()       # Copy whole list to new object
print(l)
print(l1)

l1.append(30)       # only add in l1 list
print(l)
print(l1)

l2 = l              # Assign all list value to new object
l.append(21)
print(l)
print(l2)

l2.append(22)
print(l)
print(l2)


print(l.count(1))   # Result is 2 - True will be count as 1

l.extend([40,False])# insert value in last - multiple value can be add at a time
print(l)
print(l2)

print(l.index(1.1)) # find out index of 1.1 in list


l.insert(5,50)      # Add value in particluar index in list
print(l)

l.pop()             # Delete last value in list
print(l)

l.remove(50)        # Remove particular value from list
print(l)

l.reverse()         # Reverse full list
print(l)


l.remove("Python")
l.remove("Java")
l.remove(True)
print(l)

l.sort()            # Sort Numeric Value
print(l)

l.clear()
l.append("python")
l.append("Java")
print(l)

l.sort()            # Sort Word by alpabetically
print(l)







