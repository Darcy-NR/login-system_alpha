import json
from pw_encryption import encryption
from datetime import datetime

def expiry_check(username_text,password_text, email_text):

    # Probably the most complicated algorithm in the app. We begin by assessing the current date in UTC. 00,00,01 as the date.

    nowdate = datetime.now().strftime('%Y-%m-%d')

    with open("accounts.json", "r") as f:
        accounts = json.load(f)
    # Open the user account, take the dates for their last password change
    for account in accounts[username_text]:
        pwd_change = account.get("pwd_change")
        next_login = account.get("next_login_msg")

    #Now take this UTC string, and run it through the datetime class method to strip UTC string and convert it back into a UNIX epoch integer
    nowdate_unix_time = datetime.timestamp(datetime.strptime(nowdate, "%Y-%m-%d"))

    stored_unix_time = datetime.timestamp(datetime.strptime(str(pwd_change), "%Y-%m-%d"))

    # Once we have that Unix interger, (which is minutes since Unix epoch) we can designate the two points, our warning time and our reset time from this.
    # Take the stored unix time of the password change, add 86400 minutes (24hrs) multiplied by 100, for warning, and 120, for cutoff date

    password_warning_date = stored_unix_time + (86400 * 100)
    password_cutoff_date = stored_unix_time + (86400 * 120)

    sanity_check = datetime.utcfromtimestamp(password_cutoff_date).strftime("%Y-%m-%d")


    #Now that we have those dates confirmed, we can take the current date in unixtime, subtract from it the password cutoff dates
    # and that difference remainder integer, once we dividie it by 24 hrs, should be a floating point number for how many days there are until the cut off date, which will be
    # used in a moment.
    days_difference = password_cutoff_date - nowdate_unix_time
    days_remaining = days_difference / 86400

    #Now check if the current unix interger is greater than or = to the unix interger for the password warning,
    if nowdate_unix_time >= password_warning_date:

        #If that is true, then check if the current day is greater than the password cut off date

        if nowdate_unix_time >= password_cutoff_date:
            #If that is true, then the password is expired, and the function returns false and will prompt the user on the views layer to reset their password by
            # routing them to the password reset functions.
            return False
        else:
            # Else, if only the warning date is true, we take that floating point number we just calculated above
            days_difference = password_cutoff_date - nowdate_unix_time
            days_remaining = days_difference / 86400

            #And we construct a warning message f-string literal, which takes in the floating point number, truncates it down to an integer, and then we write that to the next login message
            # so that the user when they login, will see this warning telling them to reset their password on the splash screen. 
            message = f"Your password will expire in {int(days_remaining)} days, please reset your password"
            updateUser = [{'username': username_text, 'password': encryption(password_text, hashed="", encrypt=True, validate=False), 'email': email_text, 'next_login_msg': message, 'last_login': account.get("last_login"), 'pwd_change': account.get("pwd_change")}]
            
            accounts[username_text] = updateUser
            with open("accounts.json", "w") as f:
                json.dump(accounts, f, indent = 2)
                #Once they're warned, return true and let them login
                return True
    else:
        #Else nothing is wrong with their password, and we let them login.
        return True
