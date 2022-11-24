import random
import json
import re

def password_char_validate(password):
        #Prepare Bools
        special = False
        digit = False
        lowCaps = False
        upCaps = False

        #Loop over each character in the password to check these four conditionals
        for char in password:
            if(not char.isalnum()):
                special = True
            if(char.isdigit()):
                digit = True
            if(char.islower()):
                lowCaps = True
            if(char.isupper()):
                upCaps = True
        # Return true only if all four conditionals are true
        return special and digit and lowCaps and upCaps 


def password_validate(password):
    if len(password) >= 8:
        if password_char_validate(password) == True:
            return True
        else:
            return False
    else:
        return False

def password_generator():
    salt = "wxyz12ABCDEFGH3abcdefgIJKLMNO4567hijklm89nopPQRSTUVqrstuvWXYZ!@#$%^&*()_-+}{><]["

    rand_password = ""

    while password_char_validate(rand_password) == False:
        x = 0
        rand_password = ""

        while x < 8:
                
                password_char = random.choice(salt)
                rand_password = rand_password + password_char
                x += 1
    
    return rand_password

def is_account(username_text):
    with open("accounts.json", "r") as f:
        all_acc = json.load(f)
    try:
        singleton = all_acc[username_text]
    except:
        return False
    else:
        return True


def email_validation(email_text):
    
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.fullmatch(regex, email_text)):
        # print("Valid Email")
        return True
    else:
        # print("Invalid Email")
        return False
