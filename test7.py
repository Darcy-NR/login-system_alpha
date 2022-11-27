import json

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


username_text = "TestInputt"

if username_checker(username_text) == False:
    print("ISN'T USER")
else:
    print("IS USER")