'''
Inheritance: Creating a new class from an Existing Class is callesd Inheritance.

-> The Object of one class acquire the property of Object of another class is called Inheritance.

Simplly, Inheriting the property of the base class to the child class is called ...

'''

class A:

    def getA(self,a):
        self.a = a
    def putA(self):
        print("Show from Class : A")

class B(A):
    def getB(self,b):
        self.b = b
    def putB(self):
        print("Show from Class : B")


b1 = B()
b1.getA(20)
b1.putA()
b1.getB(10)
b1.putB()

