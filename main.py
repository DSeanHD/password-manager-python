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
        print("Fail")
        login()
    else:
        view_passwords()

# Function to view all the passwords and select options
def view_passwords():
    print("Passwords!")

for x in cursor.execute("SELECT * FROM master_login"):
    print(x)

login()

con.close()

# Allow user to use master password to sign in
# User can save username, email, password, website name, url and add notes