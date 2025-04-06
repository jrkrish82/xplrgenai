import pandas as pd

url="https://en.wikipedia.org/wiki/Mobile_country_code"
df= pd.read_html(url,match="Country",header=0)[0]

df.to_json('countrycode.json',orient='records')