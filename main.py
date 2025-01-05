import sqlite3

# Connect to the database
con = sqlite3.connect("passwords.db")
cursor = con.cursor()

# Function to login to the system
def login():
    name = input("Enter name: ")
    master_password = input("Enter master password: ")
    cursor.execute(f"SELECT * FROM master_login WHERE name=? AND master_password=?;", (name, master_password))
    login_query = cursor.fetchone()

    if login_query is None:
        print("Login Fail")
        login()
    else:
        print("\nLogin Successful!\n")
        menu()

# Function to select options
def menu():
    print("Type in the corresponding number to select an option")
    print("1) View passwords")
    print("2) Add a password")
    print("3) Exit\n")

    try:
        choice = int(input())

        if choice == 1:
            view_passwords()
        elif choice == 2:
            add_password()
        elif choice == 3:
            exit()
    except ValueError:
        print("You can only type in numbers")
        menu()

# Function to view available passwords
def view_passwords():
    print("\n*-----------Your passwords-----------*\n")

    for x in cursor.execute("SELECT website_name, url, username, email, notes, password FROM passwords;"):
        print(x)
        print("\n")
    menu()

# Function to add a new password
def add_password():
    print("\n*-----------Add a password to the database-----------*\n")

    website_name = input("Website Name: ")
    url = input("URL: ")
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    notes = input("Notes: ")

    cursor.execute("INSERT INTO passwords (website_name, url, username, email, notes, password) VALUES (?, ?, ?, ?, ?, ?);", (website_name, url, username, email, notes, password))
    con.commit()

    print("\nInformation Added!\n")

    menu()

login()

con.close()