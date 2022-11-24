import json
from pw_encryption import encryption
from datetime import datetime

def expiry_check(username_text,password_text, email_text):

    nowdate = datetime.now().strftime('%Y-%m-%d')

    with open("accounts.json", "r") as f:
        accounts = json.load(f)

    for account in accounts[username_text]:
        pwd_change = account.get("pwd_change")
        next_login = account.get("next_login_msg")


    nowdate_unix_time = datetime.timestamp(datetime.strptime(nowdate, "%Y-%m-%d"))

    stored_unix_time = datetime.timestamp(datetime.strptime(str(pwd_change), "%Y-%m-%d"))

    password_warning_date = stored_unix_time + (86400 * 100)
    password_cutoff_date = stored_unix_time + (86400 * 120)

    sanity_check = datetime.utcfromtimestamp(password_cutoff_date).strftime("%Y-%m-%d")

    days_difference = password_cutoff_date - nowdate_unix_time
    days_remaining = days_difference / 86400

    if nowdate_unix_time >= password_warning_date:

        if nowdate_unix_time >= password_cutoff_date:
            return False
        else:
            days_difference = password_cutoff_date - nowdate_unix_time
            days_remaining = days_difference / 86400

            message = f"Your password will expire in {int(days_remaining)} days, please reset your password"
            updateUser = [{'username': username_text, 'password': encryption(password_text, hashed="", encrypt=True, validate=False), 'email': email_text, 'next_login_msg': message, 'last_login': account.get("last_login"), 'pwd_change': account.get("pwd_change")}]
            
            accounts[username_text] = updateUser
            with open("accounts.json", "w") as f:
                json.dump(accounts, f, indent = 2)
                return True
    else:
        return True
