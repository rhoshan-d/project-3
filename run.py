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
    Checks the Users worksheet for an account with the given email and password.
    """
    all_user_accounts = SHEET.worksheet("Users").get_all_values()
    found = False
    for emails , passwords in all_user_accounts:
        if pEmail == emails and pPassword == passwords:
            print(f'Logged in successfully , welcome {pEmail}')
            found = True
            break
    if not found:
        print(f'No account with the email {pEmail} exists, would you like to continue?')


def attempt_login():
    """
    Validate and attempt to log the user in,
    given the inputted email & password
    """
    while True:
        user_email = input('Enter Email: ')
        user_password = input('Enter Password: ')

        email_valid = validate_email_input(user_email)
        password_valid = user_password != ''
        if not email_valid and not password_valid:
            print('Please provide a valid email and password.')
        elif not password_valid:
            print('Please provide a valid password.')
        elif not email_valid:
            print('Please provide a valid email.')
        else:
            login_user(user_email,user_password)

def main():
    """
    Run all program functions
    """
    option = input('Please select an option:\n1 - Login\n2 - Register\nYour choice: ')
    if int(option) == 1:
        attempt_login()

print("Welcome To Rhoshans Login Management System Please Follow Instructions On Screen!\n")
main ()