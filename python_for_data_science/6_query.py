# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:15:43 2023

@author: sai
"""

#query


import pandas as pd
import numpy as np
tech={"courses":["math","history","science","python","geography"],"fees":[1,2,3,4,5],"duration":["10","20","30","40","50"],"discount":[1.1,20.1,30.2,40.3,50.4]}
row_labels=["r0","r1","r2","r3","r4"]
df=pd.DataFrame(tech ,index=row_labels)
print(df)

#equal condition,select history
df2=df.query("courses=='history'")
print(df2)
#not equal condition,not select history 
df2=df.query("courses!='history'")
print(df2)






#add new column to dataframe.tutor column get add
tutors=['ram',"sham","geeta","seeta","aam"]
df2=df.assign(tutor=tutors)
print(df2)


#adding multiple column to dataframe.
x=["apple","baby","cat","dog","elephant"]
tutors=['ram',"sham","geeta","seeta","aam"]
df2=df.assign(y=x,t=tutors)
print(df2)







#derive new column from existing
df=pd.DataFrame(tech)
df2=df.assign(Discountprecentage=lambda x:x.fees*x.discount/100)
print(df2)

#add new column to existing dataframe
df=pd.DataFrame(tech)
df["new"]=x
print(df)

#add new column to particular position.here comp is column name which we want to create,0 is the position,tutors is the value
df.insert(0, "comp",tutors)
print(df)

'''
    comp tutors    courses  fees duration  discount       new
0    ram    ram       math     1       10       1.1     apple
1   sham   sham    history     2       20      20.1      baby
2  geeta  geeta    science     3       30      30.2       cat
3  seeta  seeta     python     4       40      40.3       dog
4    aam    aam  geography     5       50      50.4  elephant
'''


#find number of rows
rows=len(df.index)
rows
   #or
rows=len(df.axes[0])
rows
   #or
rows=df.shape[0]
rows



#find number of column
col=len(df.axes[1])
col
  #or
col=df.shape[1]
col



--------------assignment--------------------



#write pandas program to display dataframe and  create dictionary dataframe
import pandas as pd
apple={"x":["11","12","13","14","15"],"y":["21","22","23","24","25"],"z":["31","32","33","34","35"]}
df=pd.DataFrame(apple)
df


#display dataframe using label
import pandas as pd
apple={"name":["ram","sham","geeta","seeta"],"score":[11,np.nan,33,44],"attempts":[1,2,3,4],"qualify":["y","n","y","y"]}
labels=["a","b","c","d"]
df=pd.DataFrame(apple,index=labels)
df



#write pandas program to display summary of basic info about dataframe 
df.describe()
df.info()



#get first three rows of given dataframe

df.iloc[:3]


#select name and score column from given dataframe


df.loc[:,"name":"score"] 
   #or
df[["name","score"]]


#select specified column and rows.select score and qualify column and 2 rows
df.loc[["a","b"],["score","qualify"]]

#select the rows in which number of attempts in exam is greater than 2

import pandas as pd
apple={"name":["ram","sham","geeta","seeta"],"score":[11,np.nan,33,44],"attempts":[1,2,3,4],"qualify":["y","n","y","y"]}
labels=["a","b","c","d"]
df=pd.DataFrame(apple,index=labels)
df
print("number of attempts greater than 2")

df[df["attempts"]>2]
#or
df2=df.loc[df.attempts>2]
df2

#count no. of rows and column
import pandas as pd
apple={"name":["ram","sham","geeta","seeta"],"score":[11,np.nan,33,44],"attempts":[1,2,3,4],"qualify":["y","n","y","y"]}
labels=["a","b","c","d"]
df=pd.DataFrame(apple,index=labels)
df
r=df.shape[0]
print(r)
c=df.shape[1]
print(c)

print("no.of rows " +str(r)) #for type casting
print("no. of column " +str(c))# for type casting


#select the rows where the score is missing
import pandas as pd
apple={"name":["ram","sham","geeta","seeta"],"score":[11,np.nan,33,44],"attempts":[1,2,3,4],"qualify":["y","n","y","y"]}
labels=["a","b","c","d"]
df=pd.DataFrame(apple,index=labels)
df
print("rows where score is missing")
df[df["score"].isnull()]

'''
   name  score  attempts qualify
b  sham    NaN         2       n
'''


#select rows whose score is between 30 and 44
import pandas as pd
apple={"name":["ram","sham","geeta","seeta"],"score":[11,np.nan,33,44],"attempts":[1,2,3,4],"qualify":["y","n","y","y"]}
labels=["a","b","c","d"]
df=pd.DataFrame(apple,index=labels)
df
print("score bet 30 and 44 is")
df[df["score"].between(30,44)]



#select rows where no of attempts in exam is less than 2 and score greater than 15
df[(df["attempts"]<2) & (df["score"]>15)]


#change score in row d to 11.5
df.loc["d","score"]=11.5
df


#calculate sum of exam attempts by student
print("sum of examination attend by student is ")
df["attempts"].sum()



#calculate mean of all student score
df["score"].mean()




#append a new row k to dataframe with given value for each column
df.loc["k"]=["hi",1233,45,"y"]
df


#sort dataframe first by name in descending order and then by score in ascendind order
df=df.sort_values(by=["name","score"],ascending=[False,True])#here by is used for column name
df


#replace qualify column contain values yes and no with true and false
df["qualify"]=df["qualify"].map({"y":True,"n":False})
df


#change name ram to jems to name column of dataframe
df["name"]=df["name"].replace("ram","jems")
df



#insert new column to existing dataframe
colour=["red","blue","pink","yellow","green"]
df["colours"]=colour
df


#iterate over rows in dataframe
for index,row in df.iterrows(): #here iterrows is method for iteration
    print(row["name"],row["score"])





