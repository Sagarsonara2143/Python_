sname = input("Please Enter Student Name : ")
rno = int(input("Please Enter Roll No. : "))
s1 = int(input("Enter Subject 1 Marks : "))
s2 = int(input("Enter Subject 2 Marks : "))
s3 = int(input("Enter Subject 3 Marks : "))

total = s1+s2+s3
Per = total/3


print("Student Name is ", sname)
print("Student Roll Number is ", rno)
print("Total Marks is ", total)
print("Percentage is ", Per)

if Per >= 70:
    print("Distinction")
elif Per >= 60:
    print("First Class")
elif Per >= 50:
    print("Second class")
elif Per >= 40:
    print("Pass Class")
else:
    print("Fail")
