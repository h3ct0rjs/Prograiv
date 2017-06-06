#!/usr/bin/env python3
#-encoding:utf-8-*-
#hfjimenez@utp.edu.co
import math
import pygame
import os 

"""
"""
class Piece:
    """
    Class Piece: 
    Each Piece in the game will have different attributes,
        Position
        Team
        if the piece has moved
        the board
        Valid Moves 
        Threat Is in risk of dead.
    """
    pos = (0,0);
    board = None;
    team = -1;
    spritesheet = (pygame.image.load("./img/chesspieces.png"),45);
    spriteIndex = (0,0);
    canRender = True;
    hadLastMove = False;
    hasMoved = False;
    validMoves = [];
    threat = [];
    semiThreat = [];
    char = ["?"];
    
    def __init__(self,board,pos,team):
        self.pos = pos;
        self.team = team;
        self.board = board;
        self.hasMoved = False;
        self.threat = [];
        self.validMoves = [];
        self.semiThreat = [];
        self.hadLastMove = False;
        self.canRender = True;
        
    def render(self,surface):
        if(self.canRender):
            s = self.spritesheet;
            surface.blit(s[0],(self.pos[0]*s[1],self.pos[1]*s[1]),((self.spriteIndex[self.team]%6)*s[1],math.floor(self.spriteIndex[self.team]/6)*s[1],s[1],s[1]));
        
    def moveTo(self,pos):
        if(self.canMoveTo(pos)):
            self.hasMoved = True;
            p2 = self.board.getPieceAt(pos);
            self.board.setPieceAt(pos,self);
            self.board.setPieceAt(self.pos,None);
            self.pos = pos;
            if(p2):
                p2.kill();
                return True,True;
            return True,False;
        return False,False;
        
    def canMoveTo(self,pos):
        return pos in self.validMoves;
        '''if(self.board.firstEncounter(self.pos,pos) == pos):
            #if settning som ser om det er en brikke i mellom
            #brikkens posisjon og destinasjonen
            p2 = self.board.getPieceAt(pos);
            if(p2):
                return self.team != p2.team;
            return True;
        return False;'''
    
    def kill(self):
        #Logikk som skal kjøres når brikken blir slått ut
        pass;
        
    def update(self):
        self.validMoves = [];
        for i in self.threat:
            s = self.board.getPieceAt(i); 
            if((not s) or (s and s.team != self.team)):
                self.validMoves.append(i);
                
    def afterUpdate(self):
        pass;
    def __str__(self):
        return self.char[self.team%2];
        
class King(Piece):
    char = ['K','k'];
    spriteIndex = (0,6);
    #Definisjon på hvordan kongen kan bevege seg
    def render(self,surface):
        if(self.board.isThreatend(self.pos,self.team)):
            pygame.draw.rect(surface,(255,100,0),(self.pos[0]*45,self.pos[1]*45,45,45));
        super(King,self).render(surface);
    
    def moveTo(self,pos):
        i2 = self.board.getPieceAt(pos);
        if(i2 and isinstance(i2,Rook) and (not isinstance(i2,Queen))):
            if(i2.canMoveTo(self.pos)):
                return i2.moveTo(self.pos);
            else:
                return False, False;
        else:
            return super(King,self).moveTo(pos);
            
    '''
    def canMoveTo(self,pos):
        i2 = self.board.getPieceAt(pos);
        if(i2 and isinstance(i2,Rook) and (not isinstance(i2,Queen))):
            return i2.canMoveTo(self.pos);
        return pos in self.validMoves;
        return super(King,self).canMoveTo(pos) and abs(pos[0]-self.pos[0]) <= 1 and (pos[1]-self.pos[1]) <= 1;
    '''
    def afterUpdate(self):
        threats = self.board.threatenedBy(self.pos,self.team);
        semi = self.board.threatenedBy(self.pos,self.team,True);
        vM = self.validMoves;
        self.validMoves = [];
        anyMove = False;
        for i in vM:
            '''
            if(not (self.board.isThreatend(i,self.team))):
                if(not (self.board.isThreatend(i,self.team,True))):
                self.validMoves += [i];
                anyMove = True;    
            '''
            tS = self.board.threatenedBy(i,self.team);
            
            if(len(tS) <= 0):
                sM = self.board.threatenedBy(i,self.team,True);
                if(len(sM)>0):
                    for k in sM:
                        if(not k in threats):
                            self.validMoves += [i];
                            break;
                else:
                    self.validMoves += [i];
        
        if(len(self.validMoves) > 0):
            anyMove=True;
        for i in self.board.board:
            if(i != self):
                if(i and i.team == self.team):
                    if(len(threats) == 1):
                        rC = self.board.raycast(self.pos,threats[0].pos);
                        vM = i.validMoves;
                        i.validMoves = [];
                        for j in vM:
                            if(j in rC):
                                i.validMoves += [j];
                    elif(len(threats) > 1):
                        i.validMoves = [];
                    elif(len(semi)>0):
                        for j in semi:
                            if(not len(i.validMoves)>0):
                                break;
                            if(i.pos in j.threat):
                                rCast = self.board.raycast(i.pos,j.pos);
                                vM = i.validMoves;
                                i.validMoves = [];
                                for v in vM:
                                    if((v in j.threat and v in rCast) or v==j.pos):
                                        i.validMoves += [v];
                    if(len(i.validMoves)>0):
                        anyMove = True;
        
        if(not anyMove):
            if(len(threats)>0):
                self.board.winner = ((self.team+1)%2);
            else:
                self.board.winner = 2;
    def update(self):
        s = self.pos;
        self.threat = [];
        self.validMoves = [];
        for i in range(9):
            nPos = (s[0]+(i%3)-1,s[1]+(int(i/3))-1);
            if(nPos == s or nPos[0] < 0 or nPos[1] < 0 or nPos[0] > 7 or nPos[1] > 7):
                continue;
            self.threat.append(nPos);
        super(King,self).update();
        if(not self.board.isThreatend(self.pos,self.team)):
            posT = [self.board.firstEncounter(self.pos,(self.pos[0]-8,self.pos[1])),
                    self.board.firstEncounter(self.pos,(self.pos[0]+8,self.pos[1]))];
            for p in posT:
                if(p):
                    i1 = self.board.getPieceAt(p);
                    if(i1):
                        i1.update();
                        if i1.canMoveTo(self.pos):
                            self.validMoves += [p];
        
                
class Bishop(Piece):
    char = ["B","b"];
    #Definisjon på hvordan løperen kan bevege seg
    spriteIndex = (2,6+2);
    '''
    def canMoveTo(self,pos):
        return super(Bishop,self).canMoveTo(pos) and (
            abs(pos[0]-self.pos[0]) == abs(pos[1]-self.pos[1]));
    '''
    def update(self):
        self.threat = [];
        self.threat += self.board.raycast(self.pos,(self.pos[0]+8,self.pos[1]+8));
        self.threat += self.board.raycast(self.pos,(self.pos[0]-8,self.pos[1]+8));
        self.threat += self.board.raycast(self.pos,(self.pos[0]+8,self.pos[1]-8));
        self.threat += self.board.raycast(self.pos,(self.pos[0]-8,self.pos[1]-8));
        self.semiThreat = [];
        self.semiThreat += self.board.raycast(self.pos,(self.pos[0]+8,self.pos[1]+8),2);
        self.semiThreat += self.board.raycast(self.pos,(self.pos[0]-8,self.pos[1]+8),2);
        self.semiThreat += self.board.raycast(self.pos,(self.pos[0]+8,self.pos[1]-8),2);
        self.semiThreat += self.board.raycast(self.pos,(self.pos[0]-8,self.pos[1]-8),2);
        
        Piece.update(self);
        
class Rook(Piece):
    char = ["R","r"];
    spriteIndex = (4,6+4);
    #Definisjon på hvordan tårnet kan bevege seg
    '''
    def moveTo(self,pos):
        i2 = self.board.getPieceAt(pos);
        if(i2 and isinstance(i2,King) and i2.team == self.team):
            if(self.canMoveTo(pos)):
                self.board.swapPieces(self.pos,pos);
                self.hasMoved = True;
                i2.hasMoved = True;
                return True,False;
        else:
            return super(Rook,self).moveTo(pos);
        return False,False;
    '''
    def moveTo(self,pos):
        i2 = self.board.getPieceAt(pos);
        if(i2 and (not isinstance(self,Queen)) and isinstance(i2,King) and i2.team == self.team):
            if(self.canMoveTo(pos)):
                
                nPosK = (int(i2.pos[0] + 2*math.copysign(1,self.pos[0]-i2.pos[0])),self.pos[1]);
                nPosS = (int(nPosK[0]+math.copysign(1,-self.pos[0]+i2.pos[0])),self.pos[1]);
                self.board.swapPieces(self.pos,nPosS);
                self.board.swapPieces(i2.pos,nPosK);
                self.pos = nPosS;
                i2.pos = nPosK;
                self.hasMoved = True;
                i2.hasMoved = True;
                return True, False;
        else:
            return super(Rook,self).moveTo(pos);
        return False,False;
        
    '''
    def canMoveTo(self,pos):
        i2 = self.board.getPieceAt(pos);
        if(i2 and (not self.hasMoved) and isinstance(i2,King) 
          and (not i2.hasMoved) and i2.team == self.team
          and self.board.firstEncounter(self.pos,pos) == pos):
            return True;
            
            
        else:
            return super(Rook,self).canMoveTo(pos) and (
                (abs(pos[0]-self.pos[0]) > 0) != (abs(pos[1]-self.pos[1]) > 0));
    '''
    def update(self):
        self.threat = [];
        self.threat += self.board.raycast(self.pos,(self.pos[0]+8,self.pos[1]));
        self.threat += self.board.raycast(self.pos,(self.pos[0]-8,self.pos[1]));
        self.threat += self.board.raycast(self.pos,(self.pos[0],self.pos[1]-8));
        self.threat += self.board.raycast(self.pos,(self.pos[0],self.pos[1]+8));
        self.semiThreat = [];
        self.semiThreat += self.board.raycast(self.pos,(self.pos[0]+8,self.pos[1]),2);
        self.semiThreat += self.board.raycast(self.pos,(self.pos[0]-8,self.pos[1]),2);
        self.semiThreat += self.board.raycast(self.pos,(self.pos[0],self.pos[1]-8),2);
        self.semiThreat += self.board.raycast(self.pos,(self.pos[0],self.pos[1]+8),2);
       
        Piece.update(self);
        if((not self.hasMoved) and (not isinstance(self,Queen))):
            p2 = self.board.firstEncounter(self.pos,(self.pos[0]+8,self.pos[1])) or self.board.firstEncounter(self.pos,(self.pos[0]-8,self.pos[1]))
            if(p2 and not self.board.isThreatend(p2,self.team)):
                i2 = self.board.getPieceAt(p2);
                if(i2 and isinstance(i2,King) and (not i2.hasMoved)):
                    tTest = self.board.raycast(p2,(p2[0] - 2*math.copysign(1,-self.pos[0]+p2[0]),p2[1]));
                    for i in tTest:
                        if(self.board.isThreatend(i,self.team)):
                            return;
                    self.validMoves += [p2];
        
class Pawn(Piece):
    char = ["P","p"];
    spriteIndex = (5,6+5);
    movedTwice = False;
    #Definisjon på hvordan bonden kan bevege seg
    #Bonden krever litt ekstra logikk, fordi den
    #har et spesialtrekk og kan bare slå ut andre
    #brikker på skrå
    def __init__(self,board,pos,team):
        Piece.__init__(self,board,pos,team);
        self.movedTwice = False;
        
    def moveTo(self,pos):
        xDiff = -self.pos[0] + pos[0];
        yDiff = -self.pos[1] + pos[1];
        
        r,r2 = super(Pawn,self).moveTo(pos);
        self.movedTwice = r and abs(yDiff) > 1;
        if(r and not r2 and abs(yDiff) == 1 and abs(xDiff) == 1):
            #If settning som sjekker om 'En passant', fjerner
            #motstanderen om det er tilfelle
            p2 = (pos[0],pos[1] + (self.team*2 - 1));
            i2 = self.board.getPieceAt(p2);
            self.board.setPieceAt(p2,None);
            i2.kill();
        if(r and ((pos[1]+1)%8) == self.team):
            #Sjekker om bonden har nådd enden av brettet
            while(True):
                try:
                    pieace_in = int(input("Change Pawn to 1: Queen, 2: Knight, 3: Bishop, 4: Rook: "));
                    obj = Queen(self.board,pos,self.team);
                    if(pieace_in == 2):
                        obj = Knight(self.board,pos,self.team);
                    if(pieace_in == 3):
                        obj = Bishop(self.board,pos,self.team);
                    if(pieace_in == 4):
                        obj = Rook(self.board,pos,self.team);
                        
                    self.board.setPieceAt(pos,obj);
                    break;
                except Exception:
                    pass;
        return r,r2;
    
    def update(self):
        pos = self.pos;
        self.threat = [(pos[0]-1,pos[1]-(self.team*2 - 1)),(pos[0]+1,pos[1]-(self.team*2 - 1))];
        self.validMoves = [];
        
        for i in self.threat:
            p = self.board.getPieceAt(i);
            if(p and p.team != self.team):
                self.validMoves += [i];
        
        p1 = (pos[0],self.pos[1]-(self.team*2 - 1));
        p2 = (pos[0],self.pos[1]-(self.team*2 - 1)*2);
        
        if(not self.board.getPieceAt(p1)):
            self.validMoves += [p1];
        if(not self.hasMoved):
            if(not self.board.firstEncounter(pos,p2)):
                self.validMoves += [p2];
        
        p3 = (pos[0]-1,pos[1]);
        p4 = (pos[0]+1,pos[1]);
        i3 = self.board.getPieceAt(p3);
        i4 = self.board.getPieceAt(p4);
        
        if(i3 and i3.hadLastMove and isinstance(i3,Pawn) and i3.movedTwice and i3.team != self.team):
            self.validMoves += [(pos[0]-1,pos[1]-(self.team*2 - 1))];
        elif(i4 and i4.hadLastMove and isinstance(i4,Pawn) and i4.movedTwice and i4.team != self.team):
            self.validMoves += [(pos[0]+1,pos[1]-(self.team*2 - 1))];
    '''
    def canMoveTo(self,pos):
        
        if(super(Pawn,self).canMoveTo(pos)):
            p2 = self.board.getPieceAt(pos);
            i2 = self.board.getPieceAt((pos[0],pos[1] + (self.team*2 - 1)))
            xDiff = -self.pos[0] + pos[0];
            yDiff = -self.pos[1] + pos[1];
            if(-yDiff == (self.team*2 - 1)):
                #Sjekker først om brikken beveger seg vertikalt og om det er
                #en brikke forran, så om det er mulig å utføre 'En passant'
                return xDiff == 0 and not(p2) or (
                    abs(xDiff)==1 and p2 or (i2 and isinstance(i2,Pawn) and i2.movedTwice));
                    
            return ((-yDiff)/2) == (self.team*2-1) and not(self.hasMoved) and not p2;
        else:
            return False;'
        return pos in self.validMoves;
    '''
class Knight(Piece):
    char = ["N","n"];
    #Definisjon på hvordan springeren kan bevege seg
    spriteIndex = (3,6+3);
    '''
    def canMoveTo(self,pos):
        p2 = self.board.getPieceAt(pos);
        if((not p2) or (p2.team != self.team)):
            return (abs(self.pos[0]-pos[0]) == 2 and
                    abs(self.pos[1]-pos[1]) == 1) or (
                    abs(self.pos[1]-pos[1]) == 2 and
                    abs(self.pos[0]-pos[0]) == 1);
    '''
    def update(self):
        self.threat = [];
        cPos = [(self.pos[0]+2,self.pos[1]+1),
               (self.pos[0]+2,self.pos[1]-1),
               (self.pos[0]-2,self.pos[1]+1),
               (self.pos[0]-2,self.pos[1]-1),
               (self.pos[0]+1,self.pos[1]+2),
               (self.pos[0]+1,self.pos[1]-2),
               (self.pos[0]-1,self.pos[1]+2),
               (self.pos[0]-1,self.pos[1]-2)];
        
        for i in cPos:
            if(i[0] >= 0 and i[0] < 8 and i[1] < 8 and i[1] >= 0):
                self.threat.append(i);
                o = self.board.getPieceAt(i);
                
        super(Knight,self).update();
class Queen(Rook,Bishop):
    char = ["Q","q"];
    spriteIndex = (1,6+1);
    #Definisjon på hvordan dronningen kan bevege seg
    #gjør dette ved å la Queen være en blanding av tårn og løper
    '''
    def canMoveTo(self,pos):
        return super(Rook,self).canMoveTo(pos) or (
            super(Bishop,self).canMoveTo(pos));
    '''
    
    def update(self):
        Rook.update(self);
        a = self.threat;
        b = self.validMoves;
        c = self.semiThreat;
        Bishop.update(self);
        self.threat += a;
        self.validMoves += b;
        self.semiThreat += c;
