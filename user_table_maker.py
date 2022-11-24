import json
from prettytable import PrettyTable, MARKDOWN
import uuid
import datetime

def pass_hider(pass_chars):
    censored_pass = ""
    y = 0
    while y < pass_chars:
        censored_pass += "#"
        y += 1
    return censored_pass

def user_table_maker():
    today_date = str(datetime.date.today())
    new_uuid = uuid.uuid4()

    with open("accounts.json", "r") as f:
        
        accounts = json.load(f)
                    
    accountsTable = PrettyTable(['Username', 'Password', 'Email', 'Next Login Message', 'Last Login', 'Password Changed'])

    for account in accounts:
        username_string = str(account)
        user = accounts[username_string]
        for item in user:
            pass_chars = len(item.get("password"))
            accountsTable.add_row([item.get("username"),pass_hider(pass_chars) , item.get("email"), item.get("next_login_msg"), item.get("last_login"), item.get("pwd_change")])

    accountsTable.set_style(MARKDOWN)

    export_file = open(f"user-tables/{today_date}--{str(new_uuid)}--users-table.txt", "w")
    print(accountsTable, file = export_file)

def terminal_showtable_build():

    with open("accounts.json", "r") as f:
    
        accounts = json.load(f)
                    
    accountsTable = PrettyTable(['Username', 'Password', 'Email', 'Next Login Message', 'Last Login', 'Password Changed'])

    for account in accounts:
        username_string = str(account)
        user = accounts[username_string]
        for item in user:
            pass_chars = len(item.get("password"))
            accountsTable.add_row([item.get("username"),pass_hider(pass_chars) , item.get("email"), item.get("next_login_msg"), item.get("last_login"), item.get("pwd_change")])

    accountsTable.set_style(MARKDOWN)

    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print(accountsTable)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("Login Message can be edited")
    print("Please enter the username of the user you wish to edit:")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    user_edit = input("Username: ")

    try:
        single_user = accounts[user_edit]
    except:
        terminal_showtable_build()

    SingleRowTable = PrettyTable(['Username', 'Password', 'Email', 'Next Login Message', 'Last Login', 'Password Changed'])
    for item in single_user:
        pass_chars = len(item.get("password"))
        SingleRowTable.add_row([item.get("username"),pass_hider(pass_chars) , item.get("email"), item.get("next_login_msg"), item.get("last_login"), item.get("pwd_change")])
    print(SingleRowTable)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("Enter in new user message.")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    new_next_message = input("Message:")

    for item in single_user:
        new_user = [{'username': item.get("username"), 'password': item.get("password"), 'email': item.get("email"), 'next_login_msg': new_next_message, 'last_login': item.get("last_login"), 'pwd_change': item.get("pwd_change") }]
            
        #Take the existing dictionary, attach the new dictionary to it
        accounts[user_edit] = new_user

        with open("accounts.json", "w") as f:
            json.dump(accounts, f, indent = 2)

        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        print("User Message Updated:")
        print("Enter any key to continue.")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        input()