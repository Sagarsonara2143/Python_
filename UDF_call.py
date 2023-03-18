import UDF

while True:
    print("*"*40)
    print("1. OddEven")
    print("2. Max of Two Numbers")
    print("3. Max of Three Numbers")
    print("4. Prime Number")
    print("5. Fibonacci Series")
    print("6. Exit")
    print("*"*40)
    select = int(input("Select your choice : "))

    if select == 1:
        n = int(input("Enter Value : "))
        UDF.oddEven(n)
        print("*"*40)
    elif select == 2:
        n1 = int(input("Enter Value : "))
        n2 = int(input("Enter Value : "))
        UDF.maxOfTwo(n1,n2)
        print("*"*40)
    elif select == 3:
        n1 = int(input("Enter Value : "))
        n2 = int(input("Enter Value : "))
        n3 = int(input("Enter Value : "))
        UDF.maxOfThree(n1,n2,n3)
        print("*"*40)
    elif select == 4:
        n = int(input("Enter Number to check Prime or Not : "))
        UDF.primeNum(n)
        print("*"*40)
    elif select == 5:
        n = int(input("Enter range for Fibonacci series : "))
        UDF.fibo(n)
        print()
        #print("*"*40)
    elif select == 6:
        print("Bye.. Bye..!!")
        break
