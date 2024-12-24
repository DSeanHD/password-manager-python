import sqlite3

con = sqlite3.connect("passwords.db")
cursor = con.cursor()

# Function to login to the system
def login():
    name = input("Enter name: ")
    master_password = input("Enter master password: ")
    cursor.execute(f"SELECT * FROM master_login WHERE name='{name}' AND master_password='{master_password}';")
    login_query = cursor.fetchone()

    if login_query is None:
        print("Login Fail")
        login()
    else:
        print("Login Successful!")
        menu()

# Function to select options
def menu():
    print("Type in the corresponding number to select an option")
    print("1) View passwords")
    print("2) Add a password")
    print("3) Exit")

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

def view_passwords():
    print("View your passwords")
    cursor.execute("SELECT * FROM passwords;")

def add_password():
    print("Add a password to the database")

for x in cursor.execute("SELECT * FROM master_login"):
    print(x)

menu()

con.close()

# User can save username, email, password, website name, url and add notes