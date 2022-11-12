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