import json
from prettytable import PrettyTable, MARKDOWN
import uuid
import datetime

def pass_hider(pass_chars):

#Simple function that takes in an integer for the len of the password, and then replaces it with a #, so when the tables are output the passwords are censored.

    censored_pass = ""
    y = 0
    while y < pass_chars:
        censored_pass += "#"
        y += 1
    return censored_pass

def user_table_maker():

    #Creating a UUID and today.date, these are used so each new table generated is sorted automatically in file systems, but also ensures every and each table has a unique id

    today_date = str(datetime.date.today())
    new_uuid = uuid.uuid4()

    with open("accounts.json", "r") as f:
        
        accounts = json.load(f)
                    
    #Make a call on the PrettyTable method with this input, so it knows to expect the rows we feed it to be like this.
    accountsTable = PrettyTable(['Username', 'Password', 'Email', 'Next Login Message', 'Last Login', 'Password Changed'])

    #Now loop over the accounts variable -- This is a JSON obbject tree and thus each singleton in the accounts.json, is a singular json object of AN account.
    # ergo feed that into its own for loop
    for account in accounts:
        username_string = str(account)
        user = accounts[username_string]
        for item in user:
            # If we loop over an account object, we get the individual data points stored in the account as json objects. And so we can use (singleton.GET) to parse individual datapoints.
            pass_chars = len(item.get("password"))
            accountsTable.add_row([item.get("username"),pass_hider(pass_chars) , item.get("email"), item.get("next_login_msg"), item.get("last_login"), item.get("pwd_change")])
            # Every time I access and parse the accounts.json it follows this for loop system pretty much identically.

    accountsTable.set_style(MARKDOWN)
    #Set the format method for the table to MARKDOWN (prioritized for .md files but that also means it looks nicer in .txt) 
    #Export that formatted text string to a file in the user-tables file, attach the unique name and date to it.
    export_file = open(f"user-tables/{today_date}--{str(new_uuid)}--users-table.txt", "w")
    print(accountsTable, file = export_file)

def terminal_showtable_build():

    with open("accounts.json", "r") as f:
    
        #Read the table again like before.

        accounts = json.load(f)
                    
    accountsTable = PrettyTable(['Username', 'Password', 'Email', 'Next Login Message', 'Last Login', 'Password Changed'])

    for account in accounts:
        username_string = str(account)
        user = accounts[username_string]
        for item in user:
            pass_chars = len(item.get("password"))
            accountsTable.add_row([item.get("username"),pass_hider(pass_chars) , item.get("email"), item.get("next_login_msg"), item.get("last_login"), item.get("pwd_change")])

    accountsTable.set_style(MARKDOWN)

    #But instead this time output to terminal, because the sys admin is going to use it.

    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print(accountsTable)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("Login Message can be edited")
    print("Please enter the username of the user you wish to edit:")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    user_edit = input("Username: ")

    #Input a name, run a TRY-CATCH on that username, if exception, then there is no user object, so try again. Else move on

    try:
        single_user = accounts[user_edit]
    except:
        terminal_showtable_build()

    # Display a single row table of that selected user, just to give the end user a little more syntatic feedback that they made a confirmation

    SingleRowTable = PrettyTable(['Username', 'Password', 'Email', 'Next Login Message', 'Last Login', 'Password Changed'])
    for item in single_user:
        pass_chars = len(item.get("password"))
        SingleRowTable.add_row([item.get("username"),pass_hider(pass_chars) , item.get("email"), item.get("next_login_msg"), item.get("last_login"), item.get("pwd_change")])
    print(SingleRowTable)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("Enter in new user message.")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    new_next_message = input("Message:")

    #Enter in the new login message and then run a simple constructor to save the new user message to their account in accounts.json

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

        # Waits for an input, just to make sure the sys admin sees the confirmation message, before returning them to the systems menu automatically.