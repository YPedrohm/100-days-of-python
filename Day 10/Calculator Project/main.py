import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculate(first_number):
    end = True
    while end:
        operator = input("type a mathematical operator: '+', '-', '*' or '/': ")
        second_number = int(input("Enter the second number: "))

        result = (operations[operator](first_number, second_number))
        print(f"{first_number} {operator} {second_number} = {result}")

        again = input("Do you want to use the result for the next calculation? Type 'y' for yes, 'n' for a new calculation, or 'e' to exit: ").lower()

        if again == "y":
            first_number = result
        elif again == "n":
            print(art.logo)
            first_number = int(input("Enter the first number: "))
        elif again == "e":
            end = False
        else:
            print("Please enter either 'y', 'n' or 'e'.")

first_number = int(input("Enter the first number: "))
calculate(first_number=first_number)