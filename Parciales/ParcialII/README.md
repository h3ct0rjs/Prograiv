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

our checkers game requires [python3.6](https://www.python.org/) to run, PyQt4.
you will need to install the dependencies and start the game.

#### Automatic Process
Use make to start the game.

```sh
$ make up
```

#### Manual Process
Use the command line to start the game.

```sh
$ cd Checkers
$ python start.py
```
or 
```sh
$ cd Checkers
$ chmod +x start.py && ./start.py
```

This version is not tested for Windows enviroments, but it should work! normally, if you accomplish 
with the required dependecies.

### Checkers US Rules

In order to develop our small checkers game, we  explore many different rulesets  [[1]](https://www.thespruce.com/play-checkers-using-standard-rules-409287),[[2]](https://en.wikipedia.org/wiki/Draughts)
after a long discution I agree to use the US version:
- Each player has 12 pieces 
- pieces move in one direction(toward opponent)
- pieces can only move diagonally 
- pieces that reach the end of the board becomes in king pieces
- king pieces can move in any direction 
- win by jumping over all opponent pieces

move : diagonally 1 empty space 
jump : diagonally 2 spaces 

### Architectural Pattern: MVC

#### Models
Store the state of the board movements, and all the Storage representations, perhaps the 
piece class is used to create a model for each piece.
The datastructure use to store the states is a list of list,we were reading all 
the posible data-structure to represent a checkers board  like they are :
- Piece List 
- Array2d based
- bit board 

because we're not worried about speed we can use the most simple ds, a list of list, this could be 
achive using the following snippet in python3.6

```python 
        array = []     
        size = 8
        machinePieces = 0
        playerPieces = 0
        for i in range (size):
            array.append([])
            for j in range (size):
                array[i].append(None)
```
The previous code give us how the Board Class creates the initialization where each 
position will be set to None, then we can use another iteration to start set the pieces 
over the board.

```sh
Board State
-----------------------------------------------
None| None| None| None| None| None| None| None| 
-----------------------------------------------
None| None| None| None| None| None| None| None| 
-----------------------------------------------
None| None| None| None| None| None| None| None| 
-----------------------------------------------
None| None| None| None| None| None| None| None| 
-----------------------------------------------
None| None| None| None| None| None| None| None| 
-----------------------------------------------
None| None| None| None| None| None| None| None| 
-----------------------------------------------
None| None| None| None| None| None| None| None| 
-----------------------------------------------
None| None| None| None| None| None| None| None| 
-----------------------------------------------
```


#### Views
This file generates all the graphical aspect for the game, it's mainly use to create 
the board visualization and show the board changes, we use PyQt4 and the available widgets
to set the board images.  I use multiple images to represent the current state. 

PyQt4 has many base class that can be use in order to create the Graphical User Inteface, for this game **I just implement the game for the option Player vs Machine**  and with four options :

    -  Quit
    -  Resign
    -  Start New Game
    -  Go Back 

Each option makes use of a button, that is personalized, and handle by signals when the button is clicked.

To create the board I create a  `QTableWidget(8,8)` and the for each cell I insert an ImgWidget a custom class create to put the image in each cell using drawPixmap method.


![Graphical User Interface](http://i.imgur.com/B07liTd.png)

#### Controller
Creates the board and control all the operation of the main application. This class makes all the movement and interaction with the views and the models posible, determine the valid moves for a piece and help the player and the machine with the implementation of the minimax and beta-alfa prunning algorith in order to get the maximum benefit for each one. 



### Development

Want to contribute? Great!
Open an issue and create a pull request for your fixes and new features

* Hector F. Jimenez S. , hfjimenez@utp.edu.co 
* Daniel Quiroz , dcquiroz@utp.edu.co(His Java Version is not for the final term project if not for the previous checkers game.)

### ToDos
-  Add Game Modes 
 - ~~Learn to play checkers.~~
 - ~~Create the sketch up of the game, get a list of objects and his interations between them~~
 - ~~Graphical mode !~~
 - Add Night Mode.
 - Think in m2m battles.[Pretty Slow with maximum depth equal to 5]


### Useful Resources

- MVC Explanation,https://realpython.com/blog/python/the-model-view-controller-mvc-paradigm-summarized-with-legos/
- PyQT Testing,https://www.youtube.com/watch?v=2fGPKPmQF-E&list=PLR2mMc_XnsCuuhN_wdnDxm9IUGCpGaTHk
- PyQt Tutorial, Lecture http://zetcode.com/gui/pyqt4/layoutmanagement/
- PyQt by Example, http://www.programcreek.com/python/example/55345/PyQt4.QtGui.QFont
- Trevor Paint, Minimax https://www.youtube.com/watch?v=fInYh90YMJU
- MIT Open CourseWare, Minimax https://www.youtube.com/watch?v=STjW3eH0Cik 


License
----
mozilla public license 2.0

**Free Software, Hell Yeah!**