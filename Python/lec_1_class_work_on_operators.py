# -*- coding: utf-8 -*-
"""lec 1 Class work on Operators

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vkLfKvnGq-99a0qkj1CAwbyjkSanp82p

### 1 Write a Python program to take two numbers as input from the user and display their sum.
"""

num1=int(input("Enter a number ="))
num2=int(input("Enter a number ="))
add=(num1)+(num2)
print("Addition of",num1 ,"And",num2,"is =",add)

"""###2 Calculate and print the midpoint of two numbers entered by the user.

"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
midpoint = (num1 + num2) / 2
print(f"The midpoint of {num1} and {num2} is: {midpoint}")

"""###3 Write a Python program to calculate the area of a triangle using the formula: area = 0.5 * base * height."""



base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print(f"The area of the triangle is: {area}")

"""###4 Take three numbers as input from the user and display their product."""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
product = num1 * num2 * num3
print(f"The product of {num1}, {num2}, and {num3} is: {product}")

"""###5 Take a number as input and display its square and cube."""

num = int(input("Enter a number: "))
square = num ** 2
cube = num ** 3
print("Square:", square)
print("Cube:", cube)

"""###6

##6.	Take two numbers as input and display their quotient and remainder.
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
quotient = num1 // num2
remainder = num1 % num2
print("Quotient:", quotient)
print("Remainder:", remainder)

"""##7.	Take three numbers as input and display their average"""



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
average = (num1 + num2 + num3) // 3  # Using // for integer division
print("The average is:", average)

"""###

##8.	Write a Python program to calculate the area of a rectangle using the formula: area = length * width.
"""

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is:", area)

"""###9. Take five numbers as input representing marks obtained and total marks."""

obtained_marks = int(input("Enter marks obtained: "))
total_marks = int(input("Enter total marks: "))
percentage = (obtained_marks / total_marks) * 100
print("Percentage:", percentage, "%")