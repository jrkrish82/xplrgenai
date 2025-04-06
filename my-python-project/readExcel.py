import pandas as pd

df_excel=pd.read_excel('data.xlsx')

df_excel.to_pickle('df_excel')

df = pd.read_pickle('df_excel')

print(df)

#how to write a pickle file into xml
df.to_xml('data.xml')

print(df.to_json())

#how to write a pickle file into json with proper object format
df.to_json('data.json',orient='records')


