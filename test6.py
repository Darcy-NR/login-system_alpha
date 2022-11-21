from datetime import datetime

nowdate = datetime.now().strftime('%Y-%m-%d')
pwd_change = "2022-07-15"

nowdate_unix_time = datetime.timestamp(datetime.strptime(nowdate, "%Y-%m-%d"))

stored_unix_time = datetime.timestamp(datetime.strptime(pwd_change, "%Y-%m-%d"))

print(nowdate_unix_time)
print(stored_unix_time)

password_warning_date = stored_unix_time + (86400 * 100)
password_cutoff_date = stored_unix_time + (86400 * 120)

print(password_cutoff_date)

sanity_check = datetime.utcfromtimestamp(password_cutoff_date).strftime("%Y-%m-%d")
print(sanity_check)

days_difference = password_cutoff_date - nowdate_unix_time
days_remaining = days_difference / 86400

print(int(days_remaining))

if nowdate_unix_time >= password_warning_date:

    days_difference = password_cutoff_date - nowdate_unix_time
    days_remaining = days_difference / 86400

    print(f"Your password will expire in {int(days_remaining)} days, please reset your password")

    if nowdate_unix_time >= password_cutoff_date:
        print("Your password has expired")
    else:
        pass
    
else:
    pass
