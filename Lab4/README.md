### Sieve of Erastotenes implementing Iterators

The professor Angel give us a class about the iterator pattern, he explain the ´´__iter__ and next()´´ magic method in Python, the assigment was to implement a sieve of erastotenes using 
the iterator pattern, for the most part of this assigment I use the awesome tutorial of [Norman Matloff](https://www.csee.umbc.edu/courses/331/fall13/03/PyIterGen.pdf). 

We need to understand that iterators can be use over collections in containers like list,tuples, dictionaries and other similar or derive, the thing is that iterator produce a sequence step by step and not iterate over the sequence to produce all the sequence, the items are produced at a time and this can be an infinite long sequence.

```python 
def intsfrom(i):
#   generator   for ints    >=  I   
    while   True:
        yield   i
        i+=  1   

def nextn(g,    n): 
    #next    n   items   in  generator   g
    return  [g.next()   for i   in  xrange(n)] 

def remove(n,   g):
    # remove  mul7ples    of  n
    for x   in  g:
        if  x   %   n:
            yield   x

def sieve(ints):
# generator   for primes
    p   =   ints.next() 
    yield   p
    for p   in  sieve(remove(p, ints)): 
        yield   p

def main():
    primes = sieve(intsfrom(2))
    while   True:
        print   "Next   10  primes" 
        print   nextn(primes,   10) 
        input('--more-- ')
if __name__ == "__main__":
    main()
```
From the code above we can see that we use a generator to that keeps the variable i increasing in steps of one, and the next function is use to indicate that we want next value..