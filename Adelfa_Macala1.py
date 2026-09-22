# Payment Method Checker
# Author: Princess Sofia H. Macala
# Section: 8-Adelfa
# Date: September 22, 2026

# This program determines whether a payment method is valid or invalid.

# ======================================================================================================================
# INPUT: Get customers' payment method.
# ======================================================================================================================

# List down acceptable values
valid_payment = ["Cash", "Gcash", "Card"]

# Ask the customer for their payment method
payment = input("What payment method will you be using? ")

# ======================================================================================================================
# PROCESS AND OUTPUT: Identify if the payment method is acceptable.
# ======================================================================================================================

# Check if the input is within the bounds of the acceptable list.
if payment in valid_payment:
    print("Valid payment method: ", payment.capitalize())
else:
    print("Invalid payment method")