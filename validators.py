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

    # Define our password salt here, the algorithm will loop over this at random to select the characters
    # these are specified by the gelos password standards
    salt = "wxyz12ABCDEFGH3abcdefgIJKLMNO4567hijklm89nopPQRSTUVqrstuvWXYZ!@#$%^&*()_-+}{><]["

    rand_password = ""

    while password_char_validate(rand_password) == False:
        x = 0
        rand_password = ""

        while x < 8:
                # Run a while loop, take a pseudorandom character from the salt 8 times.
                password_char = random.choice(salt)
                rand_password = rand_password + password_char
                x += 1
    
    return rand_password

def is_account(username_text):
    with open("accounts.json", "r") as f:
        all_acc = json.load(f)
        # Try catch a singleton that == the array that equals username_text, if it throws an exception then there was no retun so its false, if there was a valid return then
        # an account does exist so return true.
    try:
        singleton = all_acc[username_text]
    except:
        return False
    else:
        return True


def email_validation(email_text):
    
    # Do a regular expression -- if email_text fullmatch regex (if email_text matches the conditions of this expression in this way) then that means its an email of 3 parts with an @ and -
    # a . in it. Therefore it is a valid email.

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.fullmatch(regex, email_text)):
        # print("Valid Email")
        return True
    else:
        # print("Invalid Email")
        return False
