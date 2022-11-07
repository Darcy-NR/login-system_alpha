import curses
import datetime
import json
from curses import wrapper
from curses.textpad import Textbox, rectangle
from register import register
import time
import random

fails = 0
start_time = time.time()

def main(stdscr):
    y = 0
    stdscr.addstr(1, 1, "Welcome to the LOGIN", curses.A_REVERSE)
    stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _")
    rectangle(stdscr, 0, 0, 7, 26,)
    stdscr.clear()
    stdscr.addstr(1, 1, "Welcome to the APP", curses.A_REVERSE)
    stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _")
    rectangle(stdscr, 0, 0, 7, 26, )
    stdscr.addstr(3, 1, "Login")
    stdscr.addstr(4, 1, "Register / Reset Password", curses.A_REVERSE)
    stdscr.addstr(5, 1, "Exit")
    while True:
        key = stdscr.getkey()
        if key == "KEY_UP":
            y += 1
        elif key == "KEY_DOWN":
            y -= 1
        elif key == "KEY_RIGHT" and y == 1:
            stdscr.clear()
            login(stdscr)
        elif key == "KEY_RIGHT" and y == 0:
            stdscr.clear()
            register(stdscr)
        elif key == "KEY_RIGHT" and y == -1:
                goodbye()
        stdscr.refresh()

        if y == 1:
            stdscr.clear()
            stdscr.addstr(1, 1, "Welcome to the APP", curses.A_REVERSE)
            stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _")
            rectangle(stdscr, 0, 0, 7, 26, )
            stdscr.addstr(3, 1, "Login", curses.A_REVERSE)
            stdscr.addstr(4, 1, "Register / Reset Password")
            stdscr.addstr(5, 1, "Exit")
        elif y == 0:
            stdscr.clear()
            stdscr.addstr(1, 1, "Welcome to the APP", curses.A_REVERSE)
            stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _")
            rectangle(stdscr, 0, 0, 7, 26, )
            stdscr.addstr(3, 1, "Login")
            stdscr.addstr(4, 1, "Register / Reset Password", curses.A_REVERSE)
            stdscr.addstr(5, 1, "Exit")
        elif y == -1:
            stdscr.clear()
            stdscr.addstr(1, 1, "Welcome to the APP", curses.A_REVERSE)
            stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _")
            rectangle(stdscr, 0, 0, 7, 26, )
            stdscr.addstr(3, 1, "Login")
            stdscr.addstr(4, 1, "Register / Reset Password")
            stdscr.addstr(5, 1, "Exit", curses.A_REVERSE)
        if y >= 1:
            y = 1
        elif y <= -1:
            y = -1
        stdscr.refresh()

def logged_in(stdscr):
    stdscr.addstr(1, 1, "You have logged in", curses.A_REVERSE)
    if welcome_message:
        stdscr.addstr(2, 1, welcome_message)
    else:
        stdscr.addstr(2, 1, "Placeholder Welcome Message")
    stdscr.addstr(3, 1, "_ _ _ _ _ _ _ _ _ _ _")
    rectangle(stdscr, 0, 0, 3, 46,)
    stdscr.getch()

def failed_login(stdscr, fails):
    if fails == 1:
        stdscr.addstr(1, 1, "That Password is Invalid", curses.A_REVERSE)
        stdscr.addstr(2, 1, "You have 2 tries remaining") #I want this to change colour or be red or something
        stdscr.addstr(3, 1, "_ _ _ _ _ _ _ _ _ _ _")
        rectangle(stdscr, 0, 0, 3, 46,)
        stdscr.getch()
    elif fails == 2:
        stdscr.addstr(1, 1, "That Password is Invalid", curses.A_REVERSE)
        stdscr.addstr(2, 1, "You have 1 try remaining") #I want this to change colour or be red or something
        stdscr.addstr(3, 1, "_ _ _ _ _ _ _ _ _ _ _")
        rectangle(stdscr, 0, 0, 3, 46,)
        stdscr.getch()

def goodbye():
    global start_time
    curses.endwin()
    end_time = time.time()
    use_time = end_time - start_time
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("Thank you for using our services, please come back soon!")
    print("Active for: ")
    print(time.strftime("%H:%M:%S", time.gmtime(use_time)))
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    time.sleep(2.5)
    exit()

# // PASSWORD VALIDATION //

def password_char_validate(password):
        #Prepare Bools
        special = False
        digit = False
        lowCaps = False
        upCaps = False

        #Loop over each character in the password to check these four conditionals
        for char in password:
            if(not char.isalnum()):
                special = True
            if(char.isdigit()):
                digit = True
            if(char.islower()):
                lowCaps = True
            if(char.isupper()):
                upCaps = True
        # Return true only if all four conditionals are true
        return special and digit and lowCaps and upCaps 


def password_validate(password):
    if len(password) >= 8:
        if password_char_validate(password) == True:
            return True
        else:
            return False
    else:
        return False

# // PASSWORD VALIDATION //

def password_generator():
    salt = "wxyz12ABCDEFGH3abcdefgIJKLMNO4567hijklm89nopPQRSTUVqrstuvWXYZ!@#$%^&*()_-+}{><]["

    rand_password = ""

    while password_char_validate(rand_password) == False:
        x = 0
        rand_password = ""

        while x < 8:
                
                password_char = random.choice(salt)
                rand_password = rand_password + password_char
                x += 1
    
    return rand_password

def failed_counter(stdscr):
    global fails
    fails += 1
    if fails == 3:
        fails = 0
        register(stdscr)
    else:
        failed_login(stdscr, fails)
    return

def login_func(stdscr, username_text, password_text):

    # Strip trailing space from input (also probably sanitize)
    username = username_text.strip()
    password = password_text.strip()

    #Retrieve accounts.json as dictionary
    with open("accounts.json", "r") as f:
        accounts = json.load(f)
    
    try:
        # Exception Handling Tree, if there is no username WHERE input...
        account_result = accounts[username]
    except:
       # then it will throw a key error therefore there is no account with that username, else...
        print("there isn't an account with this username")
    else:
        # else there is a username with that account
        print("There is an account with this username")

        for account in accounts[username]:
            # Write the account[username] result to a for loop
            
            # Write password to .get("password")
            stored_pass = account.get("password")

            #Compare input password to stored password

            if password == stored_pass:
                print("Provided Password DOES match the stored password")
                print(":>")
                global welcome_message
                welcome_message = account.get("next_login_msg")
                logged_in(stdscr)
            else:
                failed_counter(stdscr)

def select_password_type(stdscr):
    #User needs to select if they want to generate their own password or have it randomly generated
    y = 1
    stdscr.clear()
    stdscr.addstr(1, 1, "Do you want us to randomly generate you a password or, enter your own", curses.A_REVERSE)
    stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    rectangle(stdscr, 0, 0, 7, 70)
    stdscr.addstr(3, 1, "Randomly Generated Password", curses.A_REVERSE)
    stdscr.addstr(4, 1, "Enter your own")
    
    while True:
        key = stdscr.getkey()
        if key == "KEY_UP":
            y += 1
        elif key == "KEY_DOWN":
            y -= 1
        elif key == "KEY_RIGHT" and y == 1:
            stdscr.clear()
            register_new_user_RAND(stdscr)
        elif key == "KEY_RIGHT" and y == 0:
            stdscr.clear()
            register_new_user(stdscr)

        if y == 1:
            stdscr.clear()
            stdscr.addstr(1, 1, "Do you want us to randomly generate you a password or, enter your own", curses.A_REVERSE)
            stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
            rectangle(stdscr, 0, 0, 7, 70)
            stdscr.addstr(3, 1, "Randomly Generated Password", curses.A_REVERSE)
            stdscr.addstr(4, 1, "Enter your own")
        elif y == 0:
            stdscr.clear()
            stdscr.addstr(1, 1, "Do you want us to randomly generate you a password or, enter your own", curses.A_REVERSE)
            stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
            rectangle(stdscr, 0, 0, 7, 70)
            stdscr.addstr(3, 1, "Randomly Generated Password")
            stdscr.addstr(4, 1, "Enter your own", curses.A_REVERSE)
        if y >= 1:
            y = 1
        elif y <= 0:
            y = 0

def add_user(username_text, password_text, email_text):
    username_text.strip()
    password_text.strip()
    email_text.strip()

    today_date = str(datetime.date.today())
    #Open json file in read mode, assign the array to a dictionary named accounts
    with open("accounts.json", "r") as f:
        accounts = json.load(f)

    #Construct a dictionary for our new user (we could theoretically use input variables for these)
    new_user = [{'username': username_text, 'password': password_text, 'email': email_text, 'next_login_msg': '', 'last_login': today_date, 'pwd_change': today_date }]
    
#Take the existing dictionary, attach the new dictionary to it
    accounts[username_text] = new_user

    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent = 2)

    print(new_user)
    print("- - - - - - - - - - - -")
    print(accounts)
    exit()

def reset_password(username_text, password_text, email_text):
    pass
    # - Take input
    # - Construct object
    # - Presumably, I can just do what I did with add user, but set the object to == the username and that should overwrite the account?
        # - That also means I can still demand an email, which I can pretend is a security feature (if you need to reset you need to know your email?)
def register_new_user_RAND(stdscr):
    #User wants a random password
    stdscr.refresh()
    stdscr.addstr(1, 1, "Please enter a valid username and password", curses.A_REVERSE)
    stdscr.addstr(2, 1, "'Ctrl + G' to finish typing and move to the next box [Emacs]")
    stdscr.addstr(3, 1, "_ _ _ _ _ _ _ _ _ _ _")

    un_window = curses.newwin(1, 30, 7, 2)
    pass_window = curses.newwin(1, 30, 11, 2)
    un_box = Textbox(un_window)
    email_box = Textbox(pass_window)
    stdscr.addstr(5, 1, "Username:", curses.A_REVERSE)
    stdscr.addstr(9, 1, "Email:", curses.A_REVERSE)
    rectangle(stdscr, 6, 1, 8, 32)
    rectangle(stdscr, 10, 1, 12, 32)
    stdscr.refresh()
    un_box.edit()
    email_box.edit()

    username_text = un_box.gather().strip()
    password_text = password_generator().strip()
    email_text = email_box.gather().strip()


    #These are placeholders, this should be removed in production
    stdscr.addstr(13, 1, "Username: " + username_text)
    stdscr.addstr(14, 1, "Email: " + email_text)
    stdscr.addstr(15, 1, "Password: " + password_text)
    
    stdscr.getch()

    add_user(username_text, password_text, email_text)

    # Add User and then redirect to new screen

    stdscr.clear()
    main(stdscr)

def register_new_user(stdscr):
    #User wants their own password
    stdscr.refresh()
    stdscr.addstr(1, 1, "Please enter a valid username, password and email address.", curses.A_REVERSE)
    stdscr.addstr(2, 1, "'Ctrl + G' to finish typing and move to the next box [Emacs]")
    stdscr.addstr(3, 1, "_ _ _ _ _ _ _ _ _ _ _")

    un_window = curses.newwin(1, 30, 7, 2)
    pass_window = curses.newwin(1, 30, 11, 2)
    email_window = curses.newwin(1, 30, 15, 2)
    un_box = Textbox(un_window)
    pass_box = Textbox(pass_window)
    email_box = Textbox(email_window)
    stdscr.addstr(5, 1, "Username:", curses.A_REVERSE)
    stdscr.addstr(9, 1, "Password:", curses.A_REVERSE)
    stdscr.addstr(13, 1, "Email:", curses.A_REVERSE)
    rectangle(stdscr, 6, 1, 8, 32)
    rectangle(stdscr, 10, 1, 12, 32)
    rectangle(stdscr, 14, 1, 16, 32)
    stdscr.refresh()
    un_box.edit()
    pass_box.edit()
    email_box.edit()

    username_text = un_box.gather().strip()
    password_text = pass_box.gather().strip()
    email_text = email_box.gather().strip()


    #These are placeholders, this should be removed in production
    stdscr.addstr(19, 1, "Username: " + username_text)
    stdscr.addstr(20, 1, "Password: " + password_text)
    stdscr.addstr(21, 1, "Email: " + email_text)
    
    stdscr.getch()

    add_user(username_text, password_text, email_text)

    # Add User and then redirect to new screen

    stdscr.clear()
    main(stdscr)

    #This works but its not every syntatic, maybe try give the user some better feedback? Not really possible with a function so maybe just a blanket errorr
    if password_validate(password_text) == True:
        stdscr.clear()
        main(stdscr)
    else:
        stdscr.clear()
        register_new_user(stdscr)
    

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

    username_text = un_box.gather().strip()
    password_text = pass_box.gather().strip()


    #These are placeholders, this should be removed in production
    stdscr.addstr(13, 1, "Username: " + username_text + "|")
    stdscr.addstr(14, 1, "Password: " + password_text + "|")
    
    stdscr.getch()
    stdscr.clear()
    login_func(stdscr, username_text, password_text)

def register(stdscr):
    y = 0
    stdscr.addstr(1, 1, "Register or Reset Password?", curses.A_REVERSE)
    stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _")
    rectangle(stdscr, 0, 0, 7, 27,)
    stdscr.addstr(3, 1, "Register New Account")
    stdscr.addstr(4, 1, "Reset Password", curses.A_REVERSE)
    stdscr.addstr(5, 1, "Return to Main Menu")
    
    while True:
        key = stdscr.getkey()
        if key == "KEY_UP":
            y += 1
        elif key == "KEY_DOWN":
            y -= 1
        elif key == "KEY_RIGHT" and y == 1:
            stdscr.clear()
            select_password_type(stdscr)
        elif key == "KEY_RIGHT" and y == 0:
            stdscr.clear()
            pass
        elif key == "KEY_RIGHT" and y == -1:
            stdscr.clear()
            main(stdscr)

        if y == 1:
            stdscr.clear()
            stdscr.addstr(1, 1, "Register or Reset Password?", curses.A_REVERSE)
            stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _")
            rectangle(stdscr, 0, 0, 7, 27, )
            stdscr.addstr(3, 1, "Register New Account", curses.A_REVERSE)
            stdscr.addstr(4, 1, "Reset Password")
            stdscr.addstr(5, 1, "Return to Main Menu")
        elif y == 0:
            stdscr.clear()
            stdscr.addstr(1, 1, "Register or Reset Password?", curses.A_REVERSE)
            stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _")
            rectangle(stdscr, 0, 0, 7, 27, )
            stdscr.addstr(3, 1, "Register New Account")
            stdscr.addstr(4, 1, "Reset Password", curses.A_REVERSE)
            stdscr.addstr(5, 1, "Return to Main Menu")
        elif y == -1:
            stdscr.clear()
            stdscr.addstr(1, 1, "Register or Reset Password?", curses.A_REVERSE)
            stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _")
            rectangle(stdscr, 0, 0, 7, 27, )
            stdscr.addstr(3, 1, "Register New Account")
            stdscr.addstr(4, 1, "Reset Password")
            stdscr.addstr(5, 1, "Return to Main Menu", curses.A_REVERSE)
        if y >= 1:
            y = 1
        elif y <= -1:
            y = -1


    
wrapper(main)




#MOTD generated from a prexisting library should go here