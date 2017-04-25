# Computer Programming IV: Laboratory #5 

The idea behind this laboratory is create a new solver, because for me the observer pattern 
is ok and understable but I want to code my own solver I've never code a puzzle like this one
so I would like to adapt it to the strategy pattern in Python, in the end this is the homework.

## Considerations
If I start considering the problems and requirements to create a sudoku puzzle generator and solver

My requirements are:
 - My generator needs to be able to generate proper sudoku puzzle,there must be at least 
 one valid solution to complete the sudoku. 
 - Off course I want to have different levels of difficulty,because everybody is different 
 - I have to implement the strategy pattern according to the proffesor requirements. 
 - I have to create code in different files. 

Considering the posible methods to solve it :
 - Brute Force Method , Backtracking 
 - Constraints Satisfaction and search[1](http://norvig.com/sudoku)

The first one is a little expensive and ineficient, because it needs to try all the possible solutions
until it reached the correct solution, if not try with another number, meanwhile with Constraints satisfaction 
we just need to solve the constraints in this case our variables are 81 squares, the domain are the numbers in 
the range [1...9], and the constrainst are three only one occurence of a number in each row,column, and a unit. 

## Strategy Pattern
According to wikipedia, this design pattern is widely use when we have multiple options to do an action, 
that's it, for this sudoku generator we want to create a class with a default method **execute()** that 
is able to create easy, medium and insane puzzle.

The insane puzzles are generated using pregenerated puzzles, they're part of the top95. The following python code will overwrite the behavior of the **execute()** function, this pattern can also be used when we have serializer, it doesn't matter what protocol do you use, because there're many options to do actions.
```python
#Sample of strategypattern
class StrategyGenerator:
    def __init__(self, func=None):
        if func:
             self.execute = func

    def execute(self):
        print("Creating an Easy One Challenge")
        
def executeMedium():
	print("Creating an Medium One Challenge")
  
def executeInsane():
    print("Creating an insane sudoku")

if __name__ == "__main__":
    choice=input("?")
    if choice== '1':
        strat0 = StrategyGenerator()
    elif choice== '2':
        strat0 = StrategyGenerator(executeMedium)
    elif choice == '3' :
        strat0 = StrategyGenerator(executeInsane)
    else:
        strat0 = StrategyGenerator()
    x=strat0.execute()
    print(x)
``` 




