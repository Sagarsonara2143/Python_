import datetime
from datetime import date

'''
n = int(input("Enter N Number : "))
list = [0, 1]
[list.append(sum(list[-2:])) for x in range(n)]
print(list[:n])
'''
'''
today=datetime.date.today()
yesterday=today - datetime.timedelta(days=1)
tommorow=today + datetime.timedelta(days=1)


print("Yesterday : ",yesterday.strftime("%d-%m-%Y"))
print("Today : ",today.strftime("%d-%m-%Y"))
print("Tommorow : ",tommorow.strftime("%d-%m-%Y"))
'''

#   x,y=10,20
#   x,y=y,x
#   print("After Swap  X is ",x,"and Y is ",y )

f=open("interview.txt","w")
f.write("This is a demo of File management in Python")
f.close()

f=open("interview.txt","r")
print(f.read())
f.close()
print("*"*80)

f=open("interview.txt","a")
f.write("\nThis is Appended Text")
f.close()

f=open("interview.txt","r+")
print(f.read())
f.write("\nThis is r+ text")
f.close()
print("*"*80)

f=open("interview.txt","r")
print(f.read())
f.close()
print("*"*80)

f=open("interview.txt","w+")
f.tell()
f.write("\n This is w+ Text")
f.seek(0)
print(f.read())
f.close()
