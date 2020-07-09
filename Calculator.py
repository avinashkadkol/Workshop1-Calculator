import os


# This function Add two numbers
def add(parameter_a, parameter_b):
    return parameter_a + parameter_b


# This function subtracts two numbers
def subtract(parameter_a, parameter_b):
    return parameter_a - parameter_b


# This function multiplies two numbers
def multiply(parameter_a, parameter_b):
    return parameter_a * parameter_b


# This function divides two numbers
def divide(parameter_a, parameter_b):
    return parameter_a / parameter_b


print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)


with open("workshop1_calc.txt",mode='r') as file_calc:
    file_string = file_calc.read().splitlines()
    print(file_string)
    file_calc.read().split()

    if user_choice in ('+', '-', '*', '/'):
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))

        if user_choice == '+':
            print(first_num, "+", second_num, "=", add(first_num, second_num))

        elif user_choice == '-':
            print(first_num, "-", second_num, "=", subtract(first_num, second_num))

        elif user_choice == '*':
            print(first_num, "*", second_num, "=", multiply(first_num, second_num))

        elif user_choice == '/':
            print(first_num, "/", second_num, "=", divide(first_num, second_num))
        break
    else:
        print("Oops you have only 4 choices at this point in time , more features will be add shortly")
