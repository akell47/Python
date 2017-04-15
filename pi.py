import math
print math.pi/4
print "----"

import random
def rand():
    return random.uniform(-1, 1)

print rand()
print "----"

p1 = (4,9)
p2 = (3,4)
print p1[0]
print p2[0]
print math.sqrt(26)
#The distance between two points x and y is the square root of the sum of squared
#differences along each dimension of x and y

def distance1(n,b):
    n1 = b[0] - n[0]
    b1 = b[1] - n[1]
    return math.sqrt((n1**2)+(b1**2))
#
print distance1(p1,p2)
print "----"


x = (0,0)
y = (1,1)

def distance(x, y):
    return math.sqrt( ((y[0]-x[0])**2) + ((y[1]-x[1])**2) )

print (distance(x,y))

origin = [0]*2
print origin

p3 = (0,.5)

def in_circleB(p, origin):
    return distance(p, origin) < 1

print in_circleB(p1, origin)
print in_circleB(p3, origin)
print "-----"

R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)

for point in x:
    inside.append(in_circleB(point, origin))
print inside.count(True)
CountT = float(inside.count(True))
CountT_R = CountT/R
print "----"

print math.pi/4
print CountT_R
diff = abs(CountT_R - (math.pi/4))
print diff
