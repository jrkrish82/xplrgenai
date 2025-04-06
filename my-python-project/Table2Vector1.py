import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import MinMaxScaler


# Create a connection to the database
engine = create_engine('sqlite:///example.db') 

# Load data into a pandas DataFrame
df = pd.read_sql('SELECT * FROM EMPLOYEES', engine)
print(df)

# Initialize the scaler
scaler = MinMaxScaler()

# Normalize the 'Age' and 'Salary' columns
df[['age', 'salary']] = scaler.fit_transform(df[['age', 'salary']])
print(df)

# Convert the normalized DataFrame to NumPy arrays
vectors = df.values
print("Normalized Vectors:\n", vectors)