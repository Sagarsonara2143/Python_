from tkinter import *

root = Tk()                # it will open blank page
root.geometry("500x500")    # it will open page in size of 500 X 500
root.title("My First Tkinter Example")



#Create a Label and place in root

l_id = Label(root,text="ID",font=("Arial",15))
l_id.place(x = 50, y=50)

l_fname = Label(root,text="Fname",font=("Arial",15))
l_fname.place(x = 50, y=100)

l_lname = Label(root,text="Lname",font=("Arial",15))
l_lname.place(x = 50, y=150)

l_email = Label(root,text="Email",font=("Arial",15))
l_email.place(x = 50, y=200)

l_mobile = Label(root,text="Mobile",font=("Arial",15))
l_mobile.place(x = 50, y=250)
