# NumPy

`import numpy as np`
module for scientific computation. Tools for integrating code with existing C, C++, and Fortran code. Tools to help preform linear algebra, generate random numbers and way more. numpy.org

------------------

## NumPy Arrays

NumPy arrays are an additional data type provided by NumPy. -used for representing vectors and matrices. -have a size that is fixed when constructed.
Elements are all of the same data-type - floating point numbers.

```
zero_vector = np.zeros(5)
print (zero_vector)
```
prints `[0. 0. 0. 0. 0.]`
```
zero_matrix = np.zeros((5,3))
print (zero_matrix)
```
prints
```
[[ 0.  0.  0.]
 [ 0.  0.  0.]
 [ 0.  0.  0.]
 [ 0.  0.  0.]
 [ 0.  0.  0.]]
```
`np.array` create an empty array. Allocates the requested space for the array but does not initialize it. <br/>
When you construct a numpy array - elements of each row is a list then define the entire table as a list that contains at its elements each of the lists of the row elements you've defined. <br/>
`a = np.array([[1,3], [5,9]])` - nested list inside of parentheses
```
print (a)
[[1 3]
 [5 9]]

print (a.transpose())
[[1 5]
 [3 9]]
```

## Slicing

Remember position starts at 0. First index is row second is the column.
Start is included but stop is not. Can three or four dimensional array. Can use `:` in place of a fixed value for an index - the array elements corresponding to all values of that particular index will be returned.

`X = np.array([[1,2,3], [4,5,6]])` <br/>
`print (X[:, 1])` returns all rows for the second column, in this case: `[2 5]`

`Y = np.array([[2,4,6], [8,10,12]])` <br/>
```
B = X[:, 1] + Y[:, 1]
print (B)
[6 15]
```
Adds together the second two columns of the two arrays <br/>
```
C = X[1, :] + Y[1, :]
print (C)
[12, 15, 18]
```
Adds together the second rows of the two arrays. `X[1] + Y[1]` is the same thing (shorthand) <br/>
`[2,4] + [6,8]` --> `[2,4,6,8]` Two lists are concatenated with +, but
`np.array([2,4]) + np.array([6,8])` --> `array([8,12])`

## Indexing

NumPy arrays can be indexed with other arrays. <br/>

```
z1 = np.array([1,3,5,7,9])
z2 = z1 + 1

ind = [0,2,3]

print (z1[ind])
```
prints `[1 5 7]` using ind as the index. <br/>

NumPy array can also be indexed using logical indices. Can have an array consisting of true and false (Boolean elements)
`print (z1 > 6)` ---> `[False False False True True]` Cal use the Boolean array aka logical array to index another vector.
`print (z1[z1 > 6])` ---> `[7 9]` <br/>
Note* When you **slice** an array using the color operator you get a view of the object, meaning that if you modify it, the original array will also be modified.  When you **index** an array you get a copy of the original data.
- slice = view
- index = copy

## Building and Examining NumPy Arrays

Ways to construct arrays with fixed start, and end variables, so that the other elements are uniformly spaced between them.  <br/>
`np.linspace()`  

```
print (np.linspace(0, 100, 10))
#creates 10 evenly spaced numbers from 0 to 100
[   0.           11.11111111   22.22222222   33.33333333   44.44444444
   55.55555556   66.66666667   77.77777778   88.88888889  100.        ]
print (np.logspace(1, 2, 10))
#creates 10 numbers from 10 to 100. log of 10 is 1 and log of 100 is 2
[  10.           12.91549665   16.68100537   21.5443469    27.82559402
   35.93813664   46.41588834   59.94842503   77.42636827  100.        ]
```
`.shape` number of columns and rows `.size` number of elements
size and shape are attributes not methods of the arrays
```
R = np.random.random(10)
print (np.any(R > 0.9)) --> sometimes True, sometimes False
print (np.all(R >= 0.1)) --> sometimes True, sometimes False
```
