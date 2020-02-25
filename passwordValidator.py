import re

def check(passCheck):
    match = re.match(r"([!@#$%^&*()\-+[\]'\";?/<>,\.=\\\|`~]?[a-zA-Z0-9][!@#$%^&*()\-+[\]'\";?/<>,\.=\\\|`~]?){5,10}", passCheck, )
    if(match):
        print("true")
    else:
        print("false")

passW = input("Insert Password: ")
check(passW)