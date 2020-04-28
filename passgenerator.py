# RandomPasswordGenerator
import string 
import random

def PasswordGenerator(passlength):
    password = string.ascii_letters + string.digits + "!@#$%^&*()_+=-./?><|\}{[]"
    
    passwordlist = []
    
    for char in range(passlength):
        passrandom = random.choice(password)
        passwordlist.append(passrandom)
        
    output = "".join(passwordlist)
    return output
