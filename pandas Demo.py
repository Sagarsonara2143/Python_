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
var
print(var)      
print("Value of B Index : ",var["b"])       # We can find out data with index value
'''

'''
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df.loc[0])
'''

var=pd.read_csv('1.csv')
print(var)
