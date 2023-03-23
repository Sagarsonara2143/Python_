'''
Hierarchical Inheritance: When more then one child class are created from one bash(parent) class is called Hierarchical Inheritance.

Example-. Father Having Three Sons
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


class C(A):
    def getC(self,c):
        self.c = c
    def putC(self):
        print("C :",self.c)

class D(A):
    def getD(self,d):
        self.d = d
    def putD(self):
        print("D :",self.d)

b1 = B()
c1 = C()
d1 = D()
b1.getA(50)
b1.putA()
b1.getB(100)
b1.putB()
c1.getC(150)
c1.putC()
d1.getD(200)
d1.putD()
