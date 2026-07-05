def plus(a, b):
    return a + b


def minu(a, b):
    return a - b


def mult(a, b):
    return a * b


def did(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def show_history():
    with open("store.txt", "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("No history found!")
        else:
            for line in reversed(lines):
                print(line.strip())


def clear_history():
    with open("store.txt", "w") as file:
        pass
    print("History Cleared")


def log_calculation(expression, result):
    with open("store.txt", "a") as f:
        f.write(f"{expression} = {result}\n")


while True:
    task_user = int(input("1 = calculation - 2 = command: "))

    if task_user == 1:
        while True:
            user = int(input("""
1 for Add,
2 for Subtract,
3 for Multiply,
4 for Divide.
Enter choice (1/2/3/4): """))

            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            if user == 1:
                result = plus(a, b)
                print(result)
                log_calculation(f"{a} + {b}", result)
            elif user == 2:
                result = minu(a, b)
                print(result)
                log_calculation(f"{a} - {b}", result)
            elif user == 3:
                result = mult(a, b)
                print(result)
                log_calculation(f"{a} * {b}", result)
            elif user == 4:
                result = did(a, b)
                print(result)
                log_calculation(f"{a} / {b}", result)
            else:
                print("Invalid input")

            user_int = input("Do More Calculation ? 'yes','no': ")
            if user_int.lower() != "yes":
                break

    elif task_user == 2:
        user_cmd = int(
            input("Which command you want to use: '1=History','2=Clear','3=Exit': ")
        )

        if user_cmd == 1:
            show_history()  
        elif user_cmd == 2:
            clear_history()
        elif user_cmd == 3:
            break
        else:
            print("Invalid command")

    else:
        print("Invalid input")

