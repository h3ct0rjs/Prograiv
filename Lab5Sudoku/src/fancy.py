#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Project Details: Part of Sudoku Generator,Solver.
#Lab5, Computer Programming IV
#File Details: Contains Colors, And Core functions
#feedback:hfjimenez@utp.edu.co
#    License Details:
#    Copyright (C) 2017  Hector F. Jimenez S.
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

import os
import sys
import  subprocess
import random

reset = '\x1b[0m'    # reset all colors to white on black
bold = '\x1b[1m'     # enable bold text
uline = '\x1b[4m'    # enable underlined text
nobold = '\x1b[22m'  # disable bold text
nouline = '\x1b[24m' # disable underlined text
red = '\x1b[31m'     # red text
green = '\x1b[32m'   # green text
blue = '\x1b[34m'    # blue text
cyan = '\x1b[36m'    # cyan text
white = '\x1b[37m'   # white text (use reset unless it's only temporary)

warning = "{}[!]{}".format(red, reset)
info = "{}[*]{}".format(green, reset)
__version__="0.2"               
__author__='Hector F. Jimenez S.'
__email__='hfjimenez@utp.edu.co'


def signalHandler(signal, frame):
    warning("Ctrl-C Para cerrar !")

def menu():
    subprocess.call(['clear'],shell=False)#clean term
    banner()
    print("""
    {}Select level of difficulty[1-4] :{}
    {}Easy
    {}Medium
    {}Insane
    {}Hardcore
    """.format(bold,reset,info,info,info,info))

    
    


# Random Banner
def banner():
    target = random.randrange(1,4)
    lb=[
    """
    ███████╗██╗   ██╗██████╗  ██████╗ ██╗  ██╗██╗   ██╗
    ██╔════╝██║   ██║██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║
    ███████╗██║   ██║██║  ██║██║   ██║█████╔╝ ██║   ██║
    ╚════██║██║   ██║██║  ██║██║   ██║██╔═██╗ ██║   ██║
    ███████║╚██████╔╝██████╔╝╚██████╔╝██║  ██╗╚██████╔╝
    ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ """,
    """
    .▄▄ · ▄• ▄▌·▄▄▄▄       ▄ •▄ ▄• ▄▌
    ▐█ ▀. █▪██▌██▪ ██▪     █▌▄▌▪█▪██▌
    ▄▀▀▀█▄█▌▐█▌▐█· ▐█▌▄█▀▄ ▐▀▀▄·█▌▐█▌
    ▐█▄▪▐█▐█▄█▌██. ██▐█▌.▐▌▐█.█▌▐█▄█▌
     ▀▀▀▀  ▀▀▀ ▀▀▀▀▀• ▀█▄▀▪·▀  ▀ ▀▀▀ """,
     """
      ▄▀▀▀▀▄  ▄▀▀▄ ▄▀▀▄  ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▄ █  ▄▀▀▄ ▄▀▀▄ 
    █ █   ▐ █   █    █ █ ▄▀   █ █      █ █  █ ▄▀ █   █    █ 
       ▀▄   ▐  █    █  ▐ █    █ █      █ ▐  █▀▄  ▐  █    █  
    ▀▄   █    █    █     █    █ ▀▄    ▄▀   █   █   █    █   
     █▀▀▀      ▀▄▄▄▄▀   ▄▀▄▄▄▄▀   ▀▀▀▀   ▄▀   █     ▀▄▄▄▄▀  
     ▐                 █     ▐           █    ▐             
                       ▐                 ▐                  
     """,
     """      
      ██████  █    ██▓█████▄  ▒█████   ██ ▄█▀ █    ██ 
    ▒██    ▒  ██  ▓██▒██▀ ██▌▒██▒  ██▒ ██▄█▒  ██  ▓██▒
    ░ ▓██▄   ▓██  ▒██░██   █▌▒██░  ██▒▓███▄░ ▓██  ▒██░
      ▒   ██▒▓▓█  ░██░▓█▄   ▌▒██   ██░▓██ █▄ ▓▓█  ░██░
    ▒██████▒▒▒▒█████▓░▒████▓ ░ ████▓▒░▒██▒ █▄▒▒█████▓ 
    ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ 
    ░ ░▒  ░ ░░░▒░ ░ ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ 
    ░  ░  ░   ░░░ ░ ░ ░ ░  ░ ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ 
          ░     ░       ░        ░ ░  ░  ░      ░     
     """
    ]
    print("{}{}\n\t\t{},\n\t Solver and Generator 2017,UTP\n\t\t{}\n{}".format(red,  
        lb[target],__author__,__email__,reset))
