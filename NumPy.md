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
`a = np.array([[1,3], [5,9]])` - nested list inside pf parentheses
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
