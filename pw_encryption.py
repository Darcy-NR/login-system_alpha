import hashlib

#Function call passes in the plaintextpassword, or the hashed password, then expects a boolean for either encrypt
# or validate.

def encryption(password_text, hashed, encrypt, validate):
    
    if encrypt == True:
        # If this boolean is true, then the call is to encrypt a plaintext password to md5 hash, so expect a plaintext password
        # and then run.

        plaintext_password = password_text

        hashed = hashlib.md5(plaintext_password.encode())

        print(hashed)

        return hashed.hexdigest()
        # hashlibs class methods actually return hexidecimal objects, not strings for the hash, so we need to call a seperate class method to convert.

    elif validate == True:
        
        #The inverse of what we just did, except as hashes are one way of course, we aren't getting anything out of here. Instead whats happening is the stored password 
        # is being presented hashed against the stored hashed password and if they == then they're the same password and thus password is valid. Hash algorithms better than
        # md5 (like SHA or Blowfish) don't let you do this and md5 is dangerously comprimised as a password hash by now, but this is a good demonstration for the app's sake.

        encrypted_pass = hashed

        input_password = password_text

        input_hash = hashlib.md5(input_password.encode())

        if input_hash.hexdigest() == encrypted_pass:
            # print ("passwords match")
            return True
        else:
            # print("Passwords DO NOT match")
            return False

