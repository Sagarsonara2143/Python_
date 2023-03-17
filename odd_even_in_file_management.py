import random

f = open("data.txt","w")
for i in range(10):
    num = random.randint(1,20)
    f.write(str(num)+",")
f.close()

f = open("data.txt","r")
odd = open("odd.txt","w")
even = open("even.txt","w")
prime=open("prime.txt","w")
l=f.read().split(",")[:-1]
print(l)

for i in l:
    if int(i) % 2 == 0:
        even.write(i+",")
    else:
        odd.write(i+",")
        
f.close()
odd.close()
even.close()
prime.close()


odd = open("odd.txt","r")
prime=open("prime.txt","w")
o=odd.read().split(",")[:-1]
print(o)


for i in o:
    print(int(i))

'''
for i in int(o):
    if int(i) % o == 0:
        print("Prime")
        prime.write(i)
'''    

odd.close()
prime.close()




'''
f = open("data.txt","r")
odd = open("odd.txt","r")
even = open("even.txt","r")
prime=open("prime.txt","w")
l=f.read().split(",")[:-1]
print(l)

for i in l:
    for j in range (2,int(i)):
        if int(j) % int(i) == 0:
            prime.write(i + ",")

print("Odd Numbers are : ",odd.read())
print("Even Numbers are : ",even.read())
#print("Prime Numbers are : ",prime.read())
f.close()
odd.close()
even.close()
prime.close()
'''
