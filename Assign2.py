"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
if num1>num2:
    hypotenuse=num1
    missing_side=math.sqrt(num1**2-num2**2)
else:
    hypotenuse=num2
    missing_side=math.sqrt(num2**2-num1**2)
rounded_missing_side=round(missing_side,1)
print("the langth of the missing side is:",rounded_missing_side)