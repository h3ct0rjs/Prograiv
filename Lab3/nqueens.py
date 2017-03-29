#!/usr/bin/python3
#-*- coding:utf-8-*-
#angel's solution
#Add animations using objects implementing the graphics.py library.
#Python Programming IV Class: Implement using python3 version
#To install graphics.py pip3 install --user http://bit.ly/csc161graphics

from graphics import  *	#Caveat! Remember "wildcard" (*) imports are not good form 
import math as m
N = 8



class Board:
	def __init__(self):
		pass 

	def maker(self,corner, width, height):  
		corner2 = corner.clone()	#Because we need to setup the new object and a new reference
		corner2.move(width, height)
		return Rectangle(corner, corner2)

	def bdraw(self):
	#""All the operations related to graphics.py"""
		win = GraphWin('Nqueens Solver',300,300)	
		win.setBackground('white')
		message = Text(Point(win.getWidth()/2, 18), 'ChessBoard')
		message.setTextColor('red')
		message.setStyle('italic')
		message.setSize(12)
		message.draw(win)
		warea=Polygon([Point(30,30),Point(270,30),Point(270,270),Point(30,270)])
		warea.draw(win)
		sqsize=m.floor(win.getWidth()/N)	#square size.
		startp=Point(30,30)
		print(sqsize)					#we need a start.
		for i in range(7):
			rect=self.maker(startp,sqsize,sqsize)
			print(rect)						#debug
			rect.draw(win)
			win.getMouse()					#Pause until you click the window.
			startp=Point(startp.getX()+sqsize,startp.getY()+sqsize)
		win.getMouse()						#Pause until you click the window.
		win.close()                   		#Destroy the object win.

	def animations(self,datalist):
	    for i in range(N):
	        q.move(posx, posy)
	        time.sleep(.05)



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
		print(self.row, self.col)


if __name__ == '__main__':
	q = None
	for i in range(N):
		q = Queen(i + 1, q)
		if not q.find_soluction():
			print('Sin solucion')
	
	q.printt()	

	boardcito=Board()
	boardcito.bdraw()
