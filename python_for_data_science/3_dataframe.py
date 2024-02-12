# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:39:21 2023

@author: sai
"""

#create using constructor
#create pandas dataframe using list!!!!!!!imp!!!!!!!!!
import pandas as pd
technologies=[["spark",2000,"30days"],["pandas",3000,"40days"]]
df=pd.DataFrame(technologies)
print(df)


#add row and column label
column_label=["courses","fee","duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_label,index=row_label)
print(df)

#printing type
df.dtypes

#dataframe using dictionary
import pandas as pd
technologies={"courses":["math","science"],"fee":[100,200],"duration":["30","40"]}
df=pd.DataFrame(technologies)
print(df)
print(df.dtypes)

#convert all datatypes to best possible types !!!!!!!!v.v.imp!!!!!!!!!
#convert object to string
df2=df.convert_dtypes()
print(df2.dtypes)

#change all columns to same type.#convert string into object
df=df.astype(str)
print(df.dtypes)

#change type for one or multiple columns
df=df.astype({"fee":int,"duration":float})
print(df.dtypes)

#convert datatype for all columns into float
df=pd.DataFrame(technologies)
df.dtypes
cols=["fee","duration"]
df[cols]=df[cols].astype(float)
print(df)

#ignore errors
df=df.astype({"courses":int},errors="ignore")
df.dtypes

#generate errors
df=df.astype({"courses":int},errors="raise")
df.dtypes

#convert feed column to numeric type
df=df.astype(str)
print(df)

#create csv file
import pandas as pd
tech={"courses":["math","science","history"],"fee":[2000,300,1000],"duration":["30","40","92"]}
df=pd.DataFrame(tech)
df
df.to_csv("data_file.csv")
#read csv file
df=pd.read_csv("data_file.csv")
df





#create dataframe of null values
import pandas as pd
import numpy as np
tech={"courses":["math","history","science","python","geography"],"fees":[1,2,3,4,5],"duration":["10","20","30","40","50"],"discount":[1.1,20.1,30.2,40.3,50.4]}
row_labels=["r0","r1","r2","r3","r4"]
df=pd.DataFrame(tech ,index=row_labels)
print(df)

#properties of dataframe
df.shape
df.size
df.columns
df.columns.values
df.index
df.dtypes
df.info

#accessing one column
df["fees"]
#accessing two columns
df[["fees","courses"]]
#select certain row and asign to another
df2=df[2:]
df
#accessing certain cell from column duration
df["duration"][2]

#substracting specific value from column
df["fees"]=df["fees"]-1
df["fees"]

#describe dataframe for all columns
df.describe()


#rename dataframe column name
df=pd.DataFrame(tech,index=row_labels)
df.columns=["a","b","c","d"]
df

#rename column name using rename method 
#for accessing row give axis=0 and for column give axis=1
df=pd.DataFrame(tech,index=row_labels)
df.columns=["a","b","c","d"]
  #or
df2=df.rename({"a":"c1","b":"c2"},axis=1)
  #or
df2=df.rename({"c":"c3","d":"c4"},axis="columns")
  #or
df2=df.rename(columns={"a":"c1","b":"c2"})
df2







________________________________________________________________
#drop dataframe rows and column




###droping of rows
#drop rows by labels
df1=df.drop(["r0","r1"])
df1

#delete row by index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1

#delete row by index range.from 2 all will be deleted
df1=df.drop(df.index[2:])
df1

#when you have default index.
df=pd.DataFrame(tech)
df
#deleting one row with index 0
df=df.drop(0)
df

df=pd.DataFrame(tech)
df
#deleting row with default index 0 and 3
df1=df.drop([0,3])
df1

#delete rows in range with default index
df2=df.drop(range(0,3))#it delete 0 to 2
df2







###droping of column!!!!!!!imp!!!!!!!!
#in it, it is mandatory to give axis=1
df2=df.drop(["fees"],axis=1)
df2


#exiplicitly giving parameter name label
df2=df.drop(labels=["fees"],axis=1)
df2

#instead of label you can also give columns
df2=df.drop(columns=["duration"],axis=1)
df2

#drop column by index
df2=df.drop(df.columns[2],axis=1)#here duration column get drop
df2

#for deleting column with working on original dataframe
df.drop(df.columns[1],axis=1,inplace=True)#when working on original dataframe then give inplace=true
print(df)


#drop two or more column by label name
df=pd.DataFrame(tech)
df
df2=df.drop(["fees","duration"],axis=1)
df2

#drop two or more column by index
df=pd.DataFrame(tech)
df
df2=df.drop(df.columns[[2,1]],axis=1)
df2 #for deleting row and column using index we have to use [[]]


#drop column from list of column
df=pd.DataFrame(tech)
df
x=["courses","fees"]
df2=df.drop(x,axis=1)
print(df2)









#loc and iloc !!!!!!!!VVIMP!!!!!!!!!!!
#these are also called slicing operator


##iloc  -------------> used when perform operation using index 
import pandas as pd
import numpy as np
tech={"courses":["math","history","science","python","geography"],"fees":[1,2,3,4,5],"duration":["10","20","30","40","50"],"discount":[1.1,20.1,30.2,40.3,50.4]}
row_labels=["r0","r1","r2","r3","r4"]
df=pd.DataFrame(tech ,index=row_labels)
print(df)


   #syntax of iloc => df.iloc[startrow:endrow,startcolumn:endcolumn]


df2=df.iloc[:,:2]#here column print upto 1 index and all rows
df2

df2=df.iloc[0:2,:]#all column and 2 rows
df2

df2=df.iloc[1:2,1:3] #one row and 2 column
df2


#select row by integer index
df2=df.iloc[2]
df2

#select row by index list
df2=df.iloc[[2,3,4]]
df2
df2=df.iloc[1:5]
df2
df2=df.iloc[:2]#select upto 2 rows
df2
df2=df.iloc[:]#select all rows
df2
df2=df.iloc[-1:]#select last row
df2
df2=df.iloc[::2]#select alternate rows
df2






##loc --------------->used when perform operation using name
   
     #syntax of loc => df.loc[startrow:endrow,startcolumn:endcolumn]

#select using row labels
df2=df.loc["r1"]#select only r1
df2
df2=df.loc[["r2","r3"]]#select only r2 and r3
df2
df2=df.loc["r1":"r3"]#select from r1 to r3.use for range
df2
df2=df.loc["r1":"r5":2]#select alternate rows
df2

#column slicing
  #syntax of loc=> df.loc[:,start:stop:step]

#select multiple column
df2=df.loc[:,["courses","fees","duration"]]
df2
#select column bet two column
df2=df.loc[:,"courses":"duration"]
df2
#select column by range
df2=df.loc[:,"duration":]
df2
#select upto fees
df2=df.loc[:,:"fees"]
df2




