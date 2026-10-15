# Topic: Python Functions and Modular Programming
# Activity Title: Sum and Difference Calculator

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

def calculate_sum():
    global sum
    sum = number1 + number2
    print(f"Sum: {sum}")

def calculate_difference():
    global difference
    difference = number1 - number2
    print(f"Difference: {difference}")

calculate_sum()
calculate_difference()
