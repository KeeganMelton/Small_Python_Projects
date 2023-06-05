another_calculation = True


# adds two numbers
def add_numbers(n1, n2):
    return n1 + n2


# subtracts two numbers
def subtract_numbers(n1, n2):
    return n1 - n2


# multiples two numbers
def multiply_numbers(n1, n2):
    return n1 * n2


# divides two numbers
def divide_numbers(n1, n2):
    return n1 / n2


# dictionary of calculation functions
calculations = {
    '+': add_numbers,
    '-': subtract_numbers,
    '*': multiply_numbers,
    '/': divide_numbers,
}

# asks user for the first number of the calculation
num1 = float(input("Please enter the first number: "))
for option in calculations:
    print(option)


# asks user to selection
# asks user for the second number of the calculation
# asks user if the user wants to continue calculating using the results, or begin a new calculation
while another_calculation == True:
    operation = input("Select an operation from the list above: ")
    math = calculations[operation]
    num2 = float(input("Please enter the next number: "))
    answer = math(num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")

    if input(f"Do you want to continue calculating with {answer}? (y\\n): ").lower() == 'y':
        num1 = answer
    elif input(f"Do you want to do another calculation? (y\\n): ").lower() == 'y':
        num1 = int(input("Please enter the first number: "))
    else:
        another_calculation = False
