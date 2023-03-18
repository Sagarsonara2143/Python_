''' Default Arguements : If Value assigned for any arguments in creation time
                        then it is optinally to enter parameter at calling time.
if not put argument at calling time then its taken from default arguments.

Defaut Arguments order will be Right to left means last to first order.
'''

def test(a=20,b=30,c=40,d=50):
    print("A : ",a," B : ",b," C : ",c," D : ",d)

test(10,20,30,40)   # print parameters values
test(10,20,30)      # Value of D is taken from default arguments

test(10,20)
test(10)
test()

test(30,40)         # a and b arguments taken and c and d takes default arguments

test(b=60,d=70)     # a and c value taken from default arguments

