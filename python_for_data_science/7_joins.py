# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 14:30:44 2023

@author: sai
"""
#join---------->  in it data get attach horizontally



import pandas as pd
import numpy as np
tech={"courses":["spark","pyspark","python","pandas"],"fees":[7,1,2,3],"duration":["10","90","20","30"]}
row_labels=["r0","r1","r2","r3"]
df1=pd.DataFrame(tech ,index=row_labels)
print(df1)

tech1={"courses":["spark","java","python","go"],"discount":[1,2,3,4]}
row_labels=["r1","b","r3","d"]
df2=pd.DataFrame(tech1,index=row_labels)
df2

#join two dataframes.by default it will be left join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
df3




#inner join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how="inner")
df3

#left join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how="left")
df3

#right join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how="right")
df3





#join on column
#inner join
df3=df1.set_index("courses").join(df2.set_index("courses"),how="inner")
df3
#left join
df3=df1.set_index("courses").join(df2.set_index("courses"),how="left")
df3
#rigth join
df3=df1.set_index("courses").join(df2.set_index("courses"),how="right")
df3






# using pandas.merge ()
df3=pd.merge(df1, df2)
df3

#using dataframe.merge()
df3=df1.merge(df2)
df3







#use pandas.concat() to concate two frame.concat is used for vertically merging

df=pd.DataFrame({"courses":["spark","pyspark","python","pandas"],"fees":[1,2,3,4]})
df1=pd.DataFrame({"courses":["hadoop","pandas","hyperion","java"],"fees":[34,23,12,54]})

data=[df,df1]
df2=pd.concat(data)
df2



#concate multiple dataframe using pandas.concate()
df=pd.DataFrame({"courses":["spark","pyspark","python","pandas"],"fees":[1,2,3,4]})
df1=pd.DataFrame({"courses":["hadoop","pandas","hyperion","java"],"fees":[34,23,12,54]})
df2=pd.DataFrame({"duration":["33","22","11","44"],"discount":[123,125,345,65]})

df3=pd.concat([df,df1,df2])
df3














