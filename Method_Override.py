class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        print("Show from B")

class C(B):
    def show(self):
        print("Show from B")


c1 = C()
c1.show()
