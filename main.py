import curses
import datetime
import json
from curses import wrapper
from curses.textpad import Textbox, rectangle
from register import register
import time
from user_table_maker import user_table_maker
from validators import password_char_validate, password_validate, password_generator, is_account
from add_user import add_user

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

def systems_menu(stdscr):
    y = 1
    stdscr.clear()
    stdscr.addstr(1, 1, "Welcome Administrator", curses.A_REVERSE)
    stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    rectangle(stdscr, 0, 0, 7, 70)
    stdscr.addstr(3, 1, "Print User Table", curses.A_REVERSE)
    stdscr.addstr(4, 1, "Exit the App")
    
    while True:
        key = stdscr.getkey()
        if key == "KEY_UP":
            y += 1
        elif key == "KEY_DOWN":
            y -= 1
        elif key == "KEY_RIGHT" and y == 1:
            stdscr.clear()
            stdscr.addstr(1, 1, "Current User Table has been output to ~/user-tables/", curses.A_REVERSE)
            stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
            user_table_maker()
            stdscr.getkey()
            goodbye()
        elif key == "KEY_RIGHT" and y == 0:
            stdscr.clear()
            goodbye()

        if y == 1:
            stdscr.clear()
            stdscr.addstr(1, 1, "Welcome Administrator", curses.A_REVERSE)
            stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
            rectangle(stdscr, 0, 0, 7, 70)
            stdscr.addstr(3, 1, "Print User Table", curses.A_REVERSE)
            stdscr.addstr(4, 1, "Exit the App")
        elif y == 0:
            stdscr.clear()
            stdscr.addstr(1, 1, "Welcome Administrator", curses.A_REVERSE)
            stdscr.addstr(2, 1, "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
            rectangle(stdscr, 0, 0, 7, 70)
            stdscr.addstr(3, 1, "Print User Table")
            stdscr.addstr(4, 1, "Exit the App", curses.A_REVERSE)
        if y >= 1:
            y = 1
        elif y <= 0:
            y = 0

def logged_in(stdscr, sys_admin, username_text, password_text, email_text):
    stdscr.addstr(1, 1, "You have logged in", curses.A_REVERSE)
    if welcome_message:
        stdscr.addstr(2, 1, welcome_message)
    else:
        stdscr.addstr(2, 1, "Placeholder Welcome Message")
    stdscr.addstr(3, 1, "_ _ _ _ _ _ _ _ _ _ _")
    rectangle(stdscr, 0, 0, 3, 46,)
    stdscr.getch()
    if sys_admin == True:
        print("Systems admin")
        systems_menu(stdscr)
    else:
        add_user(stdscr, sys_admin, username_text, password_text, email_text, password_changed = False, login = True)

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
    today_date = str(datetime.date.today())

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
            email_text = account.get("email")

            #Compare input password to stored password

            if password == stored_pass:
                print("Provided Password DOES match the stored password")
                print(":>")
                global welcome_message
                welcome_message = account.get("next_login_msg")

                if account.get("username") == "SYS_ADMIN" and account.get("email") == "gelos@systemsadmin.com.au":
                    sys_admin = True
                else:
                    sys_admin = False
                logged_in(stdscr, sys_admin, username_text, password_text, email_text)
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

def select_reset_password_type(stdscr):
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
            reset_pass_username_view(stdscr, resetRand = True)
        elif key == "KEY_RIGHT" and y == 0:
            stdscr.clear()
            reset_pass_username_view(stdscr, resetRand = False)

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

    if password_validate(password_text) == True:
        sys_admin = False
        add_user(stdscr, sys_admin, username_text, password_text, email_text, password_changed = False, login = False)
        main(stdscr)
    else:
        stdscr.clear()
        register_new_user(stdscr)

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
    sys_admin = False

    # Add User and then redirect to new screen

    #This works but its not every syntatic, maybe try give the user some better feedback? Not really possible with a function so maybe just a blanket errorr
    if password_validate(password_text) == True:
        add_user(stdscr, sys_admin, username_text, password_text, email_text, password_changed = False, login = False)
        main(stdscr)
    else:
        stdscr.clear()
        register_new_user(stdscr)

def retrieve_account(username_text):
    # username_text.strip()
    with open("accounts.json", "r") as f:
        all_acc = json.load(f)
        singleton = all_acc[username_text]
    return singleton

def reset_pass_view(username_text, stdscr):
    stdscr.clear()
    retrieved_user = retrieve_account(username_text)
    #User wants their own password
    stdscr.refresh()
    stdscr.addstr(1, 1, "Please provide the email associated with this account, and a new password.", curses.A_REVERSE)
    stdscr.addstr(2, 1, "'Ctrl + G' to finish typing and move to the next box [Emacs]")
    stdscr.addstr(3, 1, "_ _ _ _ _ _ _ _ _ _ _")

    email_window = curses.newwin(1, 30, 10, 2)
    pass_window = curses.newwin(1, 30, 14, 2)
    email_box = Textbox(email_window)
    pass_box = Textbox(pass_window)
    stdscr.addstr(5, 1, username_text, curses.A_REVERSE)
    stdscr.addstr(6, 1, "_ _ _ _ _ _ _ _ _ _ _")
    stdscr.addstr(8, 1, "Email:", curses.A_REVERSE)
    stdscr.addstr(12, 1, "New Password:", curses.A_REVERSE)
    rectangle(stdscr, 9, 1, 11, 32)
    rectangle(stdscr, 13, 1, 15, 32)

    stdscr.refresh()
    email_box.edit()
    pass_box.edit()

    password_text = pass_box.gather().strip()
    email_text = email_box.gather().strip()

    if password_validate(password_text) == True:

        with open("accounts.json", "r") as f:
            all_acc = json.load(f)
    
        singleton = all_acc[username_text]
        
        for item in singleton:
            stored_email = item.get("email")
    
        if email_text == stored_email:
            print("This email matches the stored email :)")
            sys_admin = False
            add_user(stdscr, sys_admin, username_text, password_text, email_text, password_changed = True, login = False)
        else:
            stdscr.clear()
            register(stdscr)

    else:
        reset_pass_view(username_text, stdscr)
        # Again this works but its not very syntatic, this needs feedback once the app is finished

def reset_pass_RAND_view(username_text, stdscr):
    stdscr.clear()
    retrieved_user = retrieve_account(username_text)
    #User wants their own password
    stdscr.refresh()
    stdscr.addstr(1, 1, "Please provide the email associated with this account.", curses.A_REVERSE)
    stdscr.addstr(2, 1, "'Ctrl + G' to finish typing and move to the next box [Emacs]")
    stdscr.addstr(3, 1, "_ _ _ _ _ _ _ _ _ _ _")

    email_window = curses.newwin(1, 30, 10, 2)
    email_box = Textbox(email_window)
    stdscr.addstr(5, 1, username_text, curses.A_REVERSE)
    stdscr.addstr(6, 1, "_ _ _ _ _ _ _ _ _ _ _")
    stdscr.addstr(8, 1, "Email:", curses.A_REVERSE)
    rectangle(stdscr, 9, 1, 11, 32)

    stdscr.refresh()
    email_box.edit()

    stdscr.getch()


    # username_text = un_box.gather().strip()
    password_text = password_generator().strip()
    email_text = email_box.gather().strip()

    with open("accounts.json", "r") as f:
        all_acc = json.load(f)
    
    singleton = all_acc[username_text]
    for item in singleton:
        stored_email = item.get("email")
    
    if email_text == stored_email:
        print("This email matches the stored email :)")
        sys_admin = False
        add_user(stdscr, sys_admin, username_text, password_text, email_text, password_changed = True, login = False)
    else:
        stdscr.clear()
        register(stdscr)

    # Add User and then redirect to new screen

    stdscr.clear()
    main(stdscr)
    
def reset_pass_username_view(stdscr, resetRand):
    stdscr.refresh()
    stdscr.addstr(1, 1, "Please enter your username", curses.A_REVERSE)
    stdscr.addstr(2, 1, "'Ctrl + G' to finish typing [Emacs]")
    stdscr.addstr(3, 1, "_ _ _ _ _ _ _ _ _ _ _")

    un_window = curses.newwin(1, 30, 7, 2)
    pass_window = curses.newwin(1, 30, 11, 2)
    un_box = Textbox(un_window)
    stdscr.addstr(5, 1, "Username:", curses.A_REVERSE)
    rectangle(stdscr, 6, 1, 8, 32)
    stdscr.refresh()
    un_box.edit()

    username_text = un_box.gather().strip()

    stdscr.addstr(10, 1, "Username: ", curses.A_REVERSE)
    stdscr.addstr(11, 1, username_text + "||", curses.A_REVERSE)
    stdscr.getch()


    if is_account(username_text) == True and resetRand == False:
        reset_pass_view(username_text, stdscr)
    elif is_account(username_text) == True and resetRand == True:
        reset_pass_RAND_view(username_text, stdscr)
    else:
        # PLACEHOLDER
        print("No Such User TEST")
        exit()



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
            select_reset_password_type(stdscr)
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

