import json
import requests

from getpass import getpass

endpoint = "http://127.0.0.1:8080/client-user-v0/create/"

username = input("Enter your username: ")
email = input("Enter your email address: ")
password1 = getpass("Enter your password: ")
password2 = getpass("Re-type your password: ")

while (password1 != password2):
    print("password didn't match enter again!")
    password1 = getpass("Enter your password: ")
    password2 = getpass("Re-type your password: ")

data = {
    'username': username,
    'email': email,
    'password': password2,
}

response = requests.post(endpoint, data=data)
print(f"response status: {response.status_code}")
print(response.json())