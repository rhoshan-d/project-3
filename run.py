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

def update_worksheet(data, worksheet):
    """
    Receives a list to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Signing you up...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"Registration successful!\n")

def login_user(pEmail,pPassword):
    """
    Check and validate email inputted , checks the Users worksheet for an account,
    with the given email and password. If both match break loop and return true.
    """
    print(f'\nAttempting to log you in...\n')
    if not validate_email_input(pEmail): 
        return print(f'Email address is not valid.\n')
    elif pPassword == '':
        return print(f'Password cannot be empty.\n')
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
        print(f'{pEmail} was not found.\n')
    elif not user_status['passwordFound']:
        print(f'The password you entered is incorrect.\n')
    else:
        print('Logged in successfully.')
    
    return user_status['userLoggedIn']



def attempt_login():
    """
    Validate and attempt to log the user in,
    given the inputted email & password
    """
    while True:
        user_email = input('Please provide your email: ')
        user_password = input('Please enter your password: ')
        loggedIn = login_user(user_email,user_password)
        if loggedIn:
            break


def register_user ():
    """
    Get inputted email and password & check email does not,
    already exists. Validate both email and password and save
    to the Users worksheet.
    """
    while True:
        email_input = input('Enter your email address: ')
        password_input = input('Enter your password: ')
        if not validate_email_input(email_input): 
            print(f'Email address is not valid.\n')
            continue
        elif password_input == '':
            print(f'Password cannot be empty.\n')
            continue
        users_spreadsheet_values = SHEET.worksheet("Users").get_all_values()
        all_users = users_spreadsheet_values[1:]

        user_exists = False
        for email, _ in all_users:
            if email == email_input:
                print(f'The email address "{email_input}" is already in use!\n')
                user_exists = True
                return
        
        if not user_exists:
            update_worksheet([email_input, password_input], "Users")
            break
    return user_exists

def handle_user_input():
    """
    Handle user input and validate it.
    """
    while True:
        try:
            option = input('Please select an option:\n1 - Login\n2 - Register\nYour choice: ')
            if int(option) == 1:
                attempt_login()
                break
            elif int(option) == 2:
                register_user()
                # We will make this function soon !
                break
            else:
                print(f'{option} is not a valid option.')
        except ValueError as e:
            print(f"Invalid data: {e}, (must be a NUMBER between 1 and 2)")

def main():
    """
    Run all program functions
    """
    handle_user_input()

print("Welcome To Rhoshans Login Management System Please Follow Instructions On Screen!\n")
main ()