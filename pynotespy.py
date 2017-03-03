import numpy as np

x = np.array([1,3,5])
y = np.array([1,5,9])

print x.mean()
print y.mean()

print x.shape
print y.shape
# example of attributes
# no () means shape is a data attribute

import math

print math.pi

print math.sqrt(10)

print math.sin(math.pi/2)

from math import pi
# just imported pi from the Modules

import numpy as np

math.sqrt
np.sqrt

print math.sqrt(2)
print np.sqrt(2)
#different namespaces

print np.sqrt([2,3,4])
# cant do this with math import

name = "Amber"
print type(name)
# object is a string
print dir(name)
# prints list of methods available to the methods
