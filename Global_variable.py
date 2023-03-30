'''
Global Variable :- In Python, Variable declared for global scope is called global Variable.
-- We can use global variable both inside and outside the function.
-- the scope of variable is broad, means accessible in all functions of the same module.
'''

global x            # Value of x is not changed in whole program untill we have changed it in global
x = 10

def test1():
    global y
    y = 20
    print("X :", x, "Y : ",y )          # this will print value of y=20 bcoz of value assigned as 20
    y = y+20                            # this will incerement value as y=40 and same will be continued in program
def test2():
    print("X :", x, "Y : ",y )
    
def test3():
    print("X :", x, "Y : ",y )


test1()
test2()
test3()
