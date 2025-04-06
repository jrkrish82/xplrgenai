import pandas as pd

df=pd.read_csv('sales_data.csv')
#print(df)
#print(df.head(5))
#print(df.tail(15))
#print(df.shape)
#print(df.describe())
#print(df.info())
#print(df.columns)
print(df['Total'])
print(df['Total'].sum())
print(df['Total'].mean())

print(df.loc[0,"Product"])

print(df.iloc[0])

print(df.iat[2,2])

# Describe the data frame
print(df.describe())

