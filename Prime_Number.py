#n = int(input("Enter Value : "))

'''
for i in range(3,int(n/2)+1):
    if n % i == 0:
        print(n, " is not Prime Number")
        break
    #else:
     #   print(n, " is Prime Number")
else:
    print(n," is prime Number")

'''



n = int(input("Enter Staring Number : "))
n1 = int(input("Enter Last Serial Number : "))
s = input("Enter Odd for Odd Value or Even for Even Value : ")


for i in range(n,int(n1+1)):
    if s == "Odd":
        if i % 2 != 0:
            print(i)
    elif s == "Even":
        if i % 2 == 0:
            print(i)
    else:
        print("Invalid Output")
        break
    
