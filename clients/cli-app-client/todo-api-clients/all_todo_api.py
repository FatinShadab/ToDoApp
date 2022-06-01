import json
import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

endpoint = "http://127.0.0.1:8080/api-v0/all/"

auth_username = input("Enter your username : ")
auth_password = getpass("Enter your password : ")

response = requests.get(endpoint, auth=HTTPBasicAuth(auth_username, auth_password))

print(f"response status: {response.status_code}")
print(response.json())