import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("project-3")

def validate_email_input(email):
    """
    Check if the provided email address is valid.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    domains_allowed = [".com", ".net", ".ie"]
    valid_domain = False
    for ind in domains_allowed:
        if email.endswith(ind):
            valid_domain = True
    return "@" in email and valid_domain

def update_worksheet(data, worksheet):
    """
    Update the specified worksheet in the Google Sheets document.

    Args:
        data (list): List of data to be inserted into the worksheet.
        worksheet (str): Name of the worksheet to update.
    """
    print("\n============================")
    print("Signing you up...")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print("Registration successful!")
    print("============================\n")

def login_user(pEmail, pPassword):
    """
    Attempt to log in a user with the provided email and password.

    Args:
        pEmail (str): User's email address.
        pPassword (str): User's password.

    Returns:
        dict: A dictionary with the user's login status.
    """
    print("\n============================")
    print("Attempting to log you in...")
    if not validate_email_input(pEmail):
        return {"status": False, "message": "Email address is not valid.\n"}
    elif pPassword == "":
        return {"status": False, "message": "Password cannot be empty.\n"}
    users_spreadsheet_values = SHEET.worksheet("Users").get_all_values()
    new_users_account = users_spreadsheet_values[1:]
    user_status = {
        "loggedIn": False,
        "emailFound": False,
        "passwordFound": False,
        "userLoggedIn": False,
    }
    [str(value) for value in new_users_account]
    for email, password in new_users_account:
        if pEmail == email:
            user_status["emailFound"] = True
            if pPassword == password:
                user_status["passwordFound"] = True
                user_status["userLoggedIn"] = True
                break
    if not user_status["emailFound"]:
        return {"status": False, "message": f"{pEmail} was not found.\n"}
    elif not user_status["passwordFound"]:
        return {"status": False, "message": "The password you entered is incorrect.\n"}
    return {"status": True, "message": "Logged in successfully."}

def attempt_login():
    """
    Attempt to log the user in by prompting for email and password inputs.
    """
    while True:
        user_email = input("Please provide your email:\n> ")
        user_password = input("Please enter your password:\n> ")
        result = login_user(user_email, user_password)
        print(result['message'])
        if result["status"]:
            break
        else:
            choice = input("Would you like to try again? (Y/N)\n> ")
            if choice.lower() != 'y':
                break

def register_user():
    """
    Register a new user by prompting for email and password inputs,
    and validating that the email does not already exist in the Users worksheet.
    """
    while True:
        email_input = input("Enter your email address:\n> ")
        password_input = input("Enter your password:\n> ")
        if not validate_email_input(email_input):
            print("Email address is not valid.\n")
            choice = input("Would you like to try again or go back to the main menu? (Y/N)\n> ")
            if choice.lower() == 'n':
                break
            continue
        elif password_input == "":
            print("Password cannot be empty.\n")
            choice = input("Would you like to try again or go back to the main menu? (Y/N)\n> ")
            if choice.lower() == 'n':
                break
            continue
        users_spreadsheet_values = SHEET.worksheet("Users").get_all_values()
        all_users = users_spreadsheet_values[1:]

        user_exists = False
        for email, _ in all_users:
            if email == email_input:
                print(f'Email address "{email_input}" is already in use!\n')
                user_exists = True
                break
        if not user_exists:
            update_worksheet([email_input, password_input], "Users")
            break
        else:
            choice = input("Would you like to try again or go back to the main menu? (T/M)\n> ")
            if choice.lower() == 'm':
                break

def handle_user_input():
    """
    Handle user input to either login or register based on user's choice.
    """
    while True:
        try:
            print("\n============================")
            option = input("1 - Login\n2 - Register\n3 - Exit\nYour choice:\n> ")
            print("============================\n")
            if option == '1':
                attempt_login()
            elif option == '2':
                register_user()
            elif option == '3':
                print("Exiting goodbye!")
                break
            else:
                print(f"{option} is not a valid option.")
        except ValueError as e:
            print(f"Invalid data: {e}, (must be a NUMBER between 1 and 3)")

def main():
    """
    Run all program functions
    """
    print("=====================================")
    print("Welcome to Rhoshan's Login System")
    print("Follow the on-screen instructions!")
    print("=====================================")
    handle_user_input()

main()
