import pandas as pd

data=[1,2,3,4,5]
series=pd.Series(data)
print("Series \n",series)
print(type(series))


## Dataframe
## create a Dataframe from a dictionary oof list

data={
    'Name':['Krishna','Abc','Def'],
    'Age':[25,30,45],
    'City':['Chicago','New York','Florida']
}
df=pd.DataFrame(data)
print(df)
print(type(df))