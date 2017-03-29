### Parcial I
Punto 1

### **Requirements**

If you want to run this project you will need a Gnu/Linux enviroment, this was tested under Debian 9.0  and Ubuntu 16.10 both 32bits, open a terminal session and type to run manually:

```sh
user@host /tmp$ git clone https://github.com/h3ct0rjs/ProgrammingIVassignments
user@host /tmp$ cd ProgrammingIVassignments/Lab1
user@host /Lab1$ sudo apt-get install ncurses-dev build-essential g++ 
user@host /Lab1$  g++ -o solvequeen solver.cpp -lncurses
user@host /Lab1$ ./solvequeen
```
### **Run Test Cases **
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
 
License
---
Mozilla Public License

Contact me: hfjimenez@utp.edu.co