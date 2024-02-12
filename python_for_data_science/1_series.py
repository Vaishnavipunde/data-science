#index
import pandas as pd
songs2=pd.Series([12,33,1])
songs2.index

#the index is in string
songs3=pd.Series([3,2,1,4],name="count",index=["john","paul","marry","george"])
songs3.index
songs3





#numeric column become NAN
#import and reading csv file 

import pandas as pd
file=pd.read_csv("C:/1-python/age.csv")
file

#importing exel file and read it
import pandas as pd
file=pd.read_excel("C:/1-python/Bahaman.xlsx")
file





#accessing series element
import numpy as np
x=np.array([11,22,33,12])
x[1]
   #and
songs3=pd.Series([33,44,2])
songs3[1]





#series creation
george=pd.Series([1,23,3,4],index=["1968","3845","87","967"],name="george songs")
george
george["1968"]#reading values
for item in george: #iteration for series
    print(item)


#updating values in series
george=pd.Series([1,23,3,4],index=["1968","3845","87","967"],name="george songs")
george
george["1968"]=86
for item in george:
    print(item)

#deletion in series
import pandas as pd
s=pd.Series([23,44,22],index=[1,2,3])
del s[1]
print(s)







#convert types
songs66=pd.Series([3,None,88],index=["a","b","c"],name="counts")
songs66.dtypes


pd.to_numeric(songs66.apply(str))#it will give error
#for remove error.# converting data type
pd.to_numeric(songs66.astype(str),errors="coerce")#it will give error










#for removing NAN value
songs66.fillna(-1)

#drop NAN value from series
songs66.dropna()







#append ,combining,joining to series
s=pd.Series([1,2,3,4],index=["a","b","c","d"],name="counts")
x=s.append(songs66)
x







#plotting series
import matplotlib.pyplot as plt
fig=plt.figure()
s.plot()
plt.legend()

#plotting two graphs
fig=plt.figure()
s.plot(kind="bar")
songs66.plot(kind="bar",color="r")
plt.legend()

#for plotting histogram
import numpy as np
data=pd.Series(np.random.randn(500),name="500 random")
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()






___________________________________________________________________




#for checking version of pandas
import pandas as pd
pd.__version__



