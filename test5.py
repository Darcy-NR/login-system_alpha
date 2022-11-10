def pass_hider(pass_chars):
    censored_pass = ""
    y = 0
    while y < pass_chars:
        censored_pass += "#"
        y += 1
    return censored_pass

pass_chars = 10

print(pass_hider(pass_chars))