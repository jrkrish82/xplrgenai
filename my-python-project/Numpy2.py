import numpy as np

## 2d array
arr2=np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr2)
print(arr2.shape)

np.arange(0,10,2).reshape(5,1)

## Attributes of Numpy Array
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:\n", arr)
print("Shape:", arr.shape)  # Output: (2, 3)
print("Number of dimensions:", arr.ndim)  # Output: 2
print("Size (number of elements):", arr.size)  # Output: 6
print("Data type:", arr.dtype)  # Output: int32 (may vary based on platform)
print("Item size (in bytes):", arr.itemsize)  # Output: 8 (may vary based on platform)

### Numpy Vectorized Operation
arr1=np.array([1,2,3,4,5])
arr2=np.array([10,20,30,40,50])

### Element Wise addition
print("Addition:", arr1+arr2)

## Element Wise Substraction
print("Substraction:", arr1-arr2)

# Element-wise multiplication
print("Multiplication:", arr1 * arr2)

# Element-wise division
print("Division:", arr1 / arr2)