# Password Manager with CSV Storage
# Allow users to add, retrieve, update, delete, 
# and generate new passwords using a command line interface and store in a CSV
import csv
import re

csvfilepath = 'Passwords.csv' 
passwordgen_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$') 

# def for creating the csvfile if it doesn't exist yet
def create_csv(): 
    with open(csvfilepath, 'a', newline='') as file: 
        writer = csv.writer(file) 
        writer.writerow(['Website', 'Username', 'Password'])

# def for adding passwords
def add_password():

# def for retrieving a password 
def retrieve_password():

# def for updating a password
def update_password():

# def for deleting a password
def delete_password():

#def for generating a password
def generate_password():