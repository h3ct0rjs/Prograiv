### Computer Programming IV, Laboratory 1
[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

*Based on Program Development by Stepwize refinement*
    : Following the procedure I just create a quick permutations to set positions of the queen 


### **Requirements**

If you want to run this project you will need a Gnu/Linux enviroment, this was tested under Debian 9.0  and Ubuntu 16.10 both 32bits, open a terminal session and type to run manually:

```sh
user@host /tmp$ git clone https://github.com/h3ct0rjs/ProgrammingIVassignments
user@host /tmp$ cd ProgrammingIVassignments/Lab1
user@host /Lab1$ sudo apt-get install ncurses-dev build-essential g++ 
user@host /Lab1$  g++ -o solvequeen solver.cpp -lncurses
user@host /Lab1$ ./solvequeen
```
### **Automatic Run **

```sh
user@host /Lab1$ make 
user@host /Lab1$ ./solvequeen
```


### Supported Flags
Actually I was playing with argv, and argc at low level code so I just think this could be a great chance to implement arguments as I neverused before.

```sh
user@host /Lab1$ ./solvequeen --version
``` 

* **-v**  or  **- -version** *
    : Current  software version

* **-h** or **- -help** *
    : Show the information usage

* **-nc** or **- -not-color** 
    : Disable ncurses color,this black and white. 
 
* **-t** or **- -theory**
    : Quick Explanation of how this computer programm works. 
 
License
---
Mozilla Public License

Contact me: hfjimenez@utp.edu.co
