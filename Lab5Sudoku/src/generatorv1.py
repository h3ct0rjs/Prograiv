#-*-coding:utf-8 -*-
import os
#Class to implement the strategy Pattern.
#More Information about this pattern:
#http://www.laurencegellert.com/2011/08/python-strategy-pattern/

#This class is not able to handle the class Attributes as is intended.
class StrategyGenerator:
    def __init__(self, func=None):
        if func:
             self.execute = func

    def execute(self):
        print("Default level Challenge Easy One Challenge")
        return 1

    def __str__(self):
        return "Generator of lvl : {} and format : {}".format(self.level,self.format)

def executeMedium():
    print("Medium")
    return 1 

def executeHardcore():
    print("HardCore Sudoku Challenge")
    #return medium chall 
    return 1

def executeInsane():
    print("Insane Sudoku Choosen")
    #This will generate insane sudo, from the top95 most insane, backup plan
    """data = []
                with open('top95.txt','r') as f:
                    data.append(f.readlines())
                    f.close()
                return data[0][randint(1,95)].strip('\n')"""

