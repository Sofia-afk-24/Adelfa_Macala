# Student ID Checker
# Author: Princess Sofia H. Macala
# Section: 8-Adelfa
# Date: September 22, 2026

# This program determines if a students id is valid

# ======================================================================================================================
# INPUT: Get student's information with clear prompts.
# ======================================================================================================================

# This allows our code to use regular expressions like search, match, split, and replace text patterns.
import re

# Ask the for the student's id
student_id = input("Enter student ID: ")

# ======================================================================================================================
# PROCESS AND OUTPUT: Find out the qualification status then display the result
# ======================================================================================================================

# Assign the format to the pattern(variable)
pattern = "2026-1234"

# Check if the input follows the pattern, if not, display invalid.
if re.fullmatch(pattern, student_id):
    print("Student ID is valid")
else:
    print("Student ID is not valid")