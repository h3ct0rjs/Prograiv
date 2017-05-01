#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Details:views.py, main
# ParcialII, Computer Programming IV
# feedback:hfjimenez@utp.edu.co,dcquiroz@utp.edu.co
# Features::
#   Mouse selections
#   Per token show the list of Sugestions
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; Applies version 2 of the License.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
from src.graphics import *


class BoardDrawer(object):
    """ Draw the checkers Game 
    Setup all the visualization part of the checkers,creating 
    windows, update views, making visual movements and colored sugestions

    ToDO: 
    Create the visual board using graphics.py 
    Check how to send the posx,posy for the mouse
    Add Color suggestion based on the color 
    Create the tokens or pieces using circle object
    All the data is store in the models, so make use of that info.
    """

    def __init__(self):
        self.x = self.size * TamCasilla
        self.y = self.size * TamCasilla
        self.win = GraphWin('Checkers Game', self.x, self.y, autoflush=False)


