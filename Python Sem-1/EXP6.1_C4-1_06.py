# Write a program in which we prompt users to enter personal details like name and surname, which should be strings, age should be an integer, and height and weight should be float. Whenever the user enters input of the incorrect type, keep prompting the user for the same value until it is entered correctly. Give the user sensible feedback
def get_string(prompt):
    while True:
        try:
            value = input(prompt)
            if value.isalpha():
                return value
            else:
                raise ValueError("Please enter only alphabetic characters.")
        except ValueError as e:
            print(e)

def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))  
            return value
        except ValueError:
            print("Invalid age. Please enter a valid integer for age.")  

def get_float(prompt, field_name):
    while True:
        try:
            value = float(input(prompt)) 
            return value
        except ValueError:
            print(f"Invalid {field_name}. Please enter a valid number for {field_name}.")  

name = get_string("Enter your name: ")
surname = get_string("Enter your surname: ")
age = get_integer("Enter your age: ")
height = get_float("Enter your height: ", "height")
weight = get_float("Enter your weight: ", "weight")