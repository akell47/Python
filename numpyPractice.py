import numpy as np

zero_vector = np.zeros(5)
print (zero_vector)
zero_matrix = np.zeros((5,3))
print (zero_matrix)

x = np.array([1,2,3])
print (x)
y = np.array([2,4,6])
print (y)

c = np.array([[1,3], [5,9]])
print (c)

print (c.transpose())

print ("-----")

q = np.array([[3,6], [5,7]])
u = q.transpose()
print (u)

x1  = np.array([1,2,3])
y1 = np.array([2,4,6])
X1 = np.array([[1,2,3], [4,5,6]])
Y1 = np.array([[2,4,6], [8,10,12]])

print (x1[2])
print (x1[0:2])
z1 = x1 + y1
print (z1)

print (X1[:, 0])

B1 = X1[:, 1] + Y1[:, 1]
print (B1)

C1 = X1[1, :] + Y1[1, :]
print (C1)

np.array([2,4]) + np.array([6,7])

print ("------")

t = np.array([1,2,5])
print (t[1:2])

# a1 = np.array([1,2])
# b1 = np.array([3,4,5])
# print (a1 + b1)

z1 = np.array([1,3,5,7,9])
z2 = z1 + 1
print (z1)
print (z2)

ind = [0,2,3]

print (z1[ind])

print (z1 > 6)

print (z1[z1 > 6])
print (z2[z1 > 6])

w = z1[0:3]
print (w)

w[0] = 3
print (w)

print (z1)

ind = np.array([0,1,2])

w1 = z1[ind]
print (w1)

aa = np.array([1,2])
bb = np.array([3,4,5])

print (bb[aa])

cc = bb[1:]
print (bb[aa] is cc)

print (np.linspace(0, 100, 10))

print (np.logspace(1, 2, 10))

X_log = (np.logspace(np.log10(250), np.log10(500), 10))
print (X_log)
print (X_log.shape)
print (X_log.size)

R = np.random.random(10)
print (R)
print (np.any(R > 0.9))
print (np.all(R >= 0.1))

x_a = 20
print (not np.any([x_a %i == 0 for i in range(2,x_a)]))
