# PIN Validator
# Author: Princess Sofia H. Macala
# Section: 8-Adelfa
# Date: September 22, 2026

# This program determines if the pin created by the user is valid

# ======================================================================================================================
# INPUT: Get user's pin.
# ======================================================================================================================

# Ask the user to create a pin
PIN = input("Create a 6-digit PIN: ")

# ======================================================================================================================
# PROCESS AND OUTPUT: Check if the input pass the requirements.
# ======================================================================================================================

# Check if the pin is 6 digits and are all in numerical value
if len(PIN) == 6 and PIN.isdigit():
    print("Valid PIN: ")
else:
    print("Invalid PIN")