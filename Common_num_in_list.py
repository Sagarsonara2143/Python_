# Write a Python function that takes two lists and returns true if they have at least one common member.

def common_num(list1,list2):
    common_list = []
    for i in list1:
        for j in list2:
            if i == j:
                common_list.append(i)
    print("Common Number in both List : ",common_list)
    return ""


l1 = []
l2 = []

n = int(input("Enter Length of List 1 : "))
for i in range(n):
    data = int(input("Enter Data for List 1 : "))
    l1.append(data)


m = int(input("Enter Length of List 2 : "))
for j in range(m):
    data = int(input("Enter Data for List 2 : "))
    l2.append(data)

print("*"*50)
print("List 1 : ",l1)
print("List 2 : ",l2)
print(common_num(l1,l2))
print("*"*50)
