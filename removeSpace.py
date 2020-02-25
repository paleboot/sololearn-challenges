import re

def removeSpace(string):
    print(string)
    result = re.sub(r"\s", "", string)  
    print(result)

string = input("Enter string: ")
removeSpace(string)