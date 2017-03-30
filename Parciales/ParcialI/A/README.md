## Parcial I
Punto 1

### Requirements 

If you want to run this project I just test it out using  a Gnu/Linux enviroment and python 3.6, this was tested under Debian 9.0  and Ubuntu 16.10 both 32bits, but it should work normaly on other OSes, just open a terminal session and use your favorite python interpreter :

```sh
user@host /tmp$ git clone https://github.com/h3ct0rjs/ProgrammingIVassignments
user@host /tmp$ cd ProgrammingIVassignments/Parciales/ParcialI/A
user@host /A$ python3.5 solve.py
PUNTO 1, PARCIAL 1
[*]Ejemplo Descuento 3x2
Lista de Productos :

Carton de Leche $1200 Quant:3 Points:0
Botella de Agua $500 Quant:5 Points:0
You pay : 3600
You pay : 2500
El total de su compra es 4400
[EOF]


```
### Basic Run Test Case with Discount 3x2
```python 
p4=ProductClass("Carton de Leche",1200,3)
p5=ProductClass("Botella de Agua",500,5)
listaproductos=[p4,p5]
print("Lista de Productos :\n")
for i in listaproductos:
	print(i)
compra =ShoppingList(listaproductos,1)	#We just said Discount type =1, means 3x2
print("El total de su compra es {}" .format(compra.getTotalBuy()))
```

### Documentation
 
 if you're using ipython you can get all the explanation, because I use the docstring desciptions
 
 ```python 
In [1]: WhiteClassProduct?
In [2]: ProductClass.getPrice?
```

License
---
Mozilla Public License

Contact with me: hfjimenez@utp.edu.co
