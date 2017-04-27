import numpy as np

# zero_vector = np.zeros(5)
# print (zero_vector)
# zero_matrix = np.zeros((5,3))
# print (zero_matrix)
#
# x = np.array([1,2,3])
# print (x)
# y = np.array([2,4,6])
# print (y)
#
# c = np.array([[1,3], [5,9]])
# print (c)
#
# print (c.transpose())
#
# print ("-----")
#
# x = np.array([[3,6], [5,7]])
# y = x.transpose()
# print (y)

# x = np.array([1,2,3])
# y = np.array([2,4,6])
# X = np.array([[1,2,3], [4,5,6]])
# Y = np.array([[2,4,6], [8,10,12]])
#
# print (x[2])
# print (x[0:2])
# z = x + y
# print (z)
#
# print (X[:, 0])
#
# B = X[:, 1] + Y[:, 1]
# print (B)
#
# C = X[1, :] + Y[1, :]
# print (C)
#
# np.array([2,4]) + np.array([6,7])


# x = np.array([1,2,5])
# print (x[1:2])
#
# a = np.array([1,2])
# b = np.array([3,4,5])
# print (a + b)

z1 = np.array([1,3,5,7,9])
z2 = z1 + 1
print (z1)
print (z2)

ind = [0,2,3]

print (z1[ind])

print (z1 > 6)

print (z1[z1 > 6])
print (z2[z1 > 6])

# w = z1[0:3]
# print (w)

# w[0] = 3
# print (w)

print (z1)

ind = np.array([0,1,2])

w = z1[ind]
print (w)
