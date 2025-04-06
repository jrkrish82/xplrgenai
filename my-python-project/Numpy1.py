import numpy as np
import pandas as pd
print(np.__version__)

# Create a NumPy array
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a pandas DataFrame from the NumPy array
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

print(df)

# Calculate the mean of each column
mean_values = np.mean(df, axis=0)
print("Mean values:\n", mean_values)

# Add a new column with the sum of each row
df['Sum'] = np.sum(df, axis=1)
print("DataFrame with Sum column:\n", df)

# Create a NumPy array
data = np.array([10, 20, 30, 40, 50])

# Convert the NumPy array to a pandas Series
series = pd.Series(data)

# Calculate the rolling mean with a window size of 2
rolling_mean = series.rolling(window=2).mean()
print("Rolling mean:\n", rolling_mean)

# Create a DataFrame with random data
np.random.seed(0)
data = np.random.randn(100, 3)
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Calculate the mean and standard deviation of each column
mean_values = df.mean()
std_values = df.std()

print("Mean values:\n", mean_values)
print("Standard deviation values:\n", std_values)

# Normalize the DataFrame using NumPy
df_normalized = (df - mean_values) / std_values
print("Normalized DataFrame:\n", df_normalized.head())

# Calculate the correlation matrix
correlation_matrix = df.corr()
print("Correlation matrix:\n", correlation_matrix)