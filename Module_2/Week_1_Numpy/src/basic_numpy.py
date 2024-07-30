import numpy as np


# cau 1
print("\nCau 1:")
arr = np.arange(0, 10, 1)  # chon a


# cau 2
print("\nCau 2:")
arr_2a = np.ones((3, 3)) > 0
arr_2b = np.ones((3, 3), dtype=bool)
arr_2c = np.full((3, 3), fill_value=True, dtype=bool)
print("Ket qua y 2a:\n", arr_2a)
print("Ket qua y 2b:\n", arr_2b)
print("Ket qua y 2c:\n", arr_2c)
# chon d


# cau 3
print("\nCau 3:")
arr_3 = np.arange(0, 10)
print(arr_3[arr_3 % 2 == 1])  # chon a


# cau 4
print("\nCau 4:")
arr_4 = np.arange(0, 10)
arr_4[arr_4 % 2 == 1] = -1
print(arr_4)  # chon b


# cau 5
print("\nCau 5:")
arr_5 = np.arange(10)
arr_2d_5 = arr_5.reshape(2, -1)
print(arr_2d_5)  # chon b


# cau 6
print("\nCau 6:")
arr1_6 = np.arange(10).reshape(2, -1)
arr2_6 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1_6, arr2_6], axis=0)
print("Result:\n", c)


# cau 7
print("\nCau 7:")
arr1_7 = np.arange(10).reshape(2, -1)
arr2_7 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1_7, arr2_7], axis=1)
print("Result:\n", c)


# cau 8
print("\nCau 8:")
arr = np.array([1, 2, 3])
print(np.repeat(arr, 3))
print(np.tile(arr, 3))


# cau 9
print("\nCau 9:")
a_9 = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.nonzero((a_9 >= 5) & (a_9 <= 10))
print("result:", a_9[index])


# cau 10
print("\nCau 10:")


def maxx(x, y):
    if x >= y:
        return x
    else:
        return y


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(a, b))


# cau 11
print("\nCau 11:")
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print("Result:", np. where(a < b, b, a))
