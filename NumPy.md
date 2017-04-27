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
