# PythonProject

# About
Python Project is an assignment for my scripting 3038C course. 
This script executes several functions:
1. Adding passwords to a password csv file when provided a website, username, and password
2. Retrieving passwords from a csv file when provided a website and username pair
3. Updating an existing password when provided an existing website and username pair
4. Deleting an existing password record provided an existing website and username pair
5. Generating a password when provided a new website and username pair
 
This script is useful as it provides the user greater management over thier passwords. It allows user to input their own passwords or generate secure passwords. It also allows users to delete or update existing passwords. By using this tool, users will also be notified if they already have an account with a website. 

# Instructions
Here are instructions for writing successful commands with this code:

Options & Usage:

-a <add>: Adds a password. Usage: python PythonProjectCode.py <-a> <Website> <Username> <Password>

-r <retrieve>: Retrieves a password. Usage: python PythonProjectCode.py <-r> <Website> <Username>

-u <update>: Updates a password. Usage: python PythonProjectCode.py <-u> <Website> <Username> <Updated_Password>

-d <delete>: Deletes a password. Usage: python PythonProjectCode.py <-d> <Website> <Username>

-g <generate>: Generates a password. Usage: python PythonProjectCode.py <-g> <Website> <Username>

-h: Display this help information.

# Examples
## Adding a password 
    python PythonProjectCode.py -a website.com username Password123!
## Retrieving a password
    python PythonProjectCode.py -r website.com username 
## Updating a password 
    python PythonProjectCode.py -u website.com username 123Password!
## Deleting a password 
    python PythonProjectCode.py -u website.com username
## Generating a password 
    python PythonProjectCode.py -u website2.com username2

# Important Notes:
1. This is not a secure form of password management. 