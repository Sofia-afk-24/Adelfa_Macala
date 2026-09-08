# Hypotenuse of a Right Triangle Calculator

## Description
### This program calculates the hypotenuse of a right triangle using input values and a math library.

# Use of the math library in order for "math.sqrt()" and "pow()" to function.
import math

## Ask the user for the lengths of side a and side b.
a =float(input("Enter the length of side a: "))
b =float(input("Enter the length of side b: "))

## Calculation of the hypotenuse using the Pythagorean theorem.
hypotenuse =math.sqrt(pow(a,2)+pow(b,2))

## Output of the result.
print(f"The hypotenuse is: {hypotenuse:.2f}")