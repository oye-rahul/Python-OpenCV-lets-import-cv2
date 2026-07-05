def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


while True:
    
    choice = input("""
1 for Add,
2 for subtract,
3 for multiply,
4 for divide.
Enter choice (1/2/3/4): 
""")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print("addition of two number is", add(num1, num2))
    elif choice == '2':
        print("subtract of two number is", subtract(num1, num2))
    elif choice == '3':
        print("multiply of two number is", multiply(num1, num2))
    elif choice == '4':
        print("divide of two number is", divide(num1, num2))
    else:
        print("invelid input")

    user_int = input("Do More Calculation ? 'yes','no': ")

    if user_int == "yes":
        print()
    else:
        break
