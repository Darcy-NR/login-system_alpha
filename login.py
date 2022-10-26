import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

def login(stdscr):
    stdscr.refresh()
    stdscr.addstr(1, 1, "Please enter your username and password", curses.A_REVERSE)
    stdscr.addstr(2, 1, "'Ctrl + G' to finish typing and move to the next box [Emacs]")
    stdscr.addstr(3, 1, "_ _ _ _ _ _ _ _ _ _ _")

    un_window = curses.newwin(1, 30, 7, 2)
    pass_window = curses.newwin(1, 30, 11, 2)
    un_box = Textbox(un_window)
    pass_box = Textbox(pass_window)
    stdscr.addstr(5, 1, "Username:", curses.A_REVERSE)
    stdscr.addstr(9, 1, "Password:", curses.A_REVERSE)
    rectangle(stdscr, 6, 1, 8, 32)
    rectangle(stdscr, 10, 1, 12, 32)
    stdscr.refresh()
    un_box.edit()
    pass_box.edit()

    username_text = un_box.gather()
    password_text = pass_box.gather()


    #These are placeholders, this should be removed in production
    stdscr.addstr(13, 1, "Username: " + username_text)
    stdscr.addstr(14, 1, "Password: " + password_text)
    
    stdscr.getch()
    stdscr.clear()

wrapper(login)

def login(username_text, password_text):
    
    
    # User enters user name and password via Emacs

    # Once completed the provided variables are put into a Login Class (or maybe a function/ I dunno it might not really need a class), where their inputs are run against the library

    # If Login() == TRUE

        # User is put into a splash screen with a randomly generated welcome message

    # IF Login() == FALSE

        # User has a "hasFailed" flag applied to their session, is asked to try again and is warned that they have X tries remaining =+ to hasFailed

        # If user fails 3 times (inclusive) => User is pushed to the reset password function to reset password.