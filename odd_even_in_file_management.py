import random

f = open("data.txt","w")
for i in range(10):
    num = random.randint(1,1000)
    f.write(str(num)+",")
f.close()

f = open("data.txt","r")
odd = open("odd.txt","w")
even = open("even.txt","w")
prime=open("prime.txt","w")
l=f.read().split(",")[:-1]
#print(l)

for i in l:
    if int(i) % 2 == 0:
        even.write(i+",")
    else:
        odd.write(i+",")
        for j in range(3,int(int(i)/2)+1,2):
            if int(i) % j == 0:
                break
        else:
            prime.write(i + ",")
        
f.close()
odd.close()
even.close()
prime.close()


f = open("data.txt","r")
odd = open("odd.txt","r")
even = open("even.txt","r")
prime=open("prime.txt","r")

print("Data are : \t",f.read())
print("Even Numbers are : ",even.read())
print("Odd Numbers are : ",odd.read())
print("Prime Numbers are :",prime.read())
f.close()
odd.close()
even.close()
prime.close()
