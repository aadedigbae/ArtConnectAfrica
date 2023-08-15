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
