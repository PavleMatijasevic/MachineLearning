# at least 1 letter between [a-z]
# at least 1 number beetwen [0-9]
# at least 1 letter beetwen [A-Z]
# at least 1 character from [$#@]
# minimum length password 6
# maximum length password 12

import re

def is_valid(password):
    if 6 <= len(password) <= 12:
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])", password):
            return True
        else:
            return False

password = input("Enter passwords separated by commas: ").split(',')
valid_passwords = []

for psw in password:
    if is_valid(psw):
        valid_passwords.append(psw)

print("Valid passwords are: ", (',').join(valid_passwords))       









