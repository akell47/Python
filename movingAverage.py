import random

def moving_window_average(values, n_neighbors=1):
    n = len(values)
    width = n_neighbors*2 + 1
    x = [values[0]]*n_neighbors + values + [values[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width
    # for all values i from 0 to n-1.
    newList = []
    for i, value in enumerate(x):
        windowValues = x[i:i+width]
        if len(windowValues) == width:
            avg = sum(windowValues)/float(width)
            newList.append(avg)

    return newList

x=[0,10,5,3,1,5]
# print "x:",x
# print "attempt",(moving_window_average(x))

#moving average helps show trends
# import numpy as np
# def movingaverage(values, window):
#     weights = np.repeat(1.0, window)/window
#     smas = np.convolve(values, weights, 'valid')
#     return smas
#
# print "answer",movingaverage(x,3)
#
#
# def running_mean(values, N):
#     sum = 0
#     result = list(0 for x in values)
#
#     for i in range(0, N):
#         sum = sum + values[i]
#         result[i] = sum/(i+1)
#
#     for i in range(N, len(values)):
#         sum = sum - values[i-N]+values[i]
#         result[i] = sum/N
#
#     return result
#
# print "running_mean",running_mean(x,3)
import random
R = 1000
def rand():
   return random.uniform(0, 1)

x = [rand() for num in range(R)]


Y = [x]+[moving_window_average(x,neighborCount) for neighborCount in range(1,10)]
print len(Y)


ranges = [max(list_x) - min(list_x) for list_x in Y]

print ranges
