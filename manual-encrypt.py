import hashlib

password =""

hashed = hashlib.md5(input(password).encode())

print(hashed.hexdigest())