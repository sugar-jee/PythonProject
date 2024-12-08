# Password Manager with CSV Storage
# Allow users to add, retrieve, update, delete, 
# and generate new passwords using a command line interface and store in a CSV
import argparse
import csv
import os
import re
import random
import string
import sys

csvfilepath = 'Passwords.csv'
passwordgen_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

# def for creating the csvfile if it doesn't exist yet
def create_csv():
    if not os.path.exists(csvfilepath):
        with open(csvfilepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Website', 'Username', 'Password'])

# def for check if the website and username pair is already in the csv
def check_existing(Website, Username):
    with open(csvfilepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == Website and row[1] == Username:
                return True
    return False

# def for adding passwords
def add_password(Website, Username, Password):
    if not passwordgen_regex.match(Password):
        print("Invalid password format. Password must have at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long.")
        return
    if check_existing(Website, Username):
        print(f"Password for {Website} with username \'{Username}\' already exists.")
        return
    with open(csvfilepath, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Website, Username, Password])
    print(f"Password added successfully for {Website} with username \'{Username}\'.")

# def for retrieving a password 
def retrieve_password(Website, Username):
    with open(csvfilepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == Website and row[1] == Username:
                print(f"Password for {Website} with username \'{Username}\' is: {row[2]}")
                return
    print(f"Password not found for {Website} with username \'{Username}\'.")

# def for updating a password
def update_password(Website, Username, Updated_Password):
    if not passwordgen_regex.match(Updated_Password):
        print("Invalid password format. Password must have at at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long.")
        return
    rows = []
    found = False
    with open(csvfilepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == Website and row[1] == Username:
                row[2] = Updated_Password
                found = True
            rows.append(row)
    if not found:
        print(f"Password not found for {Website} with username \'{Username}\'.")
        return
    with open(csvfilepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print(f"Password updated successfully for {Website} with username \'{Username}\'.")

# def for deleting a password
def delete_password(Website, Username):
    rows = []
    found = False
    with open(csvfilepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != Website or row[1] != Username:
                rows.append(row)
            else:
                found = True
    if not found:
        print(f"Password not found for {Website} with username \'{Username}\'.")
        return
    with open(csvfilepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        print(f"Password for {Website} with username \'{Username}\' deleted successfully.")

# def for generating a password for a website/username pair and adding it to the csv file. checks if pair is there before adding
def generate_password(Website, Username, length=12):
    if check_existing(Website, Username):
        print(f"Password for {Website} with username {Username} already exists.")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    Gen_password = ''.join(random.choice(characters) for i in range(length))
    with open(csvfilepath, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Website, Username, Gen_password])
    print(f"Generated and added password for {Website} with username \'{Username}\': {Gen_password}")
    return Gen_password

# command-line argument def,
def main():
    parser = argparse.ArgumentParser(description="Password Manager with CSV Storage")
    parser.add_argument('-a', '--add', nargs=3, metavar=('Website', 'Username', 'Password'), help="Add a new password")
    parser.add_argument('-r', '--retrieve', nargs=2, metavar=('Website', 'Username'), help="Retrieve a password")
    parser.add_argument('-u', '--update', nargs=3, metavar=('Website', 'Username', 'Updated_Password'), help="Update an existing password")
    parser.add_argument('-d', '--delete', nargs=2, metavar=('Website', 'Username'), help="Delete a password")
    parser.add_argument('-g', '--generate', nargs=2, metavar=('Website', 'Username'), help="Generate a new password for a website and username, and append it to the CSV file")
    
    args = parser.parse_args()
    
    # show help if no arguments/uses -h
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    if args.add:
        add_password(*args.add)
    elif args.retrieve:
        retrieve_password(*args.retrieve)
    elif args.update:
        update_password(*args.update)
    elif args.delete:
        delete_password(*args.delete)
    elif args.generate:
        generate_password(*args.generate)
    else:
        print("Invalid argument or missing options. Use -h for help.") 
        parser.print_help() 
        sys.exit()

# run it
if __name__ == "__main__":
    create_csv()
    main()