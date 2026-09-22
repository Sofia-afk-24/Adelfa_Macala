# Grade Checker
# Author: Princess Sofia H. Macala
# Section: 8-Adelfa
# Date: September 22, 2026

# This program determines if the grade given is valid or invalid.

# ======================================================================================================================
# INPUT: Get student's information with clear prompts
# ======================================================================================================================

# Ask the student's grade
grade = int(input("Enter your grade: "))

# ======================================================================================================================
# PROCESS AND OUTPUT: Check if the input passes the requirement.
# ======================================================================================================================

# Check if the grade is from 0 to 100 and does not exceed these bounds.
if 0<=grade<=100:
    print("Valid grade: ", grade)
else:
    print("Invalid grade.")

