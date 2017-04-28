## Simulating Randomness

Randomness, or apparent randomness occurs almost everywhere, from motions of microscopic molecules to electoral candidates.  In addition to phenomena that are genuinely random, randomness is often used when modeling complicated systems to abstract away those aspects of the phenomenon for which we do not have useful simple models. We can model parts of a process that can be explained in relatively simple terms, and we assume, true or not that the rest is noise. Model what we can and whatever is left out is attributed to randomness.  That is why it is important to recognize, understand, and simulate random numbers and random processes. With Python there is the
`random` module and other processes to generate random numbers. <br/>

`print (random.choice(range(1,7)))`
Random number between 1 and 6, like a dice.
<br/>

Three Random dice
* one has 6 sides
* one has 8 sides
* one has 10 sides

`print (random.choice(random.choice([range(1,7), range(1,9), range(1,11)])))`
randomly rolls one of the three dice. Everything is an object in Python. The innermost random choice first chooses one object from a sequence. The outermost random choice chooses on of the numbers from the given range object.
<br/><br/><br/>
`print (random.choice(random.choice([range(1,7), range(1,9), range(1,11)])))`
sums random integers from 0 to 9 <br/>
`print (sum(random.sample(range(10),10)))` makes a random list of numbers between 0-9 - so sum is always 45.  <br/><br/>
