# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:35:02 2023

@author: sai
"""
import pandas as pd
df=pd.read_csv("C:/2-dataset/Seeds_data.csv")
df

#equal
df2=df.query("length=='5.554'")
print(df2)

#not equal
df2=df.query("length!='5.554'")
print(df2)

#checking percentage
df2=df.assign(Discountprecentage=lambda x:x.length*x.Area/100)
print(df2)



#print no. of rows
rows=df.shape[0]
rows
#print no. of column
col=df.shape[1]
col


#create new column
x=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,434,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210]
df2=df.assign(tutor=x)
df2

#add new column to existing dataframe
df["new"]=x
print(df)

#insert at particular position
df.insert(0, "comp",x)
print(df)

#get first 55 rows of given dataframe
df.iloc[:55]

#print two column
df[["Area","length"]]


#select specified column and rows.select score and qualify column and 2 rows
df.iloc[[55,45,33,12,4],[3,4]]



#print value of Area which is less than 2
df[df["Area"]>2]

#printing null value
print("rows where score is missing")
df[df["length"].isnull()]



#print the length which is between 5 and 44
print("length between 5 and 44")
df[df["length"].between(5,44)]




#select length less than 5 and width greater than 1
df[(df["length"]<5) & (df["Width"]>1)]


#print area column sum
print("sum of Area column is ")
df["Area"].sum()


#calculate mean of length 
df["length"].mean()




#append a new row k to dataframe with given value for each column
df.loc["k"]=[23,1233,45,255,22,34,78,123]
df



#sort dataframe first by name in descending order and then by score in ascendind order
df=df.sort_values(by=["length","Area"],ascending=[False,True])#here by is used for column name
df



#iterate over rows in dataframe
for index,row in df.iterrows(): #here iterrows is method for iteration
    print(row["length"],row["Area"])







