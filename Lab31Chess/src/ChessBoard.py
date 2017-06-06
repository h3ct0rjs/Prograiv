import math
import pygame
import os
from src.Piece import *
from src.helpers import *

alphaValueOffset = 65;
boardfix = [
    ["┌","┬","┐"],
    ["├","┼","┤"],
    ["└","┴","┘"],
];

class ChessBoard:
    board = [None]*(8*8);
    currentTeam = 0;
    background = pygame.image.load("./img/chessbg.png");
    winner = -1;
    lastPiece = None;
    #threatField brukes for å finne ut om 
    #brikker ved forkjellige felter er truet
    
    def __init__(self):
        #Setter alle feltene til None;
        self.board = [None]*(8*8);
        self.winner = -1;
        self.lastPiece = None;
        self.currentTeam = 0;
        pass;
        
    def testBoard(self):
        #Setter brettet til et test brett
        self.board[0:7] = [Rook(self,(0,0),0),Knight(self,(1,0),0),Bishop(self,(2,0),0),Queen(self,(3,0),0),
                           King(self,(4,0),0),Bishop(self,(5,0),0),Knight(self,(6,0),0),Rook(self,(7,0),0)];
        self.board[8:15] = [Pawn(self,(i,1),0) for i in range(8)];
        self.board[pos2index((1,3))] = Pawn(self,(1,3),1);
        self.board[pos2index((3,3))] = Queen(self,(3,3),1);
        pass;
        
    def regularBoard(self):
        #Setter brette opp for et klassisk spill
        self.board[0:7] = [Rook(self,(0,0),0),Knight(self,(1,0),0),Bishop(self,(2,0),0),Queen(self,(3,0),0),
                           King(self,(4,0),0),Bishop(self,(5,0),0),Knight(self,(6,0),0),Rook(self,(7,0),0)];
        self.board[8:15] = [Pawn(self,(i,1),0) for i in range(8)];
        
        self.board[pos2index((0,7))-1:pos2index((7,7))-1] = [Rook(self,(0,7),1),Knight(self,(1,7),1),Bishop(self,(2,7),1),Queen(self,(3,7),1),
                           King(self,(4,7),1),Bishop(self,(5,7),1),Knight(self,(6,7),1),Rook(self,(7,7),1)];
        self.board[pos2index((0,6)):pos2index((7,6))] = [Pawn(self,(i,6),1) for i in range(8)];
        
    
    def castelingTestBoard(self):
        self.board[0:7] = [Rook(self,(0,0),0),None,None,None,
                           King(self,(4,0),0),None,None,Rook(self,(7,0),0)];
        self.board[pos2index((0,7)):pos2index((7,7))-1] = [Rook(self,(0,7),1),None,None,None,
                           Queen(self,(4,7),1),None,None,Rook(self,(7,7),1)];

    def updateAll(self):
        for i in self.board:
            if(i):
                i.update();
                
    def afterUpdate(self):
        for i in self.board:
            if(i):
                i.afterUpdate();
    
    def setBoard(self,board):
        #Setter brettet til board
        for i,v in enumerate(board):
            board[i] = v;
    
    def move(self,pos1,pos2):
        #Flytter brikke på posisjon 1 til posisjon 2
        if not(pos1 == pos2 and self.winner == -1):
            try:
                b1 = self.board[pos2index(pos1)];
                if(b1 and (b1.team == self.currentTeam or b1.team == -1)):
                    if(b1.moveTo(pos2)[0]):
                        if(self.lastPiece):
                            self.lastPiece.hadLastMove = False;
                        self.lastPiece = b1;
                        b1.hadLastMove = True;
                        self.currentTeam = (self.currentTeam + 1)%2;
                        self.updateAll();
                        self.updateAll();
                        self.afterUpdate();
                        if(self.winner != -1):
                            print("Game over!");
                            if(self.winner < 2):
                                print("The winner is {}".format(("white","black")[self.winner]));
                            else:
                                print("The game was a draw");
                        
                        return True;
                    else:
                        return False;
            except IndexError:
                return False;
        
    def setPieceAt(self,pos,Piece):
        #Setter feltverdien til en brikker
        self.board[pos2index(pos)] = Piece;
        
    def swapPieces(self,pos1,pos2):
        #Bytter om plassene til to brikker
        self.board[pos2index(pos1)],self.board[pos2index(pos2)] = self.board[pos2index(pos2)],self.board[pos2index(pos1)];
        
    def getPieceAt(self,pos):
        #Returnerer brikken i feltet
        return self.board[pos2index(pos)];
    
    def firstEncounter(self,pos,pos2,maxOcc=1):
        #Finner det første felted der en annen brikke er
        diffX = -pos[0]+pos2[0];
        diffY = -pos[1]+pos2[1];
        cPos = pos;
        first = True;
        
        for i in self.raycast(pos,pos2,maxOcc):
            if(self.getPieceAt(i)):
                return i;
      
    def threatenedBy(self,pos,team,semi=False):
        t = [];
        for i in self.board:
            if(i and i.team != team):
                if(semi and pos in i.semiThreat):
                    t += [i];
                elif(pos in i.threat):
                    t += [i];
        return t;
        
    def isThreatend(self,pos,team,semi=False):
        #Uoptimalisert måte å sjekke om et felt er truet
        for i in self.board:
            if(i and i.team != team):
                if(semi and pos in i.semiThreat):
                    return True;
                if(pos in i.threat):
                    return True;
                
        return False;
    def raycast(self,pos,pos2,maxocc = 1):
        #Returnerer alle cellene fra pos til pos2
        diffX = -pos[0]+pos2[0];
        diffY = -pos[1]+pos2[1];
        cPos = pos;
        cells = [];
        first = True;
        
        
        try:
            inc = diffY/diffX;
        except ZeroDivisionError:
            inc = "inf";
        
        for i in range(8):
            if(not first and self.getPieceAt((int(cPos[0]),int(cPos[1])))):
                maxocc-=1;

            if(cPos == pos2 or maxocc<=0):
                return cells;
            cPos = (cPos[0]+ (0 if inc == "inf" else math.copysign(1,diffX)),cPos[1] + (math.copysign(1,diffY) if inc=="inf" else inc*math.copysign(1,diffX)));
            if(not (cPos[0] < 0 or cPos[0] > 7 or cPos[1] < 0 or cPos[1] > 7)):
                cells.append((int(cPos[0]),int(cPos[1])));    
            else:
                return cells;
                    
            first = False;
        
    def renderBG(self,surface):
        surface.blit(self.background,(0,0),(0,0,360,360));
    
    def renderPieces(self,surface):
        for i in self.board:
            if(i):
                i.render(surface);
    
    def __str__(self):
        o = "   ";
        for i in range(8):
            o += " " + str(chr(i+alphaValueOffset));
        o+="\n";
        r=0;
        c=0;
        for i in range(8):
            o+= " "*3; 
            for j in range(8):
                r = math.ceil(i/8);
                c = math.ceil(j/8);
                o += boardfix[r][c] + "─";
            o+=boardfix[r][2] + "\n";
            o+=str(i+1) + " "*(2-(len(str(i+1))-1));
            for j in range(8):
                o+="|"+ (str(self.board[j + i*8] or " "));
            o+="|\n";
        o+= "   ";
        for j in range(8):
            c = math.ceil(j/8);
            o += boardfix[2][c] + "─";
        o+=boardfix[2][2] + "\n";
        return o;