# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 11:38:28 2023

@author: sai
"""

import pandas as pd
import numpy as np
df=pd.read_csv("C:/2-dataset/bank_data.csv")



df.shape
Out[2]: (45211, 32)


 
df.size
Out[3]: 1446752




df.columns
Out[4]: 
Index(['age', 'default', 'balance', 'housing', 'loan', 'duration', 'campaign',
       'pdays', 'previous', 'poutfailure', 'poutother', 'poutsuccess',
       'poutunknown', 'con_cellular', 'con_telephone', 'con_unknown',
       'divorced', 'married', 'single', 'joadmin.', 'joblue.collar',
       'joentrepreneur', 'johousemaid', 'jomanagement', 'joretired',
       'joself.employed', 'joservices', 'jostudent', 'jotechnician',
       'jounemployed', 'jounknown', 'y'],
      dtype='object')


df.columns.values
Out[5]: 
array(['age', 'default', 'balance', 'housing', 'loan', 'duration',
       'campaign', 'pdays', 'previous', 'poutfailure', 'poutother',
       'poutsuccess', 'poutunknown', 'con_cellular', 'con_telephone',
       'con_unknown', 'divorced', 'married', 'single', 'joadmin.',
       'joblue.collar', 'joentrepreneur', 'johousemaid', 'jomanagement',
       'joretired', 'joself.employed', 'joservices', 'jostudent',
       'jotechnician', 'jounemployed', 'jounknown', 'y'], dtype=object)



#display type
df.dtypes
Out[6]: 
age                int64
default            int64
balance            int64
housing            int64
loan               int64
duration           int64
campaign           int64
pdays              int64
previous           int64
poutfailure        int64
poutother          int64
poutsuccess        int64
poutunknown        int64
con_cellular       int64
con_telephone      int64
con_unknown        int64
divorced           int64
married            int64
single             int64
joadmin.           int64
joblue.collar      int64
joentrepreneur     int64
johousemaid        int64
jomanagement       int64
joretired          int64
joself.employed    int64
joservices         int64
jostudent          int64
jotechnician       int64
jounemployed       int64
jounknown          int64
y                  int64
dtype: object



#display one column
df["age"]
Out[7]: 
0        58
1        44
2        33
3        47
4        33
         ..
45206    51
45207    71
45208    72
45209    57
45210    37
Name: age, Length: 45211, dtype: int64




#printing two column
df[["balance","loan"]]
Out[8]: 
       balance  loan
0         2143     0
1           29     0
2            2     1
3         1506     0
4            1     0
       ...   ...
45206      825     0
45207     1729     0
45208     5715     0
45209      668     0
45210     2971     0

[45211 rows x 2 columns]


df.describe()
Out[9]: 
                age       default  ...     jounknown             y
count  45211.000000  45211.000000  ...  45211.000000  45211.000000
mean      40.936210      0.018027  ...      0.006370      0.116985
std       10.618762      0.133049  ...      0.079559      0.321406
min       18.000000      0.000000  ...      0.000000      0.000000
25%       33.000000      0.000000  ...      0.000000      0.000000
50%       39.000000      0.000000  ...      0.000000      0.000000
75%       48.000000      0.000000  ...      0.000000      0.000000
max       95.000000      1.000000  ...      1.000000      1.000000

[8 rows x 32 columns]

#rename the column
df2=df.rename(columns={"age":"c1","balance":"c2"})
df2

Out[11]: 
       c1  default    c2  housing  ...  jotechnician  jounemployed  jounknown  y
0      58        0  2143        1  ...             0             0          0  0
1      44        0    29        1  ...             1             0          0  0
2      33        0     2        1  ...             0             0          0  0
3      47        0  1506        1  ...             0             0          0  0
4      33        0     1        0  ...             0             0          1  0
   ..      ...   ...      ...  ...           ...           ...        ... ..
45206  51        0   825        0  ...             1             0          0  1
45207  71        0  1729        0  ...             0             0          0  1
45208  72        0  5715        0  ...             0             0          0  1
45209  57        0   668        0  ...             0             0          0  0
45210  37        0  2971        0  ...             0             0          0  0

[45211 rows x 32 columns]


#printing rows from 4
df2=df[4:]
df2

Out[13]: 
       age  default  balance  housing  ...  jotechnician  jounemployed  jounknown  y
4       33        0        1        0  ...             0             0          1  0
5       35        0      231        1  ...             0             0          0  0
6       28        0      447        1  ...             0             0          0  0
7       42        1        2        1  ...             0             0          0  0
8       58        0      121        1  ...             0             0          0  0
   ...      ...      ...      ...  ...           ...           ...        ... ..
45206   51        0      825        0  ...             1             0          0  1
45207   71        0     1729        0  ...             0             0          0  1
45208   72        0     5715        0  ...             0             0          0  1
45209   57        0      668        0  ...             0             0          0  0
45210   37        0     2971        0  ...             0             0          0  0

[45207 rows x 32 columns]

#substracting one item
df["age"]=df["age"]-1
df["age"]

Out[15]: 
0        57
1        43
2        32
3        46
4        32
         ..
45206    50
45207    70
45208    71
45209    56
45210    36
Name: age, Length: 45211, dtype: int64

df1=df.drop(df.index[1])
df1

Out[18]: 
       age  default  balance  housing  ...  jotechnician  jounemployed  jounknown  y
0       57        0     2143        1  ...             0             0          0  0
2       32        0        2        1  ...             0             0          0  0
3       46        0     1506        1  ...             0             0          0  0
4       32        0        1        0  ...             0             0          1  0
5       34        0      231        1  ...             0             0          0  0
   ...      ...      ...      ...  ...           ...           ...        ... ..
45206   50        0      825        0  ...             1             0          0  1
45207   70        0     1729        0  ...             0             0          0  1
45208   71        0     5715        0  ...             0             0          0  1
45209   56        0      668        0  ...             0             0          0  0
45210   36        0     2971        0  ...             0             0          0  0

[45210 rows x 32 columns]


df1=df.drop(df.index[2:])
df1

 age  default  balance  housing  ...  jotechnician  jounemployed  jounknown  y
0   57        0     2143        1  ...             0             0          0  0
1   43        0       29        1  ...             1             0          0  0

[2 rows x 32 columns]


df1=df.drop([0,3])
df1

Out[22]: 
       age  default  balance  housing  ...  jotechnician  jounemployed  jounknown  y
1       43        0       29        1  ...             1             0          0  0
2       32        0        2        1  ...             0             0          0  0
4       32        0        1        0  ...             0             0          1  0
5       34        0      231        1  ...             0             0          0  0
6       27        0      447        1  ...             0             0          0  0
   ...      ...      ...      ...  ...           ...           ...        ... ..
45206   50        0      825        0  ...             1             0          0  1
45207   70        0     1729        0  ...             0             0          0  1
45208   71        0     5715        0  ...             0             0          0  1
45209   56        0      668        0  ...             0             0          0  0
45210   36        0     2971        0  ...             0             0          0  0

[45209 rows x 32 columns]
#drop row in range 
df2=df.drop(range(0,3))#it delete 0 to 2
df2

Out[24]: 
       age  default  balance  housing  ...  jotechnician  jounemployed  jounknown  y
3       46        0     1506        1  ...             0             0          0  0
4       32        0        1        0  ...             0             0          1  0
5       34        0      231        1  ...             0             0          0  0
6       27        0      447        1  ...             0             0          0  0
7       41        1        2        1  ...             0             0          0  0
   ...      ...      ...      ...  ...           ...           ...        ... ..
45206   50        0      825        0  ...             1             0          0  1
45207   70        0     1729        0  ...             0             0          0  1
45208   71        0     5715        0  ...             0             0          0  1
45209   56        0      668        0  ...             0             0          0  0
45210   36        0     2971        0  ...             0             0          0  0

[45208 rows x 32 columns]

#drop one column
df2=df.drop(["age"],axis=1)
df2

Out[27]: 
       default  balance  housing  ...  jounemployed  jounknown  y
0            0     2143        1  ...             0          0  0
1            0       29        1  ...             0          0  0
2            0        2        1  ...             0          0  0
3            0     1506        1  ...             0          0  0
4            0        1        0  ...             0          1  0
       ...      ...      ...  ...           ...        ... ..
45206        0      825        0  ...             0          0  1
45207        0     1729        0  ...             0          0  1
45208        0     5715        0  ...             0          0  1
45209        0      668        0  ...             0          0  0
45210        0     2971        0  ...             0          0  0

[45211 rows x 31 columns]

df2=df.drop(df.columns[2],axis=1)#here 2nd column get drop
df2

Out[29]: 
       age  default  housing  loan  ...  jotechnician  jounemployed  jounknown  y
0       57        0        1     0  ...             0             0          0  0
1       43        0        1     0  ...             1             0          0  0
2       32        0        1     1  ...             0             0          0  0
3       46        0        1     0  ...             0             0          0  0
4       32        0        0     0  ...             0             0          1  0
   ...      ...      ...   ...  ...           ...           ...        ... ..
45206   50        0        0     0  ...             1             0          0  1
45207   70        0        0     0  ...             0             0          0  1
45208   71        0        0     0  ...             0             0          0  1
45209   56        0        0     0  ...             0             0          0  0
45210   36        0        0     0  ...             0             0          0  0

[45211 rows x 31 columns]

#droping column by using list
x=["age","balance"]
df2=df.drop(x,axis=1)
print(df2)

default  housing  loan  ...  jounemployed  jounknown  y
0            0        1     0  ...             0          0  0
1            0        1     0  ...             0          0  0
2            0        1     1  ...             0          0  0
3            0        1     0  ...             0          0  0
4            0        0     0  ...             0          1  0
       ...      ...   ...  ...           ...        ... ..
45206        0        0     0  ...             0          0  1
45207        0        0     0  ...             0          0  1
45208        0        0     0  ...             0          0  1
45209        0        0     0  ...             0          0  0
45210        0        0     0  ...             0          0  0

[45211 rows x 30 columns]


df2=df.iloc[:,:2]#here column print upto 1 index and all rows
df2
Out[34]: 
       age  default
0       57        0
1       43        0
2       32        0
3       46        0
4       32        0
   ...      ...
45206   50        0
45207   70        0
45208   71        0
45209   56        0
45210   36        0

[45211 rows x 2 columns]



#select column bet two column
df2=df.loc[:,"age":"housing"]
df2
Out[36]: 
       age  default  balance  housing
0       57        0     2143        1
1       43        0       29        1
2       32        0        2        1
3       46        0     1506        1
4       32        0        1        0
   ...      ...      ...      ...
45206   50        0      825        0
45207   70        0     1729        0
45208   71        0     5715        0
45209   56        0      668        0
45210   36        0     2971        0

[45211 rows x 4 columns]




























































