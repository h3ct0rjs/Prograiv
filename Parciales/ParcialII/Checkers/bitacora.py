#!/usr/bin/env python3
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#Bitacora Documental
#Con PyQt podemos crear Botones, menus, checkboxes, graficos, ventanas etc.

"""
Para empezar Creare botones utilizando PyQt. Lo primero es que 
todos los widgets se encuentran en QtGui, y QtCore.
Bastara con crear una clase que herede los metodos y atributos para trabajar.
Para crear botones Estanciamos del Objeto QPushButton:
btn.resize(btn.minimunSizeHint())btn.move(x,y)
btn.resize(x,y) and others with buttons
Despues de Aprender a crear las ventanas y los botones, 
Y el manejo de señales, es facil crear vebtabas de popups 
Ussing QMessages....etc


Bueno he aprendido que al parece Los WidGets Que Pintan fallan como los 
png, y toca usar jpg. Para representar la Board voy a usar un QTable de la forma 


"""
class Ventana(QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        #Set the Checkers Title
        self.setWindowTitle('Final Checkers')
        #700X690 Para la ventana
        self.setGeometry(50,50,500,300)
        
        self.home()

    def home(self):
        
        self.table = QTableWidget(8,8,self)
        self.table.verticalHeader().setDefaultSectionSize(60)
        self.table.horizontalHeader().setDefaultSectionSize(60)
        # default vertical and horizontal header size is 60 images are 60pixels x 60 pixels
        self.table.verticalHeader().setDefaultSectionSize(60)
        self.table.horizontalHeader().setDefaultSectionSize(60)
        
        # turning scroll bars off 
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # move the table 10 right and 10 down
        self.table.move(10,10)
        # fix table size of 500 x 510
        self.table.setFixedSize(500, 510)
        # fixed view for vertical and horizontal headers
        self.table.verticalHeader().setResizeMode(QHeaderView.Fixed)
        self.table.horizontalHeader().setResizeMode(QHeaderView.Fixed)
        self.show()
        

    def CambiaTitulo(self):
        self.setWindowTitle('.....Saliendo')


def run():
    #Instanciamos la aplicacion
    app = QApplication(sys.argv)
    #Creamos la ventana
    ventana = Ventana()
    sys.exit(app.exec_())


run()
