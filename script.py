#!/usr/bin/env python3

#Author: Hassnain Mohammad

#Author ID: hmohammad7

#Date: 2024/09/23


print("Welcome to the Converter Tool!")

while True:
    print("\n1. Convert inches to centimeters")
    print("2. Convert centimeters to inches")
    print("3. Exit")
    
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == '1':
        inches = int(input("Enter the value in inches: "))
        cm = inches * 2.54
        print(f"{inches} inches is equal to {cm} centimeters.")
    elif choice == '2':
        cm = int(input("Enter the value in centimeters: "))
        inches = cm / 2.54
        print(f"{cm} centimeters is equal to {inches} inches.")
    elif choice == '3':
        print("Exiting the converter tool. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
