'''  LIST SLICING  '''
# Start : End : Jump                End Index not count in List


#    0  1    2      3   4    5    6       7    8     9     10  11  12   13 14 15    +
l = [10,20,"Tops",20.5,True,150,"Python",300,"Java",False,85.5,100,True,11,22,330]
#    16 15    14    13   12  11    10     9    8      7   6    5   4    3  2   1    -


print(len(l))
print(l)
'''
print(l[5:15:4])        # Start with 5th Index to 15th Index and jump is 4

print(l[:3:3])          # Start with 0 index to 3rd Index - Jump is 3

print(l[::5])           # Start with 0 index to end - Jump is 5

print(l[10::5])         # Start with 10th index to End - Jump is 5

print(l[1:20])          # Start with 1st index to 20th Index - If 20 items not availabel in List then print till end list
'''


print(l[-16::5])        # Start with -16 index to end - Jump is 5

print(l[:-1])           # Start with -16 index to -1 index

print(l[::-5])#Reverse    # Start with 1st index(330) to last index(10) with jump of 5

print(l[-12:-3:10])     # start with -12 index to -3 index with jump of 10

print(l[-16::15])      # Start with -17 index, if not short list then -17th then start with last index(0 index in positive index)

print(l[-16::-5])       # Result is [10] only b'coz -16th index only print



