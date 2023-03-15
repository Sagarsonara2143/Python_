f = open("Example1.txt","w")
f.write("First Example of File Management in Python")
f.close()
print("************************************************************")

f = open("Example1.txt","r")
print(f.read())
f.close()
print("************************************************************")

f = open("Example1.txt","a")
f.write("\nThis is appended text")
f.close()
print("************************************************************")

f = open("Example1.txt","r")
print("Cursor is on index number ",f.tell())
print(f.read())
print("Cursor is on index number ",f.tell())
f.close()
print("************************************************************")

f = open("Example2.txt","w+")
f.write("Second Example of File Management in Python")
print(f.read())     # output is only space bcoz cursor on last index
print("************************************************************")
f.seek(0)           # Set cursor index is o to read file from start
print(f.read())     # Full content will be read
f.close()
print("************************************************************")




f = open("Example2.txt","r+")
#f.write("First Example of File Management in Python")
print(f.read())     # output is full content bcoz cursor on 1st index by default
print("************************************************************")
f.write("\nAppended text with write fun using r+ method")
f.seek(0)
print(f.read())
f.close()
print("************************************************************")


f = open("Example2.txt","a+")
f.write("\nSecond Example of File Management in Python is appended using a+")
f.seek(0)
print(f.read())     # output is full content bcoz cursor on 1st index by default
print("************************************************************")
print(f.read())
f.close()
print("************************************************************")






