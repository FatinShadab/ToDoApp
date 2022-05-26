import json
import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

endpoint = "http://127.0.0.1:8080/client-user-v0/update/"

auth_username = input("Enter your username : ")
auth_password = getpass("Enter your password : ")

username = input("[for update] Enter your username: ")
email = input("[for update] Enter your email address: ")
password1 = getpass("[for update] Enter your password: ")
password2 = getpass("[for update] Re-type your password: ")

while (password1 != password2):
    print("password didn't match enter again!")
    password1 = getpass("[for update] Enter your password: ")
    password2 = getpass("[for update] Re-type your password: ")

data = {
    'username': username,
    'email': email,
    'password': password2,
}

response = requests.put(endpoint, data=data, auth=HTTPBasicAuth(auth_username, auth_password))

print(f"response status: {response.status_code}")
print(response.json())