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
    return "@" in email and email.endswith(".com")


def login_user(pEmail,pPassword):
    """
    Checks if the email and password exists
    """
    all_user_accounts = SHEET.worksheet("Users").get_all_values()
    found = False
    for emails , passwords in all_user_accounts:
        if pEmail == emails and pPassword == passwords:
            print(f'Logged in successfully , welcome {pEmail}')
            found = True
            break
    if not found:
        print(f'No account with the email {pEmail} exists please create a account!')


def main():
    """
    Run all program functions
    """
    user_email = input('Enter Email: ')
    user_password = input('Enter Password: ')

    valid = validate_email_input(user_email)
    if valid and user_password != '':
        login_user(user_email,user_password)
    else:
        print('Please provide a valid email and password !')

print("Welcome To Rhoshans Login Management System Please Follow Instructions On Screen!")
main ()