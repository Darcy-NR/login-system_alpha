import hashlib

def encryption(password_text, hashed, encrypt, validate):
    
    if encrypt == True:
        
        plaintext_password = password_text

        hashed = hashlib.md5(plaintext_password.encode())

        return hashed.hexdigest()

    elif validate == True:
        
        encrypted_pass = hashed

        input_password = password_text

        input_hash = hashlib.md5(input_password.encode())

        if input_hash.hexdigest() == encrypted_pass:
            print ("passwords match")
            return True
        else:
            print("Passwords DO NOT match")
            return False

