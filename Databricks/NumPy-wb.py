# Databricks notebook source
# MAGIC %md #NumPy

# COMMAND ----------

# MAGIC %md ### Importing 

# COMMAND ----------

import numpy as np

# COMMAND ----------

# MAGIC %md ### Creating array

# COMMAND ----------

arr1 = np.array([1,2,3,4,5,6,7,8,9,10], dtype="int32")

arr1

# COMMAND ----------

# MAGIC %md ### get datatype of array
# MAGIC * i - integer
# MAGIC * b - boolean
# MAGIC * u - unsigned integer
# MAGIC * f - float
# MAGIC * c - complex float
# MAGIC * m - timedelta
# MAGIC * M - datetime
# MAGIC * O - object
# MAGIC * S - string
# MAGIC * U - unicode string

# COMMAND ----------

arr1.dtype

# COMMAND ----------

# MAGIC %md ### Dimentions

# COMMAND ----------

arr1.ndim

# COMMAND ----------

D0 = np.array("10")
D1 = np.array(["10", "8", "6"])
D2 = np.array([["10", "8", "6"],["10", "8", "6"]])
D3 = np.array([[["10", "8", "6"],["10", "8", "6"]], [["10", "8", "6"],["10", "8", "6"]]])

print(D0.ndim)
print(D1.ndim)
print(D2.ndim)
print(D3.ndim)

# COMMAND ----------

arr2 = np.array([1,2,3,4,5,6,7,8,9,10], ndmin=2)
print(arr2)

# COMMAND ----------

arr3 = np.array(
  [
    [
      [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    ],
    [
      [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    ]
  ])
print(arr3.ndim)

# COMMAND ----------

# MAGIC %md ### Get Values 

# COMMAND ----------

print(arr1[3:7])
print(arr1[::3])
print(arr1[-3:-7:-2])

# COMMAND ----------

D2[0,1:3]

# COMMAND ----------

D3[0,1,1]

# COMMAND ----------

# MAGIC %md 
# MAGIC # Mathematics

# COMMAND ----------

# x = [1,2,3]
# x+1

print("actual:", arr3)
print("+:", arr3+2)
print("-:", arr3-2)
print("*:", arr3*2)
print("/:", arr3/2)
print("%:", arr3%2)
print("^2:", arr3**2)

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC # Shape

# COMMAND ----------

arr3.shape

# COMMAND ----------

l_arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(l_arr)
print(l_arr.shape)

l_arr2 = l_arr.reshape(4,3)
print(l_arr2)

# COMMAND ----------

# MAGIC %md 
# MAGIC # Randomes

# COMMAND ----------

a1 = np.zeros([3,3])
print(a1)

a2 = np.ones([3,3])
print(a2)

a3 = np.full([3,3], 10)
print(a3)

a4 = np.identity(3)
print(a4)

a5 = np.random.rand(3, 3)
print(a5)

a6 = np.random.randint(1, 10, [3,3])
print(a6)


# COMMAND ----------

a6 + a4
a6.size

# COMMAND ----------

a6_d = a6
print(a6)
print(a6_d)

a6_d[1,1] = 10

print(a6_d)
print(a6)

a6_c = a6.copy()
a6_c[1,1] = 20

print(a6_c)
print(a6)


# COMMAND ----------

a6_d = a6.view()
print(a6)
print(a6_d)
print("=" * 20)
a6_d[1,1] = 15

print(a6_d)
print(a6)
print("=" * 20)
a6[1,1] = 20

print(a6_d)
print(a6)


# COMMAND ----------

a7 = np.random.randint(1, 10, [3,3,3])
print(a7)

# COMMAND ----------

print(D1)

for item in D1:
  print(item)
  
print("=" * 20)
 
# for pm in a7:
#   for cm in pm:
#     for item in cm:
#       print(item)
      
for cm in a7[1,:]:
  for item in cm:
    print(item)
    
print(a7[1,1:2, 1:2])


# COMMAND ----------

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

arr2 = np.array([[4, 5, 6], [1, 2, 3]])

arr = np.concatenate((arr1, arr2))
print(arr)

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

# COMMAND ----------

arr1 = np.array([3, 2,  5,4,1, 6])
print(arr1)

arr2 = np.array_split(arr1,3)
print(arr2)

print(np.where(arr1 == 4))

print(np.sort(arr1))

print(arr1[arr1%2 == 1])

print(arr1[arr1 >=5])

# COMMAND ----------

# MAGIC %md 
# MAGIC # Task

# COMMAND ----------

output = np.array([
  [1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,10,0,1],
  [1,0,0,0,1],
  [1,1,1,1,1]
])
output

# COMMAND ----------

grid = np.ones([5,5])
# print(grid)
ch_grid = np.zeros([3,3])
# print(ch_grid)
ch_grid[1,1] = 10
# print(ch_grid)
grid[1:-1, 1:-1] = ch_grid
print(grid)
