# Write a Python program to get the Fibonacci series of given range.

n = int(input("Enter End Value : "))

x = 0
y = 1

if n == 0:
    print(n)
elif n < 0:
    print("Invalid Input")
else:
    print(x)

while y < n:
    print(y)
    x,y = y,x+y
 

'''
n1 = int(input("Enter Start from Value series : "))
n2 = int(input("Enter End Value : "))
x = 0

while n1 < n2:
    print(n1)
    x,n1 = n1,x+n1

'''
