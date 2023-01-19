import numpy as np

array1 = np.array([1,2,3,4])
print("One dimensional array",array1)

listarray = np.array([(1,2,3,8),(5,6,4,7),(3,5,7,2)])
print("Original array: ",listarray)
print("Array dimension: ",listarray.ndim)
print("Array Data Type: ",listarray.dtype)
print("Array item size: ",listarray.itemsize)
print("Array size: ",listarray.size)
print("Array shape: ",listarray.shape)
listarray2 = np.array([(1,2,3,8),(5,6,4,7),(3,5,7,2)])
print("Original array:\n",listarray2)
print("Reshape the array:\n",listarray2.reshape(6,2))
array3= listarray2.copy()
print("Copy value one array to another:\n",array3)
array4 = np.array([5,8,97,7])
print("Another array: ",array4)
array4[1] = 44
print("Another array: ",array4)

print("Iterate on the elements of the 1-D array")
for y in array4:
    print(y)
print("Iterate on the elements of the 2-D array")
for x in array3:
    for y in x:
        print(y)
        