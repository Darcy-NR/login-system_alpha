import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from select import select
from tkinter import Menu
from xmlrpc.client import FastParser

def register(stdscr):
    stdscr.addstr(1, 1, "This is where the register will be eventually", curses.A_REVERSE)
    stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _")
    rectangle(stdscr, 0, 0, 3, 46,)
    stdscr.getch()

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    # User lands on cursor bar to select if they want to register an account or reset password or return to main menu

    # User shifts down to option, hits -> to select
    
    # Like main menu, shift coordinates to Y value, what Y == when user hits -> cooresponds to what function is run.

    # IF register

    #     Run a function for user textbox, password and option for 2FA as well as offer to randomly generate password for them based on checkbox
    #         if TRUE than it either runs one of three modules/or maybe it runs the same one but with arguements I dunno what is gonna be faster
    #         these stats are then passed into a creatUser Class that runs a method based on provided arguements
        
    # IF reset password

    #     Run a function that takes username and checks the library for that username, checks if the 2FA is set to true

    #     If 2FA flag is true => Ask for it and refuse to reset password if they cannot
        
    #     Else ==> User is just allowed to reset password I dunno, probably should check instructions later but this is for a vertical slice

    # IF return to main Menu
    
    #     Runs the main() function