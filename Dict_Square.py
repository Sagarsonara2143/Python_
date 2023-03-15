dict = {}

n = int(input("Enter Last value for dictionary : "))
for i in range(1,n+1):
    dict[i] = i*i

    print(dict)

for i in dict:
    print(i,":",dict[i])
