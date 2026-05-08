import numpy as np

# Static 3D array A
a = np.array(
    [
        [11, 22, 33, 44, 5, 666],
        [37, 38, 39, 40, 41, 42],
        [73, 74, 75, 7, 77, 78],
    ]
)

b = np.sort(a, axis=1)


print(b)
