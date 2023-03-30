'''
Exception :- An exception is an abnormal condition that accures during the run time of a program.

-- An Exception is an event which occurs during the execution of a program that disrupts the normal flow of the program.
-- An exception is a Python object that represents an error.
'''

print("*"*80)

try:
    a =int(input("Enter Value of A : "))
    b = int(input("Enter Value of B : "))

    c = a/b
    print("Division :-",c)

    l = [1,2,3,4,5,6,7,8]
    index = int(input("Enter Index Number :- "))
    print(l[index])

except Exception as error:
    print("Exception Occured : ",error)


'''    
except ZeroDivisionError as error:
    print("Exception Occured : ",error)

except ValueError as error:
    print("Exception Occured : ",error)

except IndexError as error:
    print("Exception Occured : ",error)
'''

print("*"*80)

