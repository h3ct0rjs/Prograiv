#This was the easy, I just solve this problem, in c++ for permutations I need to do this using next_permutation.

from itertools import  permutations
def solve(n):
    cols=(range(n))
    for vec in permutations(cols):
        if(n == len(set(vec[i]+i for i in cols)) == len(set(vec[i]-i for i in cols))):
            print map(lambda x:x+1, vec) #from here we can use this to plot it in pygame. 
