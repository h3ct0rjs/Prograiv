#!/usr/bin/env python
# -*- coding: utf-8 -*-
#File Details: Generate valid Sudoku Puzzles.
#Lab5, Computer Programming IV
#feedback:hfjimenez@utp.edu.co
#Class to implement the strategy Pattern.
#More Information about this pattern:
#http://www.laurencegellert.com/2011/08/python-strategy-pattern/
#Version 2 can handle object attributes
import sys
import types
from Solve1 import solver

if sys.version_info[0] > 2:  # Is Python 3+
    create_bound_method = types.MethodType
else:
    def create_bound_method(func, obj):
        return types.MethodType(func, obj, obj.__class__)

class StrategyGenerator:
    """
    Generate a Sudoku puzzle using the strategy generator.

    This class will return an object of type str, according to 
    the input level. Levels need to be validated outside of this 
    class.
    """
    def __init__(self, func=None):
        self.level = '0'
        self.name = "Default Strategy Generator:Easy"
        self.puzzle = "...............223132"
        if func:
            self.execute = create_bound_method(func, self)
            #self.execute=func

    def execute(self):
        self.level='1'
        print('Enter to Defautl Exec')

    def __str__(self):
        return("Sudoku Generator Level:{}".format(self.level))
    def __str__(self):
        N = 9
        
        str = '+---------+---------+---------+\n'
        for i in range(N):
            str += '|'
            for j in range(N):
                value = self.cells[i][j].get_value()
                str += ' {} '.format(value if value != 0 else '.')
                if (j + 1) % 3 == 0:
                    str += '|'
            str += '\n'
            if (i + 1) % 3 == 0:
                str += '+---------+---------+---------+\n'
        str += '\n' + self.candidates()

        return str
    

def executeMedium(self):
    self.level = '2'
    self.name = "Strategy Generator:Medium"
    self.puzzle = "...............MID"
    #print(self.name + " from Medium")


def executeInsane(self):
    self.level = '4'
    self.name = "Strategy Generator:Insane"
    self.puzzle = ".........INSANE......000"
    #print(self.name + " from Insane")
