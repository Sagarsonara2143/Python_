#for i in range(1,10):          #Simple \ * pattern
#  print("*"*i)

#for i in range(1,10):          #Simple / * pattern
#    print("*"*(10-i))

'''
for i in range(1,10):           #Triangel pattern
    print(" "*(10-i),"* "*i)

for i in range(1,10):           # Reverse Triangel pattern
    print(" "*i," *"*(10-i))
'''

'''
for i in range(1,10):
    print(" " * (10-i), "* " * i)
for i in range (1,10):
    print(" " * i, " *" * (10-i))
'''


#\/
#/\
for i in range(1,10):
    print("*"*i,"  " *(10-i)*2,"*"*i)

for i in range(1,10):
    print("*"*(10-i),"  "*(i*2),"*"*(10-i))
