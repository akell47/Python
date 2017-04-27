# def update(n, x):
#     n = 2
#     x.append(4)
#     print ('update', n, x)
#
# def main():
#     n = 1
#     x = [0,1,2,3]
#     print('main ', n, x)
#     update(n,x)
#     print('main :', n, x)
#
# main()
print '---------'
# def increment(n):
#     n += 1
#     print(n)
#
# n = 1
# increment(n)
# print(n)
print '---------'
# def increment(n):
#     n += 1
#     return n
#
# n = 1
# while n < 10:
#     n = increment(n)
# print(n)

ml = [5,9,3,6,8,11,4,3]

ml.sort()

print "ml:",ml
print "min",min(ml)
ml.remove(3)
print "ml remove 3",ml

class MyList(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))

x = [1,2,3,4,5,6,7,8,9]
print "x:",x
y = MyList(x)
print dir(x)
print dir(y)

y.remove_min()
print "y.remove_min",y
y.remove_max()
print "y.remove_min",y
