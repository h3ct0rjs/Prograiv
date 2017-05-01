# Checkers
[![Python](https://www.python.org/static/community_logos/python-powered-w-100x40.png)](https://www.python.org/)

Your task is Design and implement a checkers game taking in count the following patterns:
 - Observator
 - Iterator
 - Strategic 
 - Facade
 - MVC
 
You're able to use : C++, Java, Python as graphical options you are able to use : Python{Qt,Graphics.py},C++{Qt,Allegro},Java{Fx}.

### Installation

our checkers game requires [python3.6](https://www.python.org/) to run.
you will need to install the dependencies and start the game.

```sh
$ cd Checkers
$ python3.6 start.py
```
or 
```sh
$ cd Checkers
$ chmod +x start.py && ./start.py
```

This version is not tested for Windows enviroments, but it should work! normally.


### Checkers US Rules

In order to develop our small checkers game, we  explore many different rulesets  [[1]](https://www.thespruce.com/play-checkers-using-standard-rules-409287),[[2]](https://en.wikipedia.org/wiki/Draughts)
after a long discution we agree to use the US version
- Each player has 12 tokens 
- tokens move in one direction(toward opponent)
- tokens can only move diagonally 
- tokens that reach the end of the board becomes in king tokens
- king tokens can move in any direction 
- win by jumping over all opponent tokens 

move : diagonally 1 empty space 
jump : diagonally 2 spaces 


### Architectural Pattern: mvc

#### Models
Store the state of the board movements, and current list of sugestion. 
The datastructure use to store the states is a list of list,we were reading all 
the posible data-structure to represent a checkers board  like they are :
- Piece List 
- Array2d based
- bit board 

because we're not worried about speed we can use the most simple ds, the array, this could be 
achive using the following snippet in python3.6

```python 
        grid = [[0]*8 for _ in range(8)]
        grid[0] = [0 if i%2 == 0 else 1 for i in range(8)]
        grid[1] = grid[0][::-1]
        grid[6] = [0 if i%2 == 0 else 2 for i in range(8)]
        grid[7] = grid[6][::-1]
```
The previous code give us a representation where the number 0 is an empty space, 1 represent tokens for black pieces and 2 for white pieces:

```sh
-----------------------
0| 1| 0| 1| 0| 1| 0| 1| 
-----------------------
1| 0| 1| 0| 1| 0| 1| 0| 
-----------------------
0| 0| 0| 0| 0| 0| 0| 0| 
-----------------------
0| 0| 0| 0| 0| 0| 0| 0| 
-----------------------
0| 0| 0| 0| 0| 0| 0| 0| 
-----------------------
0| 0| 0| 0| 0| 0| 0| 0| 
-----------------------
0| 2| 0| 2| 0| 2| 0| 2| 
-----------------------
2| 0| 2| 0| 2| 0| 2| 0| 
-----------------------
```
#### Activity Log for movements

We want to show your game, so after know how to store the data, every body knows that is pretty important in every type of board game keep an activity log, we use a dictionary where key is the id of the movement, and the asociate value is the movement, we lock the key pair to avoid changes.  

```python 

    Board.getLogMovements()
  Id | Movements 
    1. A1 to B3
    2. B5 to C4 
    3. ...so on!

```

### Development

Want to contribute? Great!
Open an issue and create a pull request for your fixes and new features

* Hector F. Jimenez S. , hfjimenez@utp.edu.co 
* Daniel Quiroz , dcquiroz@utp.edu.co


### Todos

 - ~~Learn to play checkers.~~
 - ~~Create the sketch up of the game, get a list of objects and his interations between them~~
 - Graphical mode !
 - Add Night Mode.
 - Think in m2m battles.


### Useful Resources

- https://realpython.com/blog/python/the-model-view-controller-mvc-paradigm-summarized-with-legos/

License
----
mozilla public license 2.0

**Free Software, Hell Yeah!**