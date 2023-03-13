'''   Tuple - Not Changable, will allowed duplicates value  '''

t = (1,2,"Python",True,[1,11,21,51,101],3.5,"Java",1)

print(t)
print(t.count(2))
print(t.index(3.5))

for i in t:
    print(i)


t[4].append(151)        # List can be append in a tuple
print(t)

