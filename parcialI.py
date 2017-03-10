#!/usr/bin/python3
#-*- coding : utf-8 -*- 
#Solve the first exam of Computer Programming 4,I was lost with this 
#is a shame, I know but I understand why I just fail, I was not well focus,
#anyway you need to keep things going on, so that's the porpouse of this. 
#Linea de Compra: [p1,p2,p3,p4]
import uuid

class Producto:
	"""Construye una identidad de producto."""
	def __init__(self,nombre,preciou,cantidad,tipo):
		"""Inicializa un producto,precio,cantidad, """
		self.precio=preciou
		self.nombre=nombre
		self.cantidad=cantidad 
		if tipo.lower()=='normal':
			self.tipo=False
		elif tipo.lower()=='blanco':
			self.tipo=True
		else:
			self.tipo= None

	def setNombre(self,nombre):
		"""Establece Nombre de producto"""
		self.nombre=nombre

	def getNombre(self):
		"""Nombre de  producto"""
		return self.nombre

	def setPrecio(self,preciounitario):
		"""Establece precio unitario"""
		self.precio=preciounitario

	def getPrecio(self):
		"""Precio del producto"""
		return self.precio

	def setCantidad(self,cantidad):
		"""Establece la cantidad de producto"""
		self.cantidad=cantidad

	def getCantidad(self):
		"""Establece la cantidad de producto"""
		return self.cantidad

class ProductoBlanco(Producto):
	pass

class Compra :
	"""Carrito de para Linea de Compra."""
	def __init__(self,idcompra):
		self.idcompra=idcompra
		self.data=[]

	def agregarProducto(self,item):
		self.data.append(item)

	def calculaTotal():
		pass

if __name__ == '__main__':
	p1=Producto('leche',1200,3,'normal')
	p2=Producto('Arroz Libra',1800,1,'blanco')
	lc1=Compra(uuid.uuid4())			#Linea de Compra 1. Id unico 
	