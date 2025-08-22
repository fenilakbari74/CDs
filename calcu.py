import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero."
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error: Cannot take the square root of a negative number."
    return math.sqrt(x)

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root")

    while True:
        choice = input("Enter choice (1-6) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", power(num1, num2))

        elif choice == '6':
            try:
                num = float(input("Enter number: "))
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
                continue
            print("Result:", sqrt(num))
        else:
            print("Invalid choice. Please select a valid option.")

if _name_ == "_main_":
    calculator()
