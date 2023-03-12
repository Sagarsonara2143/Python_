
n1 = int(input("Enter Starting Value : "))
n2 = int(input("Enter Last Value : "))

print(" The Prime Numbers in range are ")

"""
for number in range (n1, n2+1):
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                break
        else:
            print(number)
    

"""

for num in range(n1,n2+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
