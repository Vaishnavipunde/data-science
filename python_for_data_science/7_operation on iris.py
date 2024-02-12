# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:05:06 2023

@author: sai
"""

import pandas as pd
df=pd.read_csv("C:/2-dataset/iris.csv")
df


df.shape
df.size
df.columns
df.columns.values
df.index
df.dtypes
df.info


df["sepal_length"]
df[["petal_length","sepal_width"]]


#select certain row and assign to another
df2=df[2:]
df
#accessing certain cell from column duration
df["sepal_width"][2]


x=df["sepal_width"]-1
x

#describe dataframe for all columns
df.describe()


df2=df.rename(columns={"sepal_width":"c1","petal_width":"c2"})
df2


df1=df.drop(df.index[1])
df1


df1=df.drop(df.index[2:])
df1

df2=df.drop(["sepal_width"],axis=1)
df2



df2=df.iloc[:,:2]#here column print upto 1 index and all rows
df2

df2=df.iloc[0:2,:]#all column and 2 rows
df2


df2=df.iloc[1:5]
df2

df2=df.iloc[::2]#select alternate rows
df2


#select column by range
df2=df.loc[:,"petal_width":]
df2

df2=df.assign(Discountprecentage=lambda x:x.sepal_width*x.sepal_length/100)
print(df2)


rows=df.shape[0]
rows


col=df.shape[1]
col


#select specified column and rows.select petal width and sepal length column and 2 rows
df.loc[["1","3"],["petal_width","sepal_length"]]


print("number of sepal greater than 2")
df[df["sepal_length"]>2]



print("rows where sepal is missing")
df[df["sepal_length"].isnull()]


print("sepal length bet 2.2 and 5.0 is")
df[df["sepal_length"].between(2.2,5.0)]



#select rows where no of attempts in exam is less than 2 and score greater than 15
df[(df["sepal_width"]<2) & (df["sepal_length"]>1)]


#change sepal length in row 4 to 11.5
df.loc[4,"sepal_width"]=11.5
df


#calculate sum of petal width
print("sum of petal width is ")
df["petal_width"].sum()


#calculate mean of all sepal length
df["sepal_length"].mean()


df.loc["k"]=[2,1233,45,4,"flower"]
df


#iterate over rows in dataframe
for index,row in df.iterrows(): #here iterrows is method for iteration
    print(row["sepal_length"],row["sepal_width"])







import numpy as np
x=df["sepal_length"].apply(np.square)
x


x=df["sepal_length"].transform(np.square)
x

df2=df.groupby(['petal_length']).sum()
df2


df2=df["sepal_length"].map(lambda x:x/2)
df2

df2=df.sample(frac=1) #for 100%suffling we use frac=1.
df2


df2=df.sample(frac=1).reset_index()
df2



#drop suffle index
df1=df.drop([0])
df1





