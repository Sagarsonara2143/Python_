'''
Hybrid Inheritance: Inheritance consisting multiple types of inheritance is called Hybrid Inheritance.

Example-. Grand Father have a son(Father) and Father have another three son(Child)

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

class D(B,C):
    def getD(self,d):
        self.d = d
    def putD(self):
        print("D :",self.d)

d1 = D()
d1.getA(50)
d1.putA()
d1.getB(100)
d1.putB()
d1.getC(150)
d1.putC()
d1.getD(200)
d1.putD()
