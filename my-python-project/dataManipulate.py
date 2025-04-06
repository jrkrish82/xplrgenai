import pandas as pd

df=pd.read_csv('data.csv')

#fect the first 5 rows
print(df.head(5))

grouped_sum=df.groupby(['Product','Region'])['Value'].sum()
print(grouped_sum)

## aggregate multiple functions
groudped_agg=df.groupby('Region')['Value'].agg(['sum','count'])
print(groudped_agg)