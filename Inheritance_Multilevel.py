'''
Multi level Inheritance: Parent class child class are inherited into the new child class its called Multi level Inheritance.

Grand Father -> Father -> Son
'''

class A:

    def getA(self,a):
        self.a = a
    def putA(self):
        print("A :",self.a)

class B(A):
    def getB(self,b):
        self.b = b
    def putB(self):
        print("B :",self.b)


class C(B):
    def getC(self,c):
        self.c = c
    def putC(self):
        print("C :",self.c)


c1 = C()
c1.getA(20)
c1.putA()
c1.getB(10)
c1.putB()
c1.getC(30)
c1.putC()
