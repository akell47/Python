
# coding: utf-8

# In[3]:

firstName = "Amber"


# In[4]:

lastName = "Keller"


# In[6]:

get_ipython().system(u'pip install numpy')


# In[7]:

randomNumbers = numpy


# In[8]:

randomNumbers = np.random.randint(0,100,5)


# In[9]:

type(randomNumbers)


# In[10]:

print randomNumbers


# In[11]:

import numpy as np


# In[12]:

randomNumber = np.random.randint(0,100,5)


# In[13]:

print randomNumber


# In[14]:

type randomNumber


# In[15]:

type(randomNumber)


# In[16]:

from numpy.random import randint


# In[17]:

randomNumbers2 = randint(0,100,5)


# In[18]:

print randomNumbers2


# In[19]:

import math


# In[20]:

print math.exp(0)


# In[25]:

def f(x,m):
    print m*x
    return m*x


# In[ ]:




# In[23]:

f(1,2)


# In[24]:

a = f(1,2)


# In[27]:

for x in range(5):


# In[28]:

for x in range(5):
    print f(x,2)


# In[ ]:




# In[29]:

randomNumbers2 = randint(0,100,20)


# In[30]:

print 5/2


# In[31]:

print float(5)/2


# In[32]:

print 5/2.


# In[33]:

print 5/float(2)


# In[34]:

5 % 2


# In[35]:

randomNumbers2 = randint(0,100,20)


# In[36]:

def getEvenNums(set1):


# In[38]:

def getEvenNums(set1):
    evenNums = []
    for num in set1:
        if num % 2 == 0:
            evenNums.append(num)
    events = len(evenNums)
    total = len(set1)
    return (float(events)/total)*100
    
getEvenNums(randomNumbers2)


# In[41]:

a = [1,2,3,4]
for i in range(0,len(a)):
    a[i] =a[i]*2


# In[42]:

print a


# In[43]:

b = [1,2,3,4]
newList = []
for num in b:
    newList.append(num*2)


# In[44]:

print newList


# In[45]:

newList1 = map(lambda num: num*2, b)


# In[46]:

newList1


# In[47]:

def f(x): return x*2
newList2 = map(f,b)
print newList2


# In[48]:

evenNums = filter(lambda num: num % 2 ==0, randomNumbers2)
print evenNums


# In[49]:

a


# In[51]:

def checkforEven(num): return num % 2 == 0
evenNums = filter(checkforEven, randomNumbers2)
print evenNums


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



