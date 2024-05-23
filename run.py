import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project-3')

def validate_email_input(email):
    """
    Check email address by checking if it contains an @ symbol,
    and ends with one of the allowed domains
    """
    domains_allowed = [
        '.com',
        '.net',
        '.ie'
    ]
    valid_domain = False
    for ind in domains_allowed:
       if email.endswith(ind):
        valid_domain = True
    return "@" in email and valid_domain


def login_user(pEmail,pPassword):
    """
    Check and validate email inputted , checks the Users worksheet for an account,
    with the given email and password. If both match break loop and return true.
    """
    if not validate_email_input(pEmail): 
        return print('Email address is not valid !')
    users_spreadsheet_values = SHEET.worksheet("Users").get_all_values()
    new_users_account = users_spreadsheet_values[1:]
    user_status = {
        "loggedIn": False,
        "emailFound": False,
        "passwordFound": False,
        "userLoggedIn": False
    }
    [str(value) for value in new_users_account]
    for email , password in new_users_account:
        if pEmail == email:
            user_status['emailFound'] = True
            if pPassword == password:
                user_status['passwordFound'] = True
                user_status['userLoggedIn'] = True
                break

    if not user_status['emailFound']:
        print('Email was not found..')
    elif not user_status['passwordFound']:
        print('Password is incorrect !')
    else:
        print('Login success !')
    
    return user_status['userLoggedIn']



def attempt_login():
    """
    Validate and attempt to log the user in,
    given the inputted email & password
    """
    while True:
        user_email = input('Enter Email: ')
        user_password = input('Enter Password: ')
        loggedIn = login_user(user_email,user_password)
        if loggedIn:
            break

def main():
    """
    Run all program functions
    """
    option = input('Please select an option:\n1 - Login\n2 - Register\nYour choice: ')
    if int(option) == 1:
        attempt_login()

print("Welcome To Rhoshans Login Management System Please Follow Instructions On Screen!\n")
main ()