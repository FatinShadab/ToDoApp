import json
import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

endpoint = "http://127.0.0.1:8080/api-v0/create/"

username = input("Enter your username: ")
password = getpass("Enter your password: ")

todo_title = input("Title - ")
todo_des = input("Description - ")

data = {
    "title": todo_title,
    "description": todo_des,
}

response = requests.post(endpoint, data=data, auth=HTTPBasicAuth(username, password))

print(f"response status: {response.status_code}")
print(response.json())