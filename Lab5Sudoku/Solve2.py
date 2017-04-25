#!/usr/bin/env python
# -*- coding: utf-8 -*-
#File Details:Generator of sudokus base on level of difficulty.
#Lab5, Computer Programming IV
#feedback:hfjimenez@utp.edu.co
#Feature
#it must generate proper sudoku puzzles
#wide range of difficulties(easy,medium,hard,insane)
#it must use the strategy pattern to generate
#    License Details:
#    Copyright (C) 2017  Hector F. Jimenez S.
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; Applies version 2 of the License.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

#Information Resources :
#http://norvig.com/sudoku.html
#mathworks.com/company/newsletters/articles/solving-sudoku-with-matlab.html
from src.fancy import banner, menu, warning, green, reset, info
from src.generator import *
import os
from sys import exit
ok = "{}[✓]{}".format(green, reset)
def main():
    """
    Main of Sudoku puzzle Generator
    """
    menu()
    level=input('>> ')
    if level == '1':
       selectstrat = StrategyGenerator()
    elif level == '2':
        selectstrat= StrategyGenerator(executeMedium)
    elif level == '3':
        selectstrat= StrategyGenerator(executeInsane)
    else:
        print('{}Invalid Choice...Exiting'.format(warning))
        sys.exit()
    savefile=input('>> Name of the file to Save your generated puzzle: ')
    selectstrat.execute()

    #save the generated sudoku here !
    puzzle=selectstrat.puzzle          
    if not os.path.isfile(savefile):
        with open(savefile,'w') as f:
            f.write(str(puzzle))
            f.close()
        print('{}Data Saved'.format(ok))
    else :
        with open(savefile,'a') as f :
            f.write('\n'+str(puzzle))
            f.close()
        print('{}Data Saved'.format(ok))
    
    
    want=input('\n\n{}Want to solve this ?[Y/N]'.format(info))

    if want.lower()=='y':
        from  Solve1 import solver
        solver(puzzle)
    
if __name__ == '__main__':
    main()
