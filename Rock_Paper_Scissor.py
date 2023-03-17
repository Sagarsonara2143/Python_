import random

l = ["Rock","Paper","Scissor"]
Computer = random.choice(l)

user = input("Choice : Rock, Paper, Scissor  : ")

if user == Computer:
    print("Draw..!!!")
elif user == "Rock" and Computer == "Scissor":
    print("Computer Wins..!")
elif user == "Paper" and Computer == "Scissor":
    print("Computer Wins..!")
elif user == "Scissor" and Computer == "Rock":
    print("Computer Wins..!")
elif user == "Paper" and Computer == "Rock":
    print("User Wins..!")
elif user == "Scissor" and Computer == "Paper":
    print("User Wins..!")
elif user == "Scissor" and Computer == "Rock":
    print("User Wins..!")




