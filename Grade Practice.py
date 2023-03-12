sname = input("Enter Student Name : ")
rno = int(input("Enter Roll No. : "))
s1 = int(input("Enter Marks of Subject 1 : "))
s2 = int(input("Enter Marks of Subject 2 : "))
s3 = int(input("Enter Marks of Subject 3 : "))

total = s1 + s2 + s3
per = total/3

print("Student Name is ", sname)
print("Student Roll Number is ", rno)
print("Marks of Subject 1 is ", s1)
print("Marks of Subject 2 is ", s2)
print("Marks of Subject 3 is ", s3)
print("Total Marks : ", total)
print("Percentage ", per)

if per>=70:
    print("Grade : Distinction")
elif per>=60:
    print("Grade : First Class")
elif per>=50:
    print("Grade : Second Class")
elif per>=40:
    print("Grade : First Class")
else:
    print("Fail")
