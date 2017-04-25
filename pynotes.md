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
s = [4,3,2,6]
s[0] = 4
s[-1] = 6
```
**Slicing**
```
s[2] = 2
s[0:2] = 4,3,2 s[start, stop]
s[-0] = 1
s[-0:0] = ()
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
(c1, c2) = coordinate`
tuples in for loops - lists of tuples, each tuple consists of two numbers
```
for (x,y) in coordinate
  print (x , y)
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

## Ranges

* `range(#)` - immutable sequence of integers - commonly used in for loops.
```
list(range(5))
[0,1,2,3,4]
```
`range(start, step, size)`
```
range(1,14,2)
[1, 3, 5, 7, 9, 11, 13]
```
large data - first list - uses up space. Use range objects as is don't turn to lists right away. Ranges do not instantiate their elements, making them more efficient in loops.

## Strings

``''`` or ``" "`` or ``''' '''``
* strings - immutable sequences of characters. a concatenation of characters.

```
s = '''python'''
len(s)
6
s[::-1]
nohtyp
```
**polymorphism**
- what an operator does depends on the type of objects that it is being applied to. have to define addition separately for numbers. add with `+`.
- dir(str) all the help on strings
```
"hi" + str(2)
hi2
```

```
name = "Amber"
name_a = name.replace("A", "a")
# must assign to new variable because strings are immutable
```
```
type(name)
str

name_s = name.split()
type(name_s)
list
```
`"12,000".isdigit()` False

## Sets

`(value3,value4,value6,value2)`

* Sets - unordered collection of distinct hashable objects
**hashable** - can use sets for immutable ojbects <br/>

**Sets**
* a set - mutable
* a frozen set - immutable
- cannot be indexed
- can never be duplicated, unique
Sets useful for keeping track distinct objects and doing operations like unions, intersection, and set differences.
https://docs.python.org/2/library/sets.html

## Dictionaries

`{ "Key" : value }`
* Dictionaries - mapping from key objects to value objects
keys must be immutable values can be anything
- can be used for fast lookups
- do not maintain order. - looping occurs over random order

## Dynamic Typing

Type - computer memory - sequence of 0s and 1s.  Read sequences in chunk of bits. What type? one variable to another no match loose information. float to int - ok. int gets float info lost. <br/>
Statically typed - C, C++ - type checking is preforming during compiling time  <br/>
dynamically typed - python - type checking is preformed during run time <br/>
* variable
* object
* reference
`x = 3` py creats objects 3 variable name x and assignment <br/>
variable names and objects stored in different parts of computer memory. Variable names link to objects, never to other variables. Variable = reference to the object.

* two variable names can represent the same object!
another name for the same list
```
List1 = [2,3,4]
List2 = List1
List1[0] = 20
List2
[20,3,4]
#you thought you had two lists, but just two variable names representing the same list object
```
mutable objects can be identical in content, but different in objects.
```
a = [1,2,3]
b = [1,2,3]
a == b
True
a is b
False
```
`a = list(b)` creates a new object but with identical content.
`a = b[:]` same thing

## Copies

`import copy` copy module - for creating identical copies of an object
* Shallow Copy - constructs a new compound object - only references the objects in the copied objects
* Deep Copy - constructs a new compound object and then recursively inserts copies into it of the original objects

## Statements

**statements** - used to compute values, assign values, modify attributes, etc.
* Return - return values from a function
* Import - import modules
* Pass - do nothing - place holder -

**Compound Statements** - contain groups of other statements and control the execution of other statements in some other way. Consists of one or more **clauses** - consists of header and a block of code. **header** - `keyword:` start with keyword and end in **:**- all at same indention level. - indented at the same level - form a group of statements. - indentation determines logical structure of functions/ programs.
```
#header
if x > y:
#block of code
  difference = x - y
  print ("x is greater than y")
print ("always printed")
```
```
if test:
  [block of code]
elif test:
  [block of code]
else:
  [block of code]
```

## For and While Loops

**For Loops** sequence iteration that assigns items in sequence and runs the block of code for each item. - run as many times as there are items in the sequence. `for target in sequence` - starts at index 0 then runs the block of code.

```
dictionary = {"aa":1, "bb":2, "cc":3, "dd":4}
for k in dictionary:
  print k
aa
cc
dd
bb

for k in dictionary:
  print (k, dictionary[k])
('aa', 1)
('cc', 3)
('dd', 4)
('bb', 2)

for k in sorted(dictionary.keys(),reverse = True):
   print (k, age[k])
('dd', 4)
('cc', 3)
('bb', 2)
('aa', 1)

for v in dictionary:
  if
```

**While Loops** -repeated execution of code as long as given expression is true. - repeatedly texts the expression. If true - executes first block of code, if false - executes the second block of code if present

- while loop - testing some condition some number of times - don't know how many times exactly - unknown number of iterations.
- for loop - know exactly how many times you want to run the block of code. - set number of iterations

## List Comprehension

fast and elegant
can accomplish a lot in one line
https://github.com/akell47/Python/blob/master/listcomp.ipynb
```
numbers = range(10)
numbers
[0,1,2,3,4,5,6,7,8,9]
squares = [number ** 2 for number in numbers]
# given variable square variable - for loop assign value to number
squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
```
sum([i**2 for i in range(3)])
5
# range(3) is [0,1,2], i in range squared is [0,1,4], sum of that list is 5
```
sum odd numbers from 0 through 9
`sum( [i for i in range(10) if i%2 ==1] )` = 25

## Reading and Writing Files

say `linesoftext.txt` has three lines of text like:
```
first line
second line
third line
```
```
# open() creates file object
for line in open(filename):
# rstrip strips white space beween lines
  line = line.rstrip()
  print line
first line
second line
third line

for line in open(filename):
# .split() where there is a whitespace returns a list of each line
  line = line.rstrip().split(" ")
  print line
['first', 'line']
['second', 'line']
['third', 'line']
```

Make a file for Writing
`F = open(textfile.txt, "w")` <br/>
`F.write("some text here")` <br/>
`F.close()`

## Functions 101

devices for grouping statements so they can be easily run more than once in a program. - maximize code reuse and minimize redundancy. - enable dividing larger tasks into smaller chunks - called **procedural decomposition**. written using `def` statement. send the result object back to the caller using the `return` statement. all names created or assigned in a function are local of that function and exist only while the function runs. To modify the value of a global variable from inside a function can use **global** statement. function is called using the function name followed by `()`. the **def** statement creates an object and assigns it to a name. Arguments are passed by assigning objects to local names.

```
def add(x,y)
  mysum = x + y
  return mysum

add(40, 60)
100
```
can use tuples to return multiple values from a function
```
def add_sub(a, b):
  sumit = a + b
  diffit = a - b
  return (sumit, difit)

add_sub(40, 60)
(100, -20)
```
```
def password(length):
    pw = str()
    char = "abcdefghijklmnopqrstuvwzyz" + "0123456789"
    for i in range(length):
        pw = pw + random.choice(char)
    return pw

print "password of 9 characters is :",password(30)
```
returns `gb8lwo92vsdpgcu02izegysny43e4s` for example

## Commmon Mistakes and Errors

- `list index out of range` - indexing longer than how long the sequence is
- Dictionaries are unordered- key values appear in any order
- trying an operation not supported by the object - know the type of object you are working with and the methods that object supports
- trying to access an object in the wrong way. `KeyError 1`
keys are not numbers, but strings. know the type of the key objects
- trying to modify immutable Objects
- trying to operate on objects of different type - str and int -
- improper indentation -

## Scope and Rules

- each variable name belongs to a certain abstract environment or namespace - context in which a given name exists.
- *Scope Rules*
inner layers to outer layers - first one that it finds

- *L* Local
- *E* Enclosing function
- *G* Global
- *B* Built-In 
