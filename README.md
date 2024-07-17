# Rhoshan's Login Management System

This is my third project Rhoshan's Login Management System. It is an application developed to aid in user authentication using Google Sheets. This system is all about creation, validation, and management of user accounts. It ensures security yet a simple procedure for logging in. The main interface is the terminal.

This project includes an overview of the current users, offering the possibility of logging in and registering. Also, this interface is user-friendly to ensure easy navigation and operation.

<img src="readme-images/start-screen.png" alt="start view of the application">

## Features

### Feature overview:

| Feature | Description |
| ------- | ----------- |
| Login | Authenticates User and logins upon correct credentials.
| Register | Signs in new user with a unique email and password.
| Validate Email | Ensures the email entered is in the right format and is from the right domain.
| User Authentication | Email and Password Combination validated through worksheet Users. 
| User Data Management | Stores and updates the users information into the google sheets

Below is main features in elaborated manner :
#### Validate Email
This function validates the email id that it has '@' and ends with .com or .net or .ie

#### Register User
This is the function that asks for a user's email and password, validates the email, and further checks if the email is found to be existing. If the email is valid and does not exist, this function saves the information of the new user in the Users worksheet.

## Log In User
This function gets the user's email and password, validates the email, verifies the credentials with the saved credentials from the Users worksheet, and logs in the user if the credentials match.

#### User Data Management
Helps in managing storage and retrieval of user data from the Google Sheets, and this will help put the user's information up to date and accurate.

## UX Design
The program will be run via a terminal interface to enable the best user experience in using the program. The design secures clarity in navigation and ease. User prompts and feedback will be intuitive and informative.

## User Stories

### New Site Users

* As a new user, I want to understand what the tool does.
* As a new user, I want to have a clear overview of the functionalities.

### Returning Site Users

- Being a New User, I wish to have a simple and clear interface.
- Being a Returning User, I need a reliable way to keep my used credentials.
- Being a Returning User, I should be able to login simply and quickly.

## Testing
The following actions were tested incrementally during development and after project completion, which comprised of:

- Validation checks for email and password inputs.
- Testing the log-in and sign-up logic 
 - Making it more resilient to invalid inputs and giving sufficient feedback 

### Bugs (all not fixed yet) 
None yet.. .

### Bugs (already fixed) 

| Bug | Description | Correction  | 
| --- | ----------- | ---------- | 
| Wrong email formatting | The system allowed some wrong email formats | Added validation to check for '@' and allowed domains |
| Duplicate email registration | Users could register with a previously used email. | Added a check to be able to not register using a previously used email. |

### Validator Testing
Validator testing was done using https://pep8ci.herokuapp.com/. Found no significant issues.

<img src="readme-images/python-linter.png" alt="python linter results">

## Deployment
The site installed is deployed to Heroku using a GitHub repository data store.

### Configure Heroku
To configure Heroku :

1. Visit the website https://id.heroku.com/login and either log in to account or create one. 
2. Create a new app on Heroku.
3. Link the app to GitHub and then select the branch to be deployed.
4. Add necessary creds and configure the environment.

### GitHub

Setting up your repository in GitHub :

1. In your GitHub repository, go to the Settings tab.
2. Under the source section, select Main Branch from the drop-down and hit "Save".
3. Under the repository topic section, select the template topic.
4. Under the About section, write a short description of the template.
5. Clone repository locally by following the prompted instructions.

## Tools & Technologies used

- Python librariers including gspread
- Git for version control
- GitHub for storing code
 - Heroku for Deploying

## Improvements and ideas for future projects

- Improve on validation mechanisms for improved security.
- Enhance the design of terminal interface
- Add password recovery and two factor authentication among other features.
- Create the ability to reset password.
- Add a 'forgot password' option.

## Credits

### Content
This README's structure and content were created by myself with the help and guidance of Google, Youtube and some AI.
### Code

| No | Description | Source | URL |
| -- | ----------- | ------ | --- |
| 1 | Using ASCII tables for a better view | GeeksforGeeks | https://www.geeksforgeeks.org/generate-simple-ascii-tables-using-prettytable-in-python/ |
