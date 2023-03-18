'''
    >>> Function is a set of instructions.
    >>> Function is a block of code which only runs when its called.
    >>> Function is return with result.
'''

# Function with no arguments and no return value

def printLine():
    print("*"*40)

printLine()
print("Demo of User defined Function")
printLine()

# Function with argument and no return value

def add(a,b):
    print("Addition of Two Numbers are : ",a+b)

n1 = int(input("Enter First Value : "))
n2 = int(input("Enter Second Value : "))
add(n1,n2)
printLine()

# Function with arguments and return value

def sub(a,b):
    return a-b
n1 = int(input("Enter First Value : "))
n2 = int(input("Enter Second Value : "))
ans = sub(n1,n2)
print("Subtraction of two Numbers is : ", ans)
printLine()
