'''
Polymorphism : Polymorphism means One name multiple forms.
    -> Function having same name used for different data type and number of arguments in function.

Two Types :-
1. Compile time Polymorphism (Method Over loading) :-
        When there is a more than one method(Function) in a single class having the same name but
        different number of arguments and data type that is called Method over loading.
    shortly, function name have same with diff arguments.

2. Run time Polymorphism (Method Overriding) :-
        When there is a same method(Function) prototype in your both bash class and derived(child) class and if you call
        that method using the object of derived class then only derived class method will be called. So you can say that
        method of derived class override the Method of bash class.
'''

#EXAMPLE OF METHOD OVERRIDING

class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        super().show()
        print("Show from B")

class C(B):
    def show(self):
        super().show()
        print("Show from C")


c1 = C()
c1.show()
