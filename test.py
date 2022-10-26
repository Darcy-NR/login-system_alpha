import json

#Open json file in read mode, assign the array to a dictionary named accounts
with open("test-accounts.json", "r") as f:
    accounts = json.load(f)


print("Before Add: ")
print(accounts)
print("- - - - - - - - - -")

#Construct a dictionary for our new user (we could theoretically use input variables for these)
new_user = {'new_user' : [{'username': 'new_user', 'password': 'Y%z|%"oC@', 'email': '123Brown@gmail.com', 'next_login_msg': '', 'last_login': '2021-12-04', 'pwd_change': '2021-11-26'}]}
new_user1 = [{'username': 'new_user', 'password': 'Y%z|%"oC@', 'email': '123Brown@gmail.com', 'next_login_msg': '', 'last_login': '2021-12-04', 'pwd_change': '2021-11-26'}]

#Take the existing dictionary, attach the new dictionary to it
accounts["new_user"] = new_user1

print("After Add: ")
print(accounts)
print("- - - - - - - - - -")

print("Singleton: ")
print(accounts["new_user"])
print("- - - - - - - - - -")

#Dump the updated dictionary as JSON to our accounts JSON file
with open("test-accounts.json", "w") as f:
    json.dump(accounts, f)

