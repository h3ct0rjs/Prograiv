#!/usr/bin/env python3
#-encoding:utf-8-*-
"""
Main Applicattion for ColombianChess Project 2017,
Computer Programming IV.
feedback: hfjimenez@utp.edu.co 
Fix: Distintion of pieces and game board.
"""

from src.Piece import Piece, Rook, Bishop, Pawn, Queen, Knight
from src.ChessBoard import *

def mainC():
    while(True):
        print(rGame)
        print("Current Player: {}".format(
            "Black Team" if rGame.currentTeam else "White Team"))
        while(not rGame.move(*getMove())):
            pass

def main():
    chessGame = ChessBoard()
    chessGame.regularBoard()
    chessGame.updateAll()
    chessGame.updateAll()
    chessGame.afterUpdate()
    screenSize = 360, 360
    display = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Colombian Chess, UTP 2017-I")
    runGame = True
    time = 0
    clock = pygame.time.Clock()
    PieceInHand = None  # Initially with don't have a piece in hand.
    mPos = (0, 0)
    mOffset = (0, 0)
    print(chessGame)  # For Debuging Porpouses
    while(runGame):
        mPos = pygame.mouse.get_pos()  # get the mouse position.
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                runGame = False

            if(chessGame.winner == -1):
                if(event.type == 5):
                    # Mouse click
                    i1 = chessGame.getPieceAt(
                        (int(mPos[0] / 45), int(mPos[1] / 45)))
                    if(i1 and i1.team == chessGame.currentTeam):
                        mOffset = (int(mPos[0] % 45), int(mPos[1] % 45))
                        if(PieceInHand):
                            PieceInHand.canRender = True
                        i1.canRender = False
                        PieceInHand = i1
                        PieceInHand.update()

            if(event.type == 6):
                # Select a Piece with the mouse
                if(PieceInHand):
                    if(chessGame.move(PieceInHand.pos, (int(mPos[0] / 45), \
                        int(mPos[1] / 45)))):
                        print(chessGame)
                        print("Current player: {}".format(
                            "black" if chessGame.currentTeam else "white"))
                    PieceInHand.canRender = True
                    #I need to avoid the Render 3d option, is a small bug. 
                    PieceInHand = None

        display.fill((0, 0, 0))

        chessGame.renderBG(display)
        if(PieceInHand):
            dPm = PieceInHand
        else:
            dPm = chessGame.getPieceAt((int(mPos[0] / 45), int(mPos[1] / 45)))
        #After the user select the piece and then we need to show all the valid 
        #moves for that piece, suggestions.

        if(dPm and dPm.team == chessGame.currentTeam):
            for i in dPm.validMoves:
                cDiff = -100 * ((i[0] + 1 + i[1]) % 2)
                c = (0, 255 + cDiff, 0)
                pAt = chessGame.getPieceAt(i)
                if(pAt):
                    #paint red if the piece  is from a different team
                    if(pAt.team != dPm.team):   
                        c = (255 + cDiff, 0, 0)
                    else:
                        #draw a green botton..
                        c = (0, 0, 255 + cDiff)
                pygame.draw.rect(display, c, (i[0] * 45, i[1] * 45, 45, 45))
        #Render the images.
        chessGame.renderPieces(display)
        if(PieceInHand):
            p = PieceInHand
            s = PieceInHand.spritesheet
            display.blit(s[0], (mPos[0] - mOffset[0], mPos[1] - mOffset[1]), ((p.spriteIndex[
                         p.team] % 6) * s[1], math.floor(p.spriteIndex[p.team] / 6) * s[1], s[1], s[1]))
        clock.tick(60)
        pygame.display.update()
        time += 0.1

if __name__ == '__main__':
    main()
