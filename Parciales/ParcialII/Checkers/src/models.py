#!/usr/bin/env pythongit ad
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
class BoardStorage(object):
    """
    Represent the states of Checkers board
    """
    def __init__(self):
        """
        Default initializator to create all the machines
        """
        self.array = []     
        self.size = 8
        self.machinePieces = 0
        self.playerPieces = 0
        for i in range (self.size):
            self.array.append([])
            for j in range (self.size):
                self.array[i].append(None)
        self.showgrid()#debug

    def showgrid(self):
        """
        Show your DS representation in the console.debug
        """
        print('::Board State::')
        for row in range(8):
            for col in range(8):
                print("{}|".format(self.array[row][col]), end=' ')
            print("\n{}".format(' '.join(12 * '*')))

    def addPiece(self,owner,type,x,y):
        piece = Piece()
        piece.setValues(owner,type)
        if self.array[int(x)][int(y)] == None:
            if piece.getOwner()== "M" and (piece.getType() == 1 or piece.getType() == 0):
                self.array[int(x)][int(y)] = piece
                self.machinePieces+=1
                return True
            elif piece.getOwner()== "Player" and (piece.getType() == 1 or piece.getType() == 0):
                self.array[int(x)][int(y)] = piece   
                self.playerPieces+=1
                return True
        else:
            return False


    def countMachinePieces(self):
        return self.machinePieces

    
    def countPlayerPieces(self):
        return self.playerPieces

    
    def pieceAt(self,x,y):
        """
        Esta la ficha en la posicion x,y, retornemos True or False.
        """    
        fichita = self.array[int(x)][int(y)]
        if fichita != None:
            return True
        else:
            return False

    def removePiece(self,x,y): 
        """
        returns the piece from the array given at position x and y 
        and sets that array position to none
        number of pieces - 1 
        """
        if self.pieceAt(x,y) :
            tmp = self.getPieceAt(x,y)
            self.array[int(x)][int(y)] = None
            if tmp.getOwner() == "M":
                self.machinePieces-=1
            elif tmp.getOwner() == "Player":
                self.playerPieces-=1
            return tmp
        
    def updatePieceType(self,type,x,y):
        tmpF = self.removePiece(x, y)
        if tmpF:
            self.addPiece(tmpF.getOwner(), type, x, y)
            return True
        else:
            return False
        
    def getPieceAt(self,x,y):
        """
        Returns the piece at array X,Y if the piece exits there
        """    
        if self.pieceAt(x, y):
            return self.array[int(x)][int(y)]
        
    # returns size
    def getSize(self):
        return self.size
    
    
    def movePiece(self,x,y,x1,y1):
        """ 
        move piece takes current piece position at X, Y and moves it to X1, Y1
        removes Piece at X and Y in the array and adds it back at position X1, Y1
        """
        tmp = self.removePiece(x, y)
        if tmp:
            self.addPiece(tmp.getOwner(), tmp.getType(), x1, y1)
            return True
        else:
            return False

class Piece(object):
    """
    Creates a Piece Object
    type, and owner. With the owner I identified the color.
    For this Game I've done the development mostly with machine vs player. 
    player vs player will be the last
    """
    def __init__(self):
        self.type = 0
        self.owner = ""

    def setValues(self,owner,type):
        self.type = type
        self.owner = owner
    
    def getType(self):
        return self.type
    
    def getOwner(self):
        """
        Who is the owner of the piece?
        return owner value.
        """
        return self.owner

    def getInfo(self):
        """
        Returns the owner and type of piece
        """
        print("Owner = {}".format(self.owner))
        print("Type = {}".format(self.type))