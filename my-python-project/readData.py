import pandas as pd
from io import StringIO

Data = '{"employee_name": "Krishna", "email": "krishna@gmail.com", "job_profile": [{"title1":"Principal Architect", "title2":"Solution Architect"}]}'
df=pd.read_json(StringIO(Data))

print(df.to_json())

print(df.to_json(orient='index'))