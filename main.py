#import libraries
import numpy as np
import pandas as pd

#creating a series
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

#creating a data frame
df1 = pd.DataFrame({"A":1.0, 
                    "B":pd.Timestamp("20130102"),
                    "C":pd.Series(1,index = list(range(4)),dtype="float32"),
                    "D":np.array([3]*4, dtype="int32"),
                    "E":pd.Categorical(["test","train","test","train"]),
                    "F":"foo",})
print(df1) #shows whole table
print(df1.dtypes) #shows the types of each column
print(df1.head(2)) #shows top 2 rows
print(df1.tail(3)) #shows bottom 3 rows
print(df1.describe()) #shows stats of data