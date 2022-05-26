import os
import sys
import json
import requests
from requests.auth import HTTPBasicAuth

from rich.table import Table
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.console import Console


def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def validate_user(console):
    clear_terminal()
    server_error = False
    endpoint = "http://127.0.0.1:8080/client-user-v0/get_info/"

    username = Prompt.ask("[bold]Enter your [blue]username[/]")
    password = Prompt.ask("[bold]Enter your [blue]password[/]", password=True)
    
    try:
        response = requests.get(endpoint, auth=HTTPBasicAuth(username, password))

        if response.status_code >= 200 and response.status_code <= 300:
            return {'is_valid_user':True, 'username':username, 'password':password}
    except Exception as e:
        server_error = True

    return {'is_valid_user':False, 'server_error':server_error}

def login_page(console):

    global user_credentials

    isLogedIn = False
    show_login_error = False
    show_server_error = False
    
    terminal_text = """[bold][green]                                       __            __                                  
 /  |      /                          /|            /|                 /           /     
(   | ___ (  ___  ___  _ _  ___      ( |  ___      ( |  ___  ___  _ _    ___  ___ (      
| / )|___)| |    |   )| | )|___)       | |   )       | |___)|   )| | )| |   )|   )|      
|/|/ |__  | |__  |__/ |  / |__         | |__/        | |__  |    |  / | |  / |__/||      
                                                                                         

[/][/]\n"""

    while not isLogedIn:
        clear_terminal()
        console.print(terminal_text, justify="center")
        console.print("\n[bold][red]Invalid {username/password}![/]") if show_login_error else None
        console.print("\n[bold][red]Internal server error! please try again later [strong](check your internet connection/make sure the server is running on port 8080)[/].[/]") if show_server_error else None
        user_cmd = Prompt.ask("\n[bold]Type one of the cmd from choices [/]", choices=["login", "register", "exit"], default="register")

        if user_cmd == "register":
            user_data = create_user_page(console=console, call_from_start=True)
            if user_data is not None:
                user_credentials = {'username':user_data['username'], 'password':user_data['password']}
                isLogedIn = True
            else:
                show_server_error = True

        if user_cmd == "login":
            validation_result = validate_user(console=console)
            if validation_result['is_valid_user']:
                user_credentials = {'username':validation_result['username'], 'password':validation_result['password']}
                isLogedIn = True
            else:
                if validation_result['server_error']:
                    show_server_error = True
                else:
                    show_login_error = True

        if user_cmd == "exit":
            clear_terminal()
            sys.exit()

    return user_credentials

def logout(console):
    login_page(console=console)

def callApiId2(session, console):
    clear_terminal()

    endpoint = "http://127.0.0.1:8080/client-user-v0/get_info/"

    try:
        response = session.get(endpoint)

        if response.status_code >= 200 and response.status_code <= 300:
            
            console.print("[bold]The detail information of our [green]account[/]:[/]\n")
            console.print_json(data=response.json())
    except Exception as e:
        console.print("\n[bold][red]Internal server error! please try again later [strong](check your internet connection/make sure the server is running on port 8080)[/].[/]")

def callApiId3(session, console):
    clear_terminal()

    endpoint = "http://127.0.0.1:8080/client-user-v0/update/"

    username = Prompt.ask("[bold][blue]<For update>[/] Enter your username: [/]")
    email = Prompt.ask("[bold][blue]<For update>[/] Enter your email address: [/]")
    password1 = Prompt.ask("[bold][blue]<For update>[/] Enter your password: [/]", password=True)
    password2 = Prompt.ask("[bold][blue]<For update>[/] Re-type your password: [/]", password=True)

    while (password1 != password2):
        clear_terminal()
        console.print("[bold][red]password didn't match enter again![/][/]")
        password1 = Prompt.ask("[bold]Enter your password[/]", password=True)
        password2 = Prompt.ask("[bold]Re-Enter your password[/]", password=True)

    data = {
        'username': username,
        'email': email,
        'password': password2,
    }

    try:
        response = session.put(endpoint, data=data)

        if response.status_code >= 200 and response.status_code <= 300:
            clear_terminal()
            console.print("[bold]You're account has been [green]updated[/].[/]\n")
    except Exception as e:
        console.print("\n[bold][red]Internal server error! please try again later [strong](check your internet connection/make sure the server is running on port 8080)[/].[/]")

def callApiId4(session, console):
    clear_terminal()
    has_deleted = False

    endpoint = "http://127.0.0.1:8080/client-user-v0/delete/"

    user_is_sure = Confirm.ask("[strong]Do you want to [red]delete[/] the account permanently?[/]")
    if user_is_sure:
        try:
            response = session.delete(endpoint)
            has_deleted = True
            console.print_json(data=response.json())
        except Exception as e:
            console.print("\n[bold][red]Internal server error! please try again later [strong](check your internet connection/make sure the server is running on port 8080)[/].[/]")
    else:
        console.print("\n[strong][green]Account Deletion Stopped![/][/]")

    return has_deleted

def create_user_page(console, call_from_start=False):
    clear_terminal()
    endpoint = "http://127.0.0.1:8080/client-user-v0/create/"

    username = Prompt.ask("[bold]Enter your [blue]username[/]")
    email = Prompt.ask("[bold]Enter your [blue]email[/]")
    password1 = Prompt.ask("[bold]Enter your [blue]password[/]", password=True)
    password2 = Prompt.ask("[bold]Re-Enter your [blue]password[/]", password=True)

    while (password1 != password2):
        clear_terminal()
        console.print("[bold][red]password didn't match enter again![/][/]")
        password1 = Prompt.ask("[bold]Enter your [blue]password[/]", password=True)
        password2 = Prompt.ask("[bold]Re-Enter your [blue]password[/]", password=True)

    data = {
        'username': username,
        'email': email,
        'password': password2,
    }

    try:
        response = requests.post(endpoint, data=data)

        clear_terminal()
        if response.status_code >= 200 and response.status_code <= 300:
            if call_from_start:
                return data
            return response.json()

    except Exception as e:
        pass

    return None

def continueInSession(console, user_cmd, user_credentials):
    with requests.sessions.Session() as session:
        session.auth = (user_credentials['username'], user_credentials['password'])

        if user_cmd == "2":
            callApiId2(session=session, console=console)

        elif user_cmd == "3":
            callApiId3(session=session, console=console)
            console.print("\n[bold]You need to [blue]login[/] again !")
            user_cmd = Prompt.ask("\n[bold]Enter [blue]'<'[/] to continue [/]", choices=["<"], default="<")
            logout(console=console)

        elif user_cmd == "4":
            has_deleted = callApiId4(session=session, console=console)
            if has_deleted:
                logout(console=console)

def homepage(console):
    clear_terminal()

    valid_api_table = Table(title="[bold]Rest Apis For [blue]user app[/][/]", show_footer=True, show_lines=True)

    valid_api_table.add_column("Id", justify="center", style="cyan", no_wrap=False)
    valid_api_table.add_column("Apis", justify="center", style="cyan", no_wrap=False, footer="[bold]Enter [blue]<[/] for nevigate back[/]\n[bold]Enter [blue]q[/] to quit[/]")
    valid_api_table.add_column("Type", justify="center", style="cyan", no_wrap=False)

    valid_api_table.add_row("1", "http://127.0.0.1:8080/client-user-v0/create/", "POST")
    valid_api_table.add_row("2", "http://127.0.0.1:8080/client-user-v0/get_info/", "GET")
    valid_api_table.add_row("3", "http://127.0.0.1:8080/client-user-v0/update/", "PUT")
    valid_api_table.add_row("4", "http://127.0.0.1:8080/client-user-v0/delete/", "DELETE")

    console.print(valid_api_table, justify="center")


if __name__ == "__main__":

    console = Console()

    user_cmd = None
    user_quit = False    
    user_credentials  = {}
    login_page(console=console)

    while not user_quit:
        homepage(console=console)
        user_cmd = Prompt.ask("\n[bold]Enter api [blue]'Id'[/] from table above to use [/]", choices=["1", "2", "3", "4", "q"], default="1")

        if user_cmd == "q":
            clear_terminal()
            user_quit = True

        elif user_cmd == "1":
            user_data = create_user_page(console=console)
            if user_data is not None:
                console.print("[bold]The new user was created [green]successfully[/].[/]\n")
                console.print_json(data=user_data)
            else:
                console.print("[bold][red]Enable to create new user.[/][/]\n")
            user_cmd = Prompt.ask("\n[bold]Enter api [blue]'<'[/] to nevigate back [/]", choices=["<"], default="<")

        else:
            continueInSession(console=console, user_cmd=user_cmd, user_credentials=user_credentials)
            user_cmd = Prompt.ask("\n[bold]Enter [blue]'<'[/] to nevigate back [/]", choices=["<"], default="<")