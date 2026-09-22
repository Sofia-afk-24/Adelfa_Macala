# Student Score Entry
# Author: Princess Sofia H. Macala
# Section: 8-Adelfa
# Date: September 22, 2026

# This program determines if the student's score is a valid numerical value and must be between 0 and 100

# We use try and except ValueError to only get an input with a valid data type
try:
    # Ask for the student's score
    Score = int(input("Enter examination score: "))

    # Check if the student's score is between 0 and 100, if not, then display Invalid input
    if 0<=Score<=100:
        print("Valid score.")
    else:
        print("Invalid input. Please enter a number between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a number")