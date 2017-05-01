#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Details:models.py, store all the states of the game
# ParcialII, Computer Programming IV
# feedback:hfjimenez@utp.edu.co,dcquiroz@utp.edu.co
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


class Token(object):
    """Class for the piece representation in the board"""

    def __init__(self, color):
        self.color = color
        self.form = 'default.png'

    def __str__(self):
        return str(self.color)


class TokenKing(Token):
    """class King Piece"""

    def __init__(self, arg):
        super(Token, self).__init__()
        self.king = True
        self.form = 'king.png'


class BoardStorage(object):
    """Represent the states of the current Checkers board"""

    def __init__(self):
        """Create the  datastructure to represent the real grid"""
        self.logm = {}
        self.idmvmt = 0
        self.grid = [['0'] * 8 for _ in range(8)]
        self.grid[0] = ['0' if i % 2 == 0 else '1' for i in range(8)]
        self.grid[1] = grid[0][::-1]
        self.grid[2] = self.grid[0]
        self.grid[6] = ['0' if i % 2 == 0 else '2' for i in range(8)]
        self.grid[5] = grid[6][::-1]
        self.grid[7] = grid[6][::-1]
        for row in range(8):
            for col in range(8):
                if self.grid[row][col] == 1:
                    self.grid[row][col] = Token('Black')
                elif self.grid[row][col] == 2:
                    self.grid[row][col] = Token('White')

    def showgrid(self):
        """Show your ds representation in the console.Debugging options """
        for row in range(8):
            for col in range(8):
                print("{}|".format(self.grid[row][col]), end=' ')
            print("\n{}".format(' '.join(12 * '*')))

    def updategrid(self, grid):
        self.grid = grid

    def LogMovements(self, movement, player):
        """Logger for player movements"""
        self.logm[self.idmvmt] = str(player.color) + ' ' + movement
        self.idmvmt += 1

    def getLogMovements(self):
        for j in range(len(self.logm)):
            print("{} : {}".format(j, self.logm[j]))
