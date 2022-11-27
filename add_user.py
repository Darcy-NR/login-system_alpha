from pw_encryption import encryption
import datetime
import json

def add_user(sys_admin, username_text, password_text, email_text, password_changed, login):
    username_text.strip()
    password_text.strip()
    email_text.strip()

    today_date = str(datetime.date.today())
    #Open json file in read mode, assign the array to a dictionary named accounts
    with open("accounts.json", "r") as f:
        accounts = json.load(f)

    if login == True:
        #Construct a dictionary for our new user (we could theoretically use input variables for these)

        for item in accounts[username_text]:
            pwd_change = item.get("pwd_change")
            message = item.get("next_login_msg")
        new_user = [{'username': username_text, 'password': encryption(password_text, hashed="", encrypt=True, validate=False), 'email': email_text, 'next_login_msg': message, 'last_login': today_date, 'pwd_change': pwd_change}]
        
    #Take the existing dictionary, attach the new dictionary to it
        accounts[username_text] = new_user

        with open("accounts.json", "w") as f:
            json.dump(accounts, f, indent = 2)
        return

    elif password_changed == True:
                #Construct a dictionary for our new user (we could theoretically use input variables for these)

        for item in accounts[username_text]:
            last_login = item.get("last_login")
        new_user = [{'username': username_text, 'password': encryption(password_text, hashed="", encrypt=True, validate=False), 'email': email_text, 'next_login_msg': '', 'last_login': last_login, 'pwd_change': today_date }]
        
    #Take the existing dictionary, attach the new dictionary to it
        accounts[username_text] = new_user

        with open("accounts.json", "w") as f:
            json.dump(accounts, f, indent = 2)
        return

    else:
        #Construct a dictionary for our new user (we could theoretically use input variables for these)
        new_user = [{'username': username_text, 'password': encryption(password_text, hashed="", encrypt=True, validate=False), 'email': email_text, 'next_login_msg': '', 'last_login': today_date, 'pwd_change': today_date }]
        
    #Take the existing dictionary, attach the new dictionary to it
        accounts[username_text] = new_user

        with open("accounts.json", "w") as f:
            json.dump(accounts, f, indent = 2)

        return

def username_checker(username_text):

    with open("accounts.json", "r") as f:
        accounts = json.load(f)
        
        try:
            new_user = accounts[username_text]
        except:
            print("There ISN'T a user with this name already")
            return False
        else:
            print("There is a user with this name already")
            return True