#-*- coding:utf-8-*-
#angel's solution
#Add animations using objects implementing the graphics.py library.
#Python Programming IV Class: Implement using python3 version
#To install graphics.py pip3 install --user http://bit.ly/csc161graphics

from graphics import  *	#Caveat! Remember "wildcard" (*) imports are not good form 

N = 8

class Board:
    def __init__(self):
        pass

    def drawer(self):
        win = GraphWin("N Queens", 500, 500)
        c = Circle(Point(500,500), 10)
        c.draw(win)
        aLine = Line(Point(250,250), Point(300,250))
        aLine.draw(win)
        win.getMouse()        
        win.close()
        
    def Drawqueen(self):
        pass
                                   
    
class Queen:

	def __init__(self,col,neighbor):
		self.row = 1
		self.col = col
		self.neighbor = neighbor

	def find_soluction(self):
		while self.neighbor is not None and self.neighbor.can_attack(self.row, self.col):
			if not self.advance():
				return False
		return True

	def advance(self):
		# trata siguiente fila
		if self.row < N:
			self.row += 1
			return self.find_soluction()

		#no puedo ir mas adelante
		#muevo el vecino a la siguiente solucion
		if not self.neighbor.advance():
			return False

		#Inicio nuevamente en fila 1
		self.row =  1
		return self.find_soluction()

	def can_attack(self,row,col):
		"probar en la misma fila"
		if self.row == row:
			return True

		#probar diagonales
		diff = col - self.col
		if self.row + diff == row or self.row - diff == row:
			return True

		#no podemos atacar ver si el vecino puede
		return self.neighbor is not None and self.neighbor.can_attack(row, col)

	def printt(self):
		if self.neighbor is not None:
			self.neighbor.printt()
		print (self.row, self.col)


if __name__ == '__main__':
	q = None
	for i in range(N):
		q = Queen(i + 1, q)
		if not q.find_soluction():
			print('Sin solucion')
	q.printt()	
