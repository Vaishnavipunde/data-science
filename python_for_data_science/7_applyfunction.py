# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:18:05 2023

@author: sai
"""
#apply function on dataframe
import pandas as pd
import numpy as np
data={"a":[1,2,34],"b":[44,33,22],"c":[76,98,44]}
df=pd.DataFrame(data)
df

def add(x):
    return x+3
df2=df.apply(add)
df2


#using apply function on single column
df2=df["a"].apply(add)
df2

#apply on multiple column
df2=df[["a","b"]].apply(add)
df2

#using lambda fun on column
df2=df.apply(lambda x:x+6)
df2

#apply() on selected list of multiple column 
df=pd.DataFrame(data)
df2=df[["a","b"]].apply(lambda x:x+5)
df2







#instead apply () we use transform () also 
def add(x):
    return x-1
df2=df.transform(add)
df2


#map() on single column
df2=df["a"].map(lambda x:x/2)
df2


#using numpy function
import numpy as np
x=df["a"].apply(np.square)
x
  #or
df2=np.square(df['a'])
df2




#groupby() in pandas .used for duplicate entry
import pandas as pd
import numpy as np
tech={"courses":["math","science","history","science","python","geography"],"fees":[7,1,2,3,4,5],"duration":["10","90","20","30","40","50"],"discount":[1.1,20.1,55,30.2,40.3,50.4]}
row_labels=["r0","r1","r2","r3","r4","r5"]
df=pd.DataFrame(tech ,index=row_labels)
print(df)

df2=df.groupby(['courses']).sum()
df2

#groupby on multiple column
df2=df.groupby(["courses","fees"]).sum()
df2



#add index to group data 
df2=df.groupby(["courses","fees"]).sum().reset_index()
df2


#get column names from dataframe
df.columns
    #or
x=list(df)
x



#get the list of all column by header
column_header=list(df.columns.values)
column_header





#suffle rows
df2=df.sample(frac=1) #for 100%suffling we use frac=1.
df2

df2=df.sample(frac=0.5)#for 50%use frac=0.5
df2


#create new index starting from zero
df2=df.sample(frac=1).reset_index()
df2


#drop suffle index
df1=df.drop()







