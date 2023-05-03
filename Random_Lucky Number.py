''' Random Number findout from Parameters start to end

choice will findout number from given List   '''



import random

#print(random.randint(1,101))

#print(random.choice([1,11,21,51,101]))


l = []
lucky = []


for i in range(1,101):
    l.append(i)
print('Total List are ',l)


for i in range(10):
    num = random.choice(l)
    lucky.append(num)
    l.remove(num)

print('Total List without Lucky Numbers ',l,"\n")
print('Lucky Numbers are ',lucky)

