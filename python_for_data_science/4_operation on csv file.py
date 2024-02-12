# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 15:59:42 2023

@author: sai
"""
import pandas as pd
import numpy as np
df=pd.read_csv("C:/2-dataset/bank_data.csv")


df.shape
 (45211, 32)
 
 
df.size
1446752


df.columns
Index(['age', 'default', 'balance', 'housing', 'loan', 'duration', 'campaign',
       'pdays', 'previous', 'poutfailure', 'poutother', 'poutsuccess',
       'poutunknown', 'con_cellular', 'con_telephone', 'con_unknown',
       'divorced', 'married', 'single', 'joadmin.', 'joblue.collar',
       'joentrepreneur', 'johousemaid', 'jomanagement', 'joretired',
       'joself.employed', 'joservices', 'jostudent', 'jotechnician',
       'jounemployed', 'jounknown', 'y'],
      dtype='object')


df.columns.values
array(['age', 'default', 'balance', 'housing', 'loan', 'duration',
       'campaign', 'pdays', 'previous', 'poutfailure', 'poutother',
       'poutsuccess', 'poutunknown', 'con_cellular', 'con_telephone',
       'con_unknown', 'divorced', 'married', 'single', 'joadmin.',
       'joblue.collar', 'joentrepreneur', 'johousemaid', 'jomanagement',
       'joretired', 'joself.employed', 'joservices', 'jostudent',
       'jotechnician', 'jounemployed', 'jounknown', 'y'], dtype=object)


df.dtypes

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


df["age"]
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




df[["balance","loan"]]
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



df2=df[4:]
df

 age  default  balance  housing  ...  jotechnician  jounemployed  jounknown  y
0       58        0     2143        1  ...             0             0          0  0
1       44        0       29        1  ...             1             0          0  0
2       33        0        2        1  ...             0             0          0  0
3       47        0     1506        1  ...             0             0          0  0
4       33        0        1        0  ...             0             0          1  0
   ...      ...      ...      ...  ...           ...           ...        ... ..
45206   51        0      825        0  ...             1             0          0  1
45207   71        0     1729        0  ...             0             0          0  1
45208   72        0     5715        0  ...             0             0          0  1
45209   57        0      668        0  ...             0             0          0  0
45210   37        0     2971        0  ...             0             0          0  0

[45211 rows x 32 columns]
df2=df.rename(columns={"age":"c1","balance":"c2"})
df2

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
df["age"]=df["age"]-1
df["age"]

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
################################################################################################################################################





import pandas as pd
import numpy as np
df=pd.read_csv("C:/2-dataset/crime_data.csv")

df.shape
(50, 5)

df.size
 250
 
 
df.columns
 Index(['Unnamed: 0', 'Murder', 'Assault', 'UrbanPop', 'Rape'], dtype='object')
 
df.columns.values
array(['Unnamed: 0', 'Murder', 'Assault', 'UrbanPop', 'Rape'],
      dtype=object)

df.dtypes
Unnamed: 0     object
Murder        float64
Assault         int64
UrbanPop        int64
Rape          float64
dtype: object

df2=df.rename(columns={"Murder":"not","Rape":"no"})
df2
