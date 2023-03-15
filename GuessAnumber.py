import random

r = random.randint(1,20)

while True:
    n = int(input("Enter Value between 1 to 20 :"))
    if n == r:
        print("Congratulate..! You Guessed Number is Correct")
        break
    elif r > n:
        print("Guessed Number is Smaller Number")
    elif r < n:
        print("Guessed Number is Greter Number")
