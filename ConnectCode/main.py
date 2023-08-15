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

