import pandas as pd

'''
data={
    'student':['sagar','sanjay','Ansh'],
    'Marks':[95,97,88],
    'Grade':["A+","A+","A"]
    }

var=pd.DataFrame(data)              # Data Display in Table like row and column
print(var)                                      # Key Value is Display in First Row
'''

'''
a=[1,7,5]                                       
print(pd.Series(a))                     # Series will display data in column
print(pd.Series(a)[2])                  # Result of second index column - Ans 5 
'''

'''
a=[10,15,20]
var=pd.Series(a,index=["a","b","c"])        # Index is with arguments display labels in index - By default value of index is start from 0
print(var)      
print("Value of B Index : ",var["b"])       # We can find out data with index value
'''

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)