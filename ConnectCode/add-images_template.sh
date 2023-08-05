#!/bin/bash

# Function to display the menu options
show_menu() {
    echo "Menu Options:"
    echo "1. View Image 1"
    echo "2. View Image 2"
    echo "3. View Image 3"
    echo "4. Exit"
}

# Function to display the selected image
view_image() {
    case "$1" in
        1)
            xdg-open "image1.jpg"  # Replace "image1.jpg" with the path to your JPEG file
            ;;
        2)
            xdg-open "image2.jpg"  # Replace "image2.jpg" with the path to your JPEG file
            ;;
        3)
            xdg-open "image3.jpg"  # Replace "image3.jpg" with the path to your JPEG file
            ;;
        *)
            echo "Invalid option"
            ;;
    esac
}

# Main program
while true; do
    show_menu
    read -p "Enter your choice (1-4): " choice

    case "$choice" in
        1|2|3)
            view_image "$choice"
            ;;
        4)
            echo "Exiting the program."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a valid option (1-4)."
            ;;
    esac

    read -p "Press Enter to continue..."
    clear
done

