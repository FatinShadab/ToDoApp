import json
import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

endpoint = "http://127.0.0.1:8080/client-user-v0/get_info/"

username = input("Enter your username : ")
password = getpass("Enter your password : ")

response = requests.get(endpoint, auth=HTTPBasicAuth(username, password))

print(f"response status: {response.status_code}")
print(response.json())