# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 11:42:40 2023

@author: sai
"""

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
Out[63]: 
Unnamed: 0     object
Murder        float64
Assault         int64
UrbanPop        int64
Rape          float64
dtype: object



df["Murder"]
Out[64]: 
0     13.2
1     10.0
2      8.1
3      8.8
4      9.0
5      7.9
6      3.3
7      5.9
8     15.4
9     17.4
10     5.3
11     2.6
12    10.4
13     7.2
14     2.2
15     6.0
16     9.7
17    15.4
18     2.1
19    11.3
20     4.4
21    12.1
22     2.7
23    16.1
24     9.0
25     6.0
26     4.3
27    12.2
28     2.1
29     7.4
30    11.4
31    11.1
32    13.0
33     0.8
34     7.3
35     6.6
36     4.9
37     6.3
38     3.4
39    14.4
40     3.8
41    13.2
42    12.7
43     3.2
44     2.2
45     8.5
46     4.0
47     5.7
48     2.6
49     6.8
Name: Murder, dtype: float64






df[["Murder","Rape"]]
    Murder  Rape
0     13.2  21.2
1     10.0  44.5
2      8.1  31.0
3      8.8  19.5
4      9.0  40.6
5      7.9  38.7
6      3.3  11.1
7      5.9  15.8
8     15.4  31.9
9     17.4  25.8
10     5.3  20.2
11     2.6  14.2
12    10.4  24.0
13     7.2  21.0
14     2.2  11.3
15     6.0  18.0
16     9.7  16.3
17    15.4  22.2
18     2.1   7.8
19    11.3  27.8
20     4.4  16.3
21    12.1  35.1
22     2.7  14.9
23    16.1  17.1
24     9.0  28.2
25     6.0  16.4
26     4.3  16.5
27    12.2  46.0
28     2.1   9.5
29     7.4  18.8
30    11.4  32.1
31    11.1  26.1
32    13.0  16.1
33     0.8   7.3
34     7.3  21.4
35     6.6  20.0
36     4.9  29.3
37     6.3  14.9
38     3.4   8.3
39    14.4  22.5
40     3.8  12.8
41    13.2  26.9
42    12.7  25.5
43     3.2  22.9
44     2.2  11.2
45     8.5  20.7
46     4.0  26.2
47     5.7   9.3
48     2.6  10.8
49     6.8  15.6



df.describe()
Out[66]: 
         Murder     Assault   UrbanPop       Rape
count  50.00000   50.000000  50.000000  50.000000
mean    7.78800  170.760000  65.540000  21.232000
std     4.35551   83.337661  14.474763   9.366385
min     0.80000   45.000000  32.000000   7.300000
25%     4.07500  109.000000  54.500000  15.075000
50%     7.25000  159.000000  66.000000  20.100000
75%    11.25000  249.000000  77.750000  26.175000
max    17.40000  337.000000  91.000000  46.000000


df2=df.rename(columns={"Murder":"c1","Rape":"c2"})
df2
Out[68]: 
        Unnamed: 0    c1  Assault  UrbanPop    c2
0          Alabama  13.2      236        58  21.2
1           Alaska  10.0      263        48  44.5
2          Arizona   8.1      294        80  31.0
3         Arkansas   8.8      190        50  19.5
4       California   9.0      276        91  40.6
5         Colorado   7.9      204        78  38.7
6      Connecticut   3.3      110        77  11.1
7         Delaware   5.9      238        72  15.8
8          Florida  15.4      335        80  31.9
9          Georgia  17.4      211        60  25.8
10          Hawaii   5.3       46        83  20.2
11           Idaho   2.6      120        54  14.2
12        Illinois  10.4      249        83  24.0
13         Indiana   7.2      113        65  21.0
14            Iowa   2.2       56        57  11.3
15          Kansas   6.0      115        66  18.0
16        Kentucky   9.7      109        52  16.3
17       Louisiana  15.4      249        66  22.2
18           Maine   2.1       83        51   7.8
19        Maryland  11.3      300        67  27.8
20   Massachusetts   4.4      149        85  16.3
21        Michigan  12.1      255        74  35.1
22       Minnesota   2.7       72        66  14.9
23     Mississippi  16.1      259        44  17.1
24        Missouri   9.0      178        70  28.2
25         Montana   6.0      109        53  16.4
26        Nebraska   4.3      102        62  16.5
27          Nevada  12.2      252        81  46.0
28   New Hampshire   2.1       57        56   9.5
29      New Jersey   7.4      159        89  18.8
30      New Mexico  11.4      285        70  32.1
31        New York  11.1      254        86  26.1
32  North Carolina  13.0      337        45  16.1
33    North Dakota   0.8       45        44   7.3
34            Ohio   7.3      120        75  21.4
35        Oklahoma   6.6      151        68  20.0
36          Oregon   4.9      159        67  29.3
37    Pennsylvania   6.3      106        72  14.9
38    Rhode Island   3.4      174        87   8.3
39  South Carolina  14.4      279        48  22.5
40    South Dakota   3.8       86        45  12.8
41       Tennessee  13.2      188        59  26.9
42           Texas  12.7      201        80  25.5
43            Utah   3.2      120        80  22.9
44         Vermont   2.2       48        32  11.2
45        Virginia   8.5      156        63  20.7
46      Washington   4.0      145        73  26.2
47   West Virginia   5.7       81        39   9.3
48       Wisconsin   2.6       53        66  10.8
49         Wyoming   6.8      161        60  15.6



df2=df[4:]
df2
Out[70]: 
        Unnamed: 0  Murder  Assault  UrbanPop  Rape
4       California     9.0      276        91  40.6
5         Colorado     7.9      204        78  38.7
6      Connecticut     3.3      110        77  11.1
7         Delaware     5.9      238        72  15.8
8          Florida    15.4      335        80  31.9
9          Georgia    17.4      211        60  25.8
10          Hawaii     5.3       46        83  20.2
11           Idaho     2.6      120        54  14.2
12        Illinois    10.4      249        83  24.0
13         Indiana     7.2      113        65  21.0
14            Iowa     2.2       56        57  11.3
15          Kansas     6.0      115        66  18.0
16        Kentucky     9.7      109        52  16.3
17       Louisiana    15.4      249        66  22.2
18           Maine     2.1       83        51   7.8
19        Maryland    11.3      300        67  27.8
20   Massachusetts     4.4      149        85  16.3
21        Michigan    12.1      255        74  35.1
22       Minnesota     2.7       72        66  14.9
23     Mississippi    16.1      259        44  17.1
24        Missouri     9.0      178        70  28.2
25         Montana     6.0      109        53  16.4
26        Nebraska     4.3      102        62  16.5
27          Nevada    12.2      252        81  46.0
28   New Hampshire     2.1       57        56   9.5
29      New Jersey     7.4      159        89  18.8
30      New Mexico    11.4      285        70  32.1
31        New York    11.1      254        86  26.1
32  North Carolina    13.0      337        45  16.1
33    North Dakota     0.8       45        44   7.3
34            Ohio     7.3      120        75  21.4
35        Oklahoma     6.6      151        68  20.0
36          Oregon     4.9      159        67  29.3
37    Pennsylvania     6.3      106        72  14.9
38    Rhode Island     3.4      174        87   8.3
39  South Carolina    14.4      279        48  22.5
40    South Dakota     3.8       86        45  12.8
41       Tennessee    13.2      188        59  26.9
42           Texas    12.7      201        80  25.5
43            Utah     3.2      120        80  22.9
44         Vermont     2.2       48        32  11.2
45        Virginia     8.5      156        63  20.7
46      Washington     4.0      145        73  26.2
47   West Virginia     5.7       81        39   9.3
48       Wisconsin     2.6       53        66  10.8
49         Wyoming     6.8      161        60  15.6




df["x"]=df["Rape"]-1
df["x"]
Out[71]: 
0     20.2
1     43.5
2     30.0
3     18.5
4     39.6
5     37.7
6     10.1
7     14.8
8     30.9
9     24.8
10    19.2
11    13.2
12    23.0
13    20.0
14    10.3
15    17.0
16    15.3
17    21.2
18     6.8
19    26.8
20    15.3
21    34.1
22    13.9
23    16.1
24    27.2
25    15.4
26    15.5
27    45.0
28     8.5
29    17.8
30    31.1
31    25.1
32    15.1
33     6.3
34    20.4
35    19.0
36    28.3
37    13.9
38     7.3
39    21.5
40    11.8
41    25.9
42    24.5
43    21.9
44    10.2
45    19.7
46    25.2
47     8.3
48     9.8
49    14.6
Name: x, dtype: float64




df1=df.drop(df.index[1])
df1
Out[73]: 
        Unnamed: 0  Murder  Assault  UrbanPop  Rape     x
0          Alabama    13.2      236        58  21.2  20.2
2          Arizona     8.1      294        80  31.0  30.0
3         Arkansas     8.8      190        50  19.5  18.5
4       California     9.0      276        91  40.6  39.6
5         Colorado     7.9      204        78  38.7  37.7
6      Connecticut     3.3      110        77  11.1  10.1
7         Delaware     5.9      238        72  15.8  14.8
8          Florida    15.4      335        80  31.9  30.9
9          Georgia    17.4      211        60  25.8  24.8
10          Hawaii     5.3       46        83  20.2  19.2
11           Idaho     2.6      120        54  14.2  13.2
12        Illinois    10.4      249        83  24.0  23.0
13         Indiana     7.2      113        65  21.0  20.0
14            Iowa     2.2       56        57  11.3  10.3
15          Kansas     6.0      115        66  18.0  17.0
16        Kentucky     9.7      109        52  16.3  15.3
17       Louisiana    15.4      249        66  22.2  21.2
18           Maine     2.1       83        51   7.8   6.8
19        Maryland    11.3      300        67  27.8  26.8
20   Massachusetts     4.4      149        85  16.3  15.3
21        Michigan    12.1      255        74  35.1  34.1
22       Minnesota     2.7       72        66  14.9  13.9
23     Mississippi    16.1      259        44  17.1  16.1
24        Missouri     9.0      178        70  28.2  27.2
25         Montana     6.0      109        53  16.4  15.4
26        Nebraska     4.3      102        62  16.5  15.5
27          Nevada    12.2      252        81  46.0  45.0
28   New Hampshire     2.1       57        56   9.5   8.5
29      New Jersey     7.4      159        89  18.8  17.8
30      New Mexico    11.4      285        70  32.1  31.1
31        New York    11.1      254        86  26.1  25.1
32  North Carolina    13.0      337        45  16.1  15.1
33    North Dakota     0.8       45        44   7.3   6.3
34            Ohio     7.3      120        75  21.4  20.4
35        Oklahoma     6.6      151        68  20.0  19.0
36          Oregon     4.9      159        67  29.3  28.3
37    Pennsylvania     6.3      106        72  14.9  13.9
38    Rhode Island     3.4      174        87   8.3   7.3
39  South Carolina    14.4      279        48  22.5  21.5
40    South Dakota     3.8       86        45  12.8  11.8
41       Tennessee    13.2      188        59  26.9  25.9
42           Texas    12.7      201        80  25.5  24.5
43            Utah     3.2      120        80  22.9  21.9
44         Vermont     2.2       48        32  11.2  10.2
45        Virginia     8.5      156        63  20.7  19.7
46      Washington     4.0      145        73  26.2  25.2
47   West Virginia     5.7       81        39   9.3   8.3
48       Wisconsin     2.6       53        66  10.8   9.8
49         Wyoming     6.8      161        60  15.6  14.6




df1=df.drop(df.index[2:])
df1

Out[75]: 
  Unnamed: 0  Murder  Assault  UrbanPop  Rape     x
0    Alabama    13.2      236        58  21.2  20.2
1     Alaska    10.0      263        48  44.5  43.5





df1=df.drop([0,3])
df1
Out[76]: 
        Unnamed: 0  Murder  Assault  UrbanPop  Rape     x
1           Alaska    10.0      263        48  44.5  43.5
2          Arizona     8.1      294        80  31.0  30.0
4       California     9.0      276        91  40.6  39.6
5         Colorado     7.9      204        78  38.7  37.7
6      Connecticut     3.3      110        77  11.1  10.1
7         Delaware     5.9      238        72  15.8  14.8
8          Florida    15.4      335        80  31.9  30.9
9          Georgia    17.4      211        60  25.8  24.8
10          Hawaii     5.3       46        83  20.2  19.2
11           Idaho     2.6      120        54  14.2  13.2
12        Illinois    10.4      249        83  24.0  23.0
13         Indiana     7.2      113        65  21.0  20.0
14            Iowa     2.2       56        57  11.3  10.3
15          Kansas     6.0      115        66  18.0  17.0
16        Kentucky     9.7      109        52  16.3  15.3
17       Louisiana    15.4      249        66  22.2  21.2
18           Maine     2.1       83        51   7.8   6.8
19        Maryland    11.3      300        67  27.8  26.8
20   Massachusetts     4.4      149        85  16.3  15.3
21        Michigan    12.1      255        74  35.1  34.1
22       Minnesota     2.7       72        66  14.9  13.9
23     Mississippi    16.1      259        44  17.1  16.1
24        Missouri     9.0      178        70  28.2  27.2
25         Montana     6.0      109        53  16.4  15.4
26        Nebraska     4.3      102        62  16.5  15.5
27          Nevada    12.2      252        81  46.0  45.0
28   New Hampshire     2.1       57        56   9.5   8.5
29      New Jersey     7.4      159        89  18.8  17.8
30      New Mexico    11.4      285        70  32.1  31.1
31        New York    11.1      254        86  26.1  25.1
32  North Carolina    13.0      337        45  16.1  15.1
33    North Dakota     0.8       45        44   7.3   6.3
34            Ohio     7.3      120        75  21.4  20.4
35        Oklahoma     6.6      151        68  20.0  19.0
36          Oregon     4.9      159        67  29.3  28.3
37    Pennsylvania     6.3      106        72  14.9  13.9
38    Rhode Island     3.4      174        87   8.3   7.3
39  South Carolina    14.4      279        48  22.5  21.5
40    South Dakota     3.8       86        45  12.8  11.8
41       Tennessee    13.2      188        59  26.9  25.9
42           Texas    12.7      201        80  25.5  24.5
43            Utah     3.2      120        80  22.9  21.9
44         Vermont     2.2       48        32  11.2  10.2
45        Virginia     8.5      156        63  20.7  19.7
46      Washington     4.0      145        73  26.2  25.2
47   West Virginia     5.7       81        39   9.3   8.3
48       Wisconsin     2.6       53        66  10.8   9.8
49         Wyoming     6.8      161        60  15.6  14.6





df2=df.drop(range(0,3))#it delete 0 to 2
df2





df2=df.drop(["Murder"],axis=1)
df2







df2=df.drop(df.columns[2],axis=1)#here duration column get drop
df2





x=["Murder","Rape"]
df2=df.drop(x,axis=1)
print(df2)





df2=df.iloc[:,:2]#here column print upto 1 index and all rows
df2








