import pandas as pd
from sqlalchemy import create_engine

# Create a connection to the database
engine = create_engine('sqlite:///example.db') 

# Load data into a pandas DataFrame
df = pd.read_sql('SELECT * FROM EMPLOYEES', engine)
print(df)

# Convert the 'Age' and 'Salary' columns to NumPy arrays
age_vector = df['age'].values
salary_vector = df['salary'].values

print("Age Vector:", age_vector)
print("Salary Vector:", salary_vector)
