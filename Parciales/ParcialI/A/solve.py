#!/usr/bin
#-*- coding :utf-8 -*-
#Usage of Product Class, WhiteProduct
from solveparcial import *
#Testing color support
HEADER = '\033[95m'
OK = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
UNDERLINE = '\033[4m'
print("{}PUNTO 1, PARCIAL 1{}".format(UNDERLINE,ENDC))
print("{}[*]{}Ejemplo Descuento 3x2".format(OK,ENDC))
p4=ProductClass("Carton de Leche",1200,3)
p5=ProductClass("Botella de Agua",500,5)
listaproductos=[p4,p5]
print("Lista de Productos :\n")
for i in listaproductos:
	print(i)
compra =ShoppingList(listaproductos,1)	#We just said Discount type =1, means 3x2
print("El total de su compra es {}" .format(compra.getTotalBuy()))
print("{}[EOF]{}".format(FAIL,ENDC))