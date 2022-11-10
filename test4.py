import json
import datetime
import uuid

from prettytable import PrettyTable, MARKDOWN

def pass_hider(pass_chars):
    censored_pass = ""
    y = 0
    while y < pass_chars:
        censored_pass += "#"
        y += 1
    return censored_pass

today_date = str(datetime.date.today())

# stdscr.clear()

with open("accounts.json", "r") as f:
    
    accounts = json.load(f)
                
accountsTable = PrettyTable(['Username', 'Password', 'Email', 'Next Login Message', 'Last Login', 'Password Changed'])

for account in accounts:
    username_string = str(account)
    # print(username_string)
    user = accounts[username_string]
    # print(user)
    for item in user:
        pass_chars = len(item.get("password"))
        # print(item.get("username"))
        # print(item.get("password"))
        # print(item.get("email"))
        # print(item.get("next_login_msg"))
        # print(item.get("last_login"))
        # print(item.get("pwd_change"))
        accountsTable.add_row([item.get("username"),pass_hider(pass_chars) , item.get("email"), item.get("next_login_msg"), item.get("last_login"), item.get("pwd_change")])

accountsTable.set_style(MARKDOWN)

new_uuid = uuid.uuid4()

export_file = open(f"user-tables/{today_date}--{str(new_uuid)}--users-table.txt", "w")
print(accountsTable, file = export_file)

# print(accounts)