'''
Multiple Inheritance: When a class can be derived from more than one bash(parent) class is called Multiple Inheritance.

Father -> Son
Mother -> Son
'''

class A:

    def getA(self,a):
        self.a = a
    def putA(self):
        print("A :",self.a)

class B():
    def getB(self,b):
        self.b = b
    def putB(self):
        print("B :",self.b)


class C(A,B):
    def getC(self,c):
        self.c = c
    def putC(self):
        print("C :",self.c)


c1 = C()
c1.getA(50)
c1.putA()
c1.getB(100)
c1.putB()
c1.getC(150)
c1.putC()
