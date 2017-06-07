#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Details:views.py, main
# ParcialIII,Final Project, Computer Programming IV
# feedback:hfjimenez@utp.edu.co,dcquiroz@utp.edu.co
#ToDos :
#    Add contextual menu for Player vs Player, Machine vs Player.
#
# Features:
#   Documentation in Spanish and English
#   Mouse selections
#   Per token show the list of Sugestions
#
#   This program is free software; you can ficharojaistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; Applies version 2 of the License.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
import sys
#PyQt4 Objects,use the selector to avoid QtCore.QWidget..bad if the project isbig
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from src.controller import *
from src.models import *
from src.routesimg import *


class ImgWidget(QWidget):
    """
    default constructor takes image path and the parent of widget
    """

    def __init__(self, imagePath, parent):
        super(ImgWidget, self).__init__(parent)
        self.picture = QPixmap(imagePath)

    def paintEvent(self, event):
        """
        Draw an Image based on an event
        """
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.picture)


class Ventana(QWidget):
    """
    Creates all visual aspects for Window main application: 
    --------
    | Main  |>> DetailsUserInterface>>ShowLabels
    --------
    Supported Methods:
    DefaultUI << Designer Generate this
    """

    def __init__(self):
        """
        We need super to inherid from the QWidget and Ventana itself
        """
        super(Ventana, self).__init__()
        self.DefaultUI()

    def DefaultUI(self):
        self.gameHistory = []
        self.score = []
        self.playing = False
        self.setFixedSize(700, 530)  # Screen Size.Fixed 700 Width,690 Heigth
        self.setWindowTitle(
            "UTP Final Term Project,2017-I hfjimenez@utp.edu.co"
        )  # sets the window title
        self.GameMode = None

        print("Game Mode is :{}".format(self.GameMode))  #debug
        playMode = QMessageBox.question(self,'Modo de Juego', \
            'Maquina Vs Jugador?',QMessageBox.Yes,QMessageBox.No)   #Choose Game Mode
        print("playMode :{}".format(True if playMode else False))

        if playMode == QMessageBox.Yes:
            self.GameMode = True
            #We Have a Game Machine vs Human
            machineLabel = QLabel(" Maquina ", self)
            machineLabel.setFont(
                QFont('TimesNewRomans', 12, weight=QFont.Bold))
            machineLabel.move(self.width() - 140, 10)
        else:
            self.GameMode = False
            #We Have a Game Human vs Human
            machineLabel = QLabel("Jugador 2", self)
            machineLabel.setFont(
                QFont('TimesNewRomans', 12, weight=QFont.Bold))
            machineLabel.move(self.width() - 140, 10)
            self.player2 = True

        exitBtn = QPushButton("Salir", self)
        exitBtn.resize(exitBtn.minimumSizeHint())
        exitBtn.move(self.width() - 90, self.height() - 250)

        deshacerBtn = QPushButton("Deshacer", self)
        deshacerBtn.resize(deshacerBtn.minimumSizeHint())
        deshacerBtn.move(self.width() - 90, self.height() - 200)

        ngBtn = QPushButton("Juego Nuevo", self)
        ngBtn.move(self.width() - (180), self.height() - (250))
        ngBtn.resize(ngBtn.minimumSizeHint())

        abandonarBtn = QPushButton("Rendirse", self)
        abandonarBtn.move(self.width() - 180, self.height() - 200)
        abandonarBtn.resize(abandonarBtn.minimumSizeHint())

        #Labels for all the players :-)
        self.turn = QLabel('', self)
        self.turn.setFont(QFont('TimesNewRomans', 18))
        self.turn.move(self.width() - 180, self.height() / 3)
        self.turn.setMinimumWidth(200)

        ficharojaImg = ImgWidget(ficharoja, self)
        ficharojaImg.setGeometry(560, 50, 60, 70)  #Score System to the left

        playerLabel = QLabel("Jugador 1", self)
        playerLabel.setFont(QFont('TimesNewRomans', 12,weight=QFont.Bold))
        playerLabel.move(self.width() - 145, self.height() - 370)

        fichanegraImg = ImgWidget(fichanegra, self)  #Score System to the left
        fichanegraImg.setGeometry(560, self.height() - 340, 60, 60)

        # Number of pieces computer has
        self.machinePiece = QLabel(" 0 ", self)
        self.machinePiece.setFont(QFont('TimesNewRomans', 12))
        self.machinePiece.move(self.width() - 75, 60)

        # Number of pieces player has
        self.playerPiece = QLabel(' 0 ', self)
        self.playerPiece.setFont(QFont('TimesNewRomans', 12))
        self.playerPiece.move(self.width() - 75, self.height() - 320)

        self.table = QTableWidget(8, 8, self)  # grilla de 8x8 Estilo Excel
        #casilla de 60*60 para el tablero. Imagenes redimensionadas a este size.
        self.table.verticalHeader().setDefaultSectionSize(60)
        self.table.horizontalHeader().setDefaultSectionSize(60)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.move(
            10,
            5)  # move the table like a padding in html 10 right and 10 down
        self.table.setFixedSize(500,
                                510)  #700, 530 is the total, 500 for table
        #Desabilita los numeros y letras de la QTable
        self.table.verticalHeader().setResizeMode(QHeaderView.Fixed)
        self.table.horizontalHeader().setResizeMode(QHeaderView.Fixed)

        #Show all my images
        fichanegraImg.show()
        ficharojaImg.show()
        playerLabel.show()
        machineLabel.show()
        self.turn.show()  #The initial Is for the max, I mean the player.
        abandonarBtn.show()
        deshacerBtn.show()
        ngBtn.show()
        exitBtn.show()
        self.show()
        self.table.show()

        #PyQt Signal Processing. Click the buttos
        ngBtn.clicked.connect(self.JuegoNuevo)
        exitBtn.clicked.connect(self.close)
        deshacerBtn.clicked.connect(self.deshacerfunc)
        abandonarBtn.clicked.connect(self.abandonajfunc)
        self.table.verticalHeader().hide(
        )  # sets the horizontal and vertical header labels hide
        self.table.horizontalHeader().hide()
        # displays a vacio board in the table
        self.setEmptyBoard()
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

    #Views EOF.
    #Necesary HelperFunctions from here
    def JuegoNuevo(self):
        """
        Create a New Game, it pops up asking the confirmation
        """
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        print("Juego Nuevo Funcion Ejecutada")#debug
        if self.playing:
            abandonarDialogo = QMessageBox.question(
                self, 'Juego Nuevo', 'Seguro que deseas iniciar otra partida?',
                QMessageBox.Yes, QMessageBox.No)
            #if yes end game else do nothing
            if abandonarDialogo == QMessageBox.Yes:
                self.game.r()
            else:
                return

            playMode = QMessageBox.question(self,'Modo de Juego', \
            'Maquina Vs Jugador?',QMessageBox.Yes,QMessageBox.No)   #Choose Game Mode
            print('play Mode{}'.format(playMode))
            print('QMess{}'.format(QMessageBox.Yes))

            if playMode == QMessageBox.Yes:
                self.GameMode = True
                #We Have a Game Machine vs Human
                machineLabel = QLabel(" Maquina ", self)
                machineLabel.setFont(
                    QFont('TimesNewRomans', 12, weight=QFont.Bold))
                machineLabel.move(self.width() - 140, 10)
            else:
                self.GameMode = False
                #We Have a Game Human vs Human
                machineLabel = QLabel("Jugador 2", self)
                machineLabel.setFont(
                    QFont('TimesNewRomans', 12, weight=QFont.Bold))
                machineLabel.move(self.width() - 140, 10)
                self.player2 = True


        self.playing = True
        # create a new game
        self.game = MainController()
        self.gameHistory = []

        tmpAllGame = deepcopy(self.game)  #Save History Just After creating the new game
        self.gameHistory.append(tmpAllGame)
        self.updateGame()
        self.connect(self.table,SIGNAL("cellClicked(int,int)"), self.clickBoard)
   
    def deshacerfunc(self):
        """ 
        Deshacerfunc function is called when deshacerfunc button is clicked
        """
        if self.gameHistory and self.playing:
            #gameHistory keep tracks of all the movements.
            #you just can go back one time. No more.
            #self.game is the state of the board.
            pop = deepcopy(self.gameHistory.pop())
            self.game = pop
            self.updateGame()  #reset the game to the last state.
            self.gameHistory = [
            ]  #I clean game history to prevent cheating and
            #multiples go backs.

        
    def abandonajfunc(self):
        """
        When you click abandonar button, we reconfirm  this.
        """
        if self.playing:
            abandonarDialogo = QMessageBox.question(
                self, 'Rendirse',
                'Estas seguro que tu quieres rendirte y perder la gloria?',
                QMessageBox.Yes, QMessageBox.No)
            if abandonarDialogo == QMessageBox.Yes:
                self.game.r()
                self.updateGame()
                self.playing = False

    
    def clickBoard(self, y, x):
        """
        Interaction between mouse and the Qtable.
        """
        #takes a deep copy of the game before a move is performed
        tmpAllGame = deepcopy(self.game)

        if not self.game.isFinished():
            if self.x1 == None:
                self.click(x, y)    #The first Click 
            else:
                self.x2 = x         #My Second Click
                self.y2 = y
                moved = False
                # checks if the turn is the players before taking a move
                if (self.game.getTurn() == "Player"):
                    moved = self.game.movePiece("Player", self.x1, self.y1,
                                                self.x2, self.y2)
                
                self.updateGame()       # updates the board
                if moved and self.game.getTurn(
                ) == "Player" and not self.game.isFinished():
                    # add to the deepcopy state of the board that was copied before a move
                    self.gameHistory.append(tmpAllGame)
                    self.game.turnEnd()     #next turn 
                    self.x1 = None
                    self.y1 = None
                    x = None                
                    y = None
                    self.updateGame()       # updates piece positions

                    if self.game.getTurn() == "M" and not self.game.isFinished():
                        # call the M to make a move and update the move it has taken.
                        #returns a string and higlith the move its taken
                        ai_moved = self.game.M()
                        self.updateGame()
                        if len(ai_moved) > 0:
                            self.resaltarPieza(ai_moved[0], ai_moved[1])
                            self.resaltarPieza(ai_moved[2], ai_moved[3])
                            self.x1 = None
                            self.y1 = None
                            x = None
                            y = None
                        else:
                            pass
                else:
                    self.click(x, y)    #highligth and position x,y with movementp.

            self.x2 = None
            self.y2 = None

    
    def click(self, x, y):
        #click in the position of x,y, get the piece and highlight=resalta.
        if self.game.getPiece(x, y):
            self.x1 = x
            self.y1 = y
            # resaltar los posiblemovimientos de la pieza.
            self.resaltarMovable(self.x1, self.y1,self.game.getMoves("Player"))
        else:
            self.x1 = None
            self.y1 = None

    #resaltar pieza
    def resaltarPieza(self, x1, y1):
        tmpF = self.game.getPiece(x1, y1)
        if tmpF:
            # checks the pieces owner and sets the cell image based on the pieces owner and type
            if (tmpF.getOwner() == "M"):
                if (tmpF.getType() == 1):
                    self.table.setCellWidget(y1, x1,ImgWidget(resaltarreyRed, self))
                    #draw the image in the cell part of the Qtable. If Ficha is type=1 is a
                    #king
                else:
                    self.table.setCellWidget(y1, x1,ImgWidget(resaltarRed, self))
            else:
                #the piece is human.
                if (tmpF.getType() == 1):
                    self.table.setCellWidget(y1, x1,ImgWidget(resaltarreyBlack, self))
                else:
                    self.table.setCellWidget(y1, x1,ImgWidget(resaltarBlack, self))
        # if tmpF isn't a piece then set it as empty or posible jump
        else:
            self.table.setCellWidget(y1, x1, ImgWidget(resaltar, self))

    def resaltarMovable(self, x1, y1, moves):
        # resaltars the piece being clicked
        self.resaltarPieza(x1, y1)
        # parses i of all the moves, checks if x1 equals index 0 and y1 equals index 2
        for i in moves:
            # if they equal cast i[4] and i[6] to ints and resaltar the vacio squares the piece can move to
            if x1 == int(i[0]) and y1 == int(i[2]):
                tmpx = int(i[4])
                tmpy = int(i[6])
                self.resaltarPieza(tmpx, tmpy)

    
    def setEmptyBoard(self):
        """
        Clear the board 
        """
        for y in range(8):
            for x in range(8):
                if (y % 2 == 0 and x % 2 == 1):
                    self.table.setCellWidget(y, x, ImgWidget(vacio, self))
                if (y % 2 == 1 and x % 2 == 0):
                    self.table.setCellWidget(y, x, ImgWidget(vacio, self))
                if (y % 2 == 0 and x % 2 == 0):
                    self.table.setCellWidget(y, x, ImgWidget(blanco, self))
                if (y % 2 == 1 and x % 2 == 1):
                    self.table.setCellWidget(y, x, ImgWidget(blanco, self))

    def updateGame(self):
        # First we need to clear the board.
        # This can be ugly but it Works like a charm, because I just rebuild the board. 
        self.setEmptyBoard()
        for y in range(8):
            for x in range(8):
                # populate the board if position x and y has a piece
                ficha = self.game.getPiece(x, y)
                if ficha:
                    if ficha.getOwner() == "M":
                        if ficha.getType() == 1:
                            self.table.setCellWidget(y, x,ImgWidget(ficharojarey, self))
                        else:
                            self.table.setCellWidget(y, x,ImgWidget(ficharoja, self))
                    elif ficha.getOwner() == "Player":
                        if ficha.getType() == 1:
                            self.table.setCellWidget(y, x,ImgWidget(fichanegrarey, self))
                        else:
                            self.table.setCellWidget(y, x,ImgWidget(fichanegra, self))
                    else:
                        print('Dueño Desconocido')

        self.machinePiece.setText(str(self.game.getM())) #Show the number of pieces for machine

        self.playerPiece.setText(str(self.game.getPlayer())) #number of pieces for Player
        #show pieces in the board again.
        self.machinePiece.show()
        self.playerPiece.show()

        
        if (self.game.getTurn() == "M"):
            self.turn.move(530, 400)
            self.turn.setText("Pensando, minimax...")
            self.turn.setFont(QFont('TimesNewRomans', 12))

        else:
            self.turn.move(535, 400)
            self.turn.setText("Turno: Jugador 1")
            self.turn.setFont(QFont('TimesNewRomans', 12))
        # if over set the players turn to game over.
        if self.game.isFinished():
            self.turn.setText("Game Over!!")
            self.turn.setFont(QFont('TimesNewRomans', 12))
            self.playing = False
        self.turn.show()

    def closeEvent(self, event):
        #Adaptado de https://stackoverflow.com/questions/1414781/prompt-on-exit-in-pyqt-application
        reply = QMessageBox.question(self, 'Salir','Seguro que desea cerrar el programa?',QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.playing = False
            event.accept()
        else:
            event.ignore()


def Start():
    """
    Creates The Window. 
    """
    app = QApplication(sys.argv)
    print("Hey Hooray, I start the views.py")
    interface = Ventana()
    sys.exit(app.exec_())