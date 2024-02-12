# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:11:32 2023

@author: sai
"""


#create one series or create and display 1D array like containing array of data
import pandas as pd
x=pd.Series([2,3,4,5])
print(x)


#convert pandas module series to python list and its type
import pandas as pd
x=pd.Series([2,3,4,5])
print("pandas series and type")
print(x)
print(type(x))
print("convert series in list")
print(x.tolist())
print(type(x.tolist()))

#add,substract,multiply and divide two series
import pandas as pd
x=pd.Series([66,88,150,132])
y=pd.Series([33,44,55,66])
print(x)
print(y)

print("addition is")
a=x+y
print(a)
print("substraction is")
b=x-y
print(b)
print("multi is")
c=x*y
print(c)
print("division is")
d=x/y
print(d)


#compare two series
import pandas as pd
x=pd.Series([33,88,150,132])
y=pd.Series([33,44,55,66])
print("1st series is")
print(x)
print("2nd series is")
print(y)
print("compare series")
print("equal")
print(x==y)
print("greater than")
print(x>y)
print("less than")
print(x<y)


#convert dictionary to pandas series
x={"fee":[12,23,34,45],"duration":["a","b","c","d"]}
print("original dictionary")
print(x)
print("new dictionary")
y=pd.Series(x)
print(y)


#convert numpy array into pandas
import numpy as np
import pandas as pd
x=np.array([1,2,3,4])
print("numpy array")
print(x)
new_series=pd.Series(x)
print("converted pandas series")
print(new_series)



#change data type of given series or column
import pandas as pd
s1=pd.Series(["hi","hello","good","bad",66])
print(s1)
print("change datatype to numeric")
s2=pd.to_numeric(s1,errors="coerce")
print(s2)

#convert 1st column of dataframe into series!!!!!!!!!!!!!!imp!!!!!!!!!!!!!
import pandas as pd
s={"col1":[12,11,23,44],"col2":[11,22,33,44],"col3":["a","b","c","d"]}
df=pd.DataFrame(data=s)
print("original dataframe")
print(df)
s1=df.iloc[:,0]#iloc used for index and location of column
print("1st column of series is")
print(s1)

#reset index of series, convert it into stack
import pandas as pd
s=pd.Series([["red","green"],["black","white"],["purple"]])
print("original series is",s)
x=s.apply(pd.Series).stack().reset_index(drop=True)
print("one series")
print(x)

#or

#reset index of series, convert it into stack
import pandas as pd
s=pd.Series([["red","green"],["black","white"],["purple"]])
print("original series is",s)
s1=s.apply(pd.Series())
s2=s1.stack()
s3=s2.reset_index(drop=True)
print("one series")
print(s1)
print(s2)
print(s3)

#add data to existing series
import pandas as pd
s=pd.Series([11,22,33,44])
print("original series")
print(s)
print("series after adding some data")
new_s=pd.concat([s,pd.Series([12,34,56,78,"php"])],ignore_index=True)
print(new_s)


#sort given series
import pandas as pd
s=pd.Series([1,33,2])
print(s)
print("sorted series is")
x=pd.Series(s).sort_values()
print(x)

#change order of given series
import pandas as pd
s=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print("original series is",s)
print("new sorting series is")
x=s.reindex(index=["b","a","c","d","e"])
print(x)



