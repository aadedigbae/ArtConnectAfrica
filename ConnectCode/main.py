#!/usr/bin/python3
#Create a list to store artworks
artworks = []

#Create a user dictionary to store user credentials
users = {}

#Variable to keep track of the current user's email
current_user_email = None

#Function to handle user signup
def signup():
    fullname = input("Enter your full name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in users:
        print("User already exists. Please sign in.")
    else:
        users[email] = {"fullname": fullname, "password": password}
        print("Signup successful!")

#Function to handle user signin
def signin():
    global current_user_email
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in users and users[email]["password"] == password:
        print("Signin successful!")
        current_user_email = email
        return True
    else:
        print("Invalid credentials. Please try again")
        return False

#Function to display list of artworks
def show_artworks():
    print("\nSee List of Artworks below:")
    for idx, artwork in enumerate(artworks, start=1):
        print("{0}. File Name:{1} \n File Description:{2} \n Region:{3}".format(idx, artwork['file_name'], artwork['file_description'], artwork['region']))

#Function to upload artwork
def upload_artwork():
    file_name = input("Enter file name: ")
    file_description = input("Enter file description: ")
    region = input("Enter region of Artwork: ")
    artworks.append({"file_name": file_name, "file_description": file_description, "region": region})
    print("Artwork uploaded successfully!")

#Function to search artworks
def search_artworks():
    search_term = input("Enter file name or region to search: ")
    search_results = [artwork for artwork in artworks if search_term.lower() in artwork['file_name'].lower() or search_term.lower() in artwork['region'].lower()]
    if search_results:
        print("\nSearch Results:")
        for idx, artwork in enumerate(search_results, start=1):
            print("{0}. File Name:{1} \n File Description:{2} \n Region:{3}".format(idx, artwork['file_name'], artwork['file_description'], artwork['region']))
    else:
        print("The '{0}' does not exist. Pls, try again".format(search_term))

# Function to view profile
def view_profile():
    if current_user_email:
        print("\nYour Profile:")
        print("Full Name:", users[current_user_email]["fullname"])
        print("Email:", current_user_email)
    else:
        print("You are not signed in.")

# Function to sign out
def sign_out():
    global current_user_email
    choice = input("Are you sure you want to sign out? (yes/no): ")
    if choice.lower() == "yes":
        print("Signed out successfully.")
        current_user_email = None
    else:
        print("Sign out cancelled.")

# Function to delete account
def delete_account():
    global current_user_email
    if current_user_email:
        choice = input("Are you sure you want to delete your account? (yes/no): ")
        if choice.lower() == "yes":
            del users[current_user_email]
            print("Account deleted successfully.")
            current_user_email = None
        else:
            print("Account deletion cancelled.")
    else:
        print("You are not signed in.")

# Main loop
while True:
    print("\nWelcome to the Artwork App!")
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        signup()
    elif choice == "2":
        if signin():
            while True:
                print("\nMain Menu:")
                print("1. See List of Artworks")
                print("2. Upload Another Artwork")
                print("3. Search Artworks")
                print("4. View Profile")
                print("5. Delete Account")
                print("6. Sign Out")
                print("7. Quit")
                inner_choice = input("Enter your choice: ")

                if inner_choice == "1":
                    show_artworks()
                elif inner_choice == "2":
                    upload_artwork()
                elif inner_choice == "3":
                    search_artworks()
                elif inner_choice == "4":
                    view_profile()
                elif inner_choice == "5":
                    delete_account()
                elif inner_choice == "6":
                    sign_out()
		elif inner_choice == "7":
                    print("Goodbye!")
                    quit()
                else:
                    print("Invalid choice. Please select again.")
        else:
            continue
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select again.")
