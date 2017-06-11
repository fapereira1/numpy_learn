import numpy as np

# Array
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Tensor
t = np.array([[[[1], [2]], [[3], [4]], [[5], [6]]], [[[7], [8]], \
                                                     [[9], [10]], [[11], [12]]],
              [[[13], [14]], [[15], [16]], [[17], [17]]]])

# Vector
v = np.array([1, 2, 3, 4])

x = v.reshape(1, 4)

print x.shape

# Python Way to add 5 to every item
values = [1, 2, 3, 4, 5]
for i in range(len(values)):
    values[i] += 5

print values

# The Numpy Way
values = [1, 2, 3, 4, 5]
values = np.array(values) + 5
print values

#####################################################################
# Element-wise Matrix Operations
#####################################################################

a = np.array([[1, 3], [5, 7]])

print "Array A"
print a
print a.shape

b = np.array([[2, 4], [6, 8]])

print "Array B"
print b
print b.shape

print a + b

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

c = np.matmul(a, b)
print c