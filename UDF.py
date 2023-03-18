def oddEven(n):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is Odd")


def maxOfTwo(x,y):
    if x > y:
        print(x,"is Greter Number")
    else:
        print(y,"is Greter Number")


def maxOfThree(x,y,z):
    if x > y:
        if x > z:
            print(x,"is Greter Number")
        else:
            print(z,"is Greter Number")
    elif y > z:
        print(y,"is Greter Number")
    else:
        print(z,"is Greter Number")


def primeNum(n):
    if n % 2 != 0:
        for i in range(3,int(n/2)+1,3):
            if n % i == 0:
                print(n, "is not prime Number")
                break
        else:
            print(n,"is Prime Number")
    else:
        print(n, "is not Prime Number")


def fibo(n):
    a,b=0,1
    while b<n:
        print(b,end =" ")
        a,b=b,a+b
print()    
