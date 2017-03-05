## Objects
data in python is represented by objects and relationships between Objects
* mutable - values can change
* immutable - values cannot be changed
bulk of python library consists of models that you import
* object type - number, string, list
* object values - data value contained by the object
* object identity - identity number for the object - each distinct object in the computer's memory will have its own ID number

**Attributes:**
* data
* functions
* both
<br/>
* data Attributes
* method - preforms function on object
* instance - occurance of an object

## Modules an Methods
libaries of code you can import. <br/>
`import math`

* namespace - container of names shared by objects tat typically go together. to prevent naming conflicts

python executes code with in the created namespace. Example np executes code with in the numpy namespace
`np.bla` vs `math.bla`

`help(name.upper)` name.upper is a function bound to name objects
VS `help(name.upper())` wrong -

## Numbers and Basic Calculations

* Integers - unlimited precision
* Floating Point Numbers
* Complex Numbers

- Can freely mix numeric types

## Factorial
n! = n * (n-1)....2*1
3! = 3*2*1 = 6

`import math`
`math.factorial(#)`

## Random Choice

`import random` - have a set of numbers in a list and want to select from those numbers uniformly at random - for example

## Expressions and Booleans

* Boolean - True and False
* Boolean Operations - take in one or more boolean object and return object back
**Three Operations**
* or
* and
* not
* `True or False` -  `True`
* `True and True` - `True`
* `True and False` - `False`
* `not True` - `False`
* `not False` - `True`
* `==`
* `!=`
`[2,3] == [2,3]` - `True`
`[2,3] is [2,3]` - `False` - have same contents but have two objects - that's why return False
* `==` tests whether objects have the same value
* `is` tests whether objects have the same identity
`[2,3] is not [2,3]` - `True`

## Sequence Types and Sequence Operations

* sequence - a collection of objects ordered by their position <br/>
**Three Types**
* Lists
* Tuples
* 'Range Objects'

indexing starts a 0
```
`s = [4,3,2,6]`
`s[0] = 4`
`s[-1] = 6`
```
**Slicing**
```
`s[2] = 2`
`s[0:2] = 4,3,2` s[start, stop]
`s[-0] = 1`
`s[-0:0] = ()`
```

## Lists

* Lists - mutable sequences of objects of any type
One type of sequence like strings <br/>
lists are sequences of any type of Python objects <br/>
strings are sequences of individual characters
Lists - mutable, Strings immutable

## Tuples

* Tuples - immutable sequences
single object that consists of several different parts.
example - want to return more than one object from a function - typically wrap all of those objects in a tuple.

**Pack and un-pack tuples**
`x = 12.23` `y = 23.34`
`coordinate = (x,y)` - tuple packing
`(c1, c2) = coordinate`
tuples in for loops - lists of tuples, each tuple consists of two numbers
```
`for (x,y) in coordinate
  print (x , y)`
```
```
c = (2,3)
type(c)
tuple

c = (2)
type(c)
int

c = (2,)
type(c)
tuple
```
