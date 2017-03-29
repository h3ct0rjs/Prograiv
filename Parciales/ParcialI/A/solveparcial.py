#!/usr/bin
#-*- coding :utf-8 -*-
#hfjimenez@utp.edu.co, 2017
#Computer Programming IV, UTP. Exam 1. 
#http://pep8online.com/checkresult
#pep-0257,pep-008

class ProductClass:
	"""Create an object product

	This will create a product with the minimun attributes required. 
	usage : producto=ProductClass()
	 		producto1=ProductClass("Leche",5000,quantityvalue)
	 		producto1=ProductClass("Leche",5000,quantityvalue,offer=False,white=False)	 		
	Attributes:
		Product Description: name 
		Product Price: price
		Product Offering: False(D)
		Product Points: 0 as default, as . 
		Product BranchName: branch, None as default.
		Product Quantity: Total of items
	Supported methods:
		setPrice(value),getPrice()
		setBranchName(strvalue),getBranchName()
		setName(strvalue),getName()
		setOfert(), unsetOfert()
		setWhite(), unsetWhite(): You're always allowed to set and unset a 
		normal product. See ProductWhiteClass if you want to create a White 
		specific one.
		setQuantity(number),getQuantity()

	"""
	def __init__(self,name=None,price=0,quantity=1,offer=False,white=False):
		"""
		Default Initializator, See the docstring of the main Class.
		"""
		self.name=name
		self.price=price 
		self.offer=offer 
		self.white=white 
		self.points=0
		self.branch=None
		self.quantity=quantity		#I'm not pretty sure if this can be a 
									#product attribute, since I can handle as 

	def setQuantity(self,newquantity):
		"""
		Set the quantity of the product,less supounce that you want to set
		your product with 3 of the same :

		usage: product.setQuantity(3)
		"""
		self.quantity=newquantity

	def getQuantity(self):
		"""
		Returns the number of the product, 
		usage: product.getQuantity()
		"""
		return self.quantity

	def setPrice(self,newprice):
		"""
		Stablish the price (COP)of the product, 
		usage: product.setPrice(1500)
		"""
		self.price=newprice
	
	def getPrice(self):
		"""
		Retrieve the product price, 
		usage: product.getPrice()
		"""
		return self.price

	def setBranchName(self,newbranch):
		"""
		Set the BranchName of the product object.
		usage: product.setBranchName(string)
		"""
		self.branch=newbranch

	def getBranchName(self):
		"""
		Retrieve Branch product name.
		usage: product.getBranchName()
		"""
		return self.branch

	def setName(self,newname):
		"""
		Set product name.
		usage: product.setName("newname")
		"""
		self.name=newname

	def getName(self):
		"""
		Set product name.
		usage: product.setName("newname")
		"""
		return self.name

	def setOfert(self):
		"""
		Set product name.
		usage: product.setOfert("newname")
		"""
		self.offer=True

	def unsetOfert(self):
		"""
		UnSet product name.
		usage: product.unsetOfert("newname")
		"""
		self.offer=False

	def __str__(self):
		"""
		override string magic method, this avoids things like : 
		<__main__.ProductClass object at 0x1100935f8>.
		You will be able to get the values of the product.
		print(product)
		"""
		return str(self.name+" $"+str(self.price)+ \
			" Quant:"+str(self.quantity)+\
			" Points:"+str(self.points))
	

class WhiteProductClass(ProductClass):
	"""Using inheritance to create an object product of White Class.
	This will create a whiteproduct with the minimun attributes required. 
	usage : product=WhiteProductClass()
	 		product=WhiteProductClass("Leche",5000,quantityvalue)
	Default Attributes:
		Product Description: name 
		Product Price: price
		Product Offering-deal: False(D)
		Product Points: 1 as default, as it's a white product . 
		Product BranchName: branch, None as default.
		Product Quantity: Total of items

	Supported methods:
		setPrice(value),getPrice()
		setBranchName(strvalue),getBranchName()
		setName(strvalue),getName()
		setOfert(), unsetOfert()
		setWhite(), unsetWhite(): You're always allowed to set and unset a 
		normal product. See ProductWhiteClass if you want to create a White 
		specific one.
		setQuantity(number),getQuantity()
	"""
	def __init__(self,name=None,price=None,quantity=1,offer=False):
		"""
		Default Initializator, See docstring of main Class.
		"""
		self.name=name
		self.price=price 
		self.offer=offer 
		self.white=True 
		self.points=1
		self.branch=None
		self.quantity=quantity		#I'm not pretty sure if this can be a 
									#product attribute, since I can handle as 
		
class ShoppingList:
	"""Create a Buy List

	This will create a shoppinglist for each client 

	Supported methods:
		getPoints()	: it will return the amount of total points that 
		were given due to the whiteclass products.
		to use this you'll need to instance the shopping list like :
		
			Mybuy=ShoppingList(items,discount_type)
		dyscounts_type : 1: 3x2
						 2: 2nd half price
		usage:  
				Mybuy.getPoints()

		getTotalBuy(): get the total cost for all the items in the Shopping list
		usage: Mybuy.getTotalBuy()
		
		getTotalDiscounts()
		getFreeItems()
		getFreeItemsDetails()
	"""
	def __init__(self,list_items,discount_type):
		self.list_items=list_items
		self.count=len(list_items)
		self.discount_type=discount_type

	def getPoints(self):
		"""
		get the total points of the white products .
		usage: Mybuy.getPoints()
		"""
		whiteproductlist=[x for x in self.list_items if x.white==True]
		points=len(whiteproductlist)
		return points

	def getTotalBuy(self):
		"""
		Total to paid by all the items in the shopping list:
		usage: Mybuy.getTotalBuy()
		"""
		#stotal=sum([ i.getPrice()*i.getQuantity() for i in self.list_items])
		priceperitem=[]
		if self.discount_type==1:
			for i in self.list_items:
				if i.offer== True and i.white == True:
					itempay= (i.getPrice()* i.getQuantity())-(i.getPrice()* i.getQuantity()*0.10)	#-10% of total price.
				else :
					itempay= (i.getPrice()* i.getQuantity())
					print("You pay : {}".format(itempay))
				freeitems=i.getQuantity()//3
				s=freeitems*i.getPrice()
				itempay-=s
				priceperitem.append(itempay)
		return sum(priceperitem)
