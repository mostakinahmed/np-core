import numpy as np

arr  =  np.array([8,4,6,1,3,5])

print(arr)
print(arr[1:5])

print(arr[2:6:2])

print(arr[::2])

print(arr[::-1])

print("\n\n")
arr2  =  np.array([[8,4,6,1,3,5],[8,1,6,7,3,2],[8,4,3,1,4,2],[8,7,3,9,2,2]])
print(arr2)
print("\n\n")
print(arr2[1:4,2:6])

