# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# num = int(input("Enter a number: "))
# fac = factorial(num)

# print(f"Factorial of {num} is {fac}")


import math

num = int(input("enter your number "))

def Cal(num):
    square_root = math.sqrt(num)
    logarithm = math.log(num)
    sine = math.sin(num)
    print(f" Square root : {square_root} \n Logarithm : {logarithm} \n Sine : {sine}")


Cal(num)

