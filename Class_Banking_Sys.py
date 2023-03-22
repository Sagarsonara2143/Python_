class Bank():

    def openAc(self,cname,cno,balance):
        self.cname = cname
        self.cno = cno
        self.balance = balance

        print("Hello",cname,"..! Your account is opened with account Number is",cno,"and Balance is",balance,"Rs.")

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            self.needs = amount - self.balance
            print("Sorry.! You need another",self.needs,"to proceed withdraw")

    def checkBalance(self):
        print("Current Balance is : ",self.balance)


b1 = Bank()
cname = input("Enter Customer Name : ")
cno = int(input("Enter Account Number : "))
balance = int(input("Enter Initial Balance : "))

b1.openAc(cname,cno,balance)


while True:
    print("*"*80)
    print("1. Deposit")
    print("2. Check Balance")
    print("3. Withdraw")
    print("4. Exit")
    print("*"*80)
    
    select = int(input("Select Service : "))

    if select == 1:
        amount = int(input("Enter Amount to deposit : "))
        b1.deposit(amount)

    elif select == 2:
        b1.checkBalance()

    elif select == 3:
        amount = int(input("Enter Amount to withdraw : "))
        b1.withdraw(amount)
    
    elif select == 4:
        print("Thank You for using our services..!")
        break



