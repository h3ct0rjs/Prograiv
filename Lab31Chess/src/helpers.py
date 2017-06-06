#!/usr/bin/env python3
#-encoding:utf-8-*-
"""
"""
def index2pos(index):
    """

    """
    return (index%8,math.floor(index/8)*8);

def pos2index(pos):
    """
    
    """
    return pos[0] + pos[1]*8;

def str2index(str):
    """
    
    """
    return pos2index(str2pos(str));
    
def str2pos(str):
    """
    
    """
    return ((ord(str.upper()[0])-alphaValueOffset) % 8,int(str[1])-1);

def pos2str(pos):
    """
    
    """
    return chr( (pos[0]-alphaValueOffset) % 8).upper() + str(pos[1]+1);

def getMove():
    """
    
    """
    while(True):
        try:
            in1 = input("Next move: ").split(" ");
            p1 = str2pos(in1[0]);
            p2 = str2pos(in1[1]);
            return p1,p2;
        except Exception:
            print("Bad input")