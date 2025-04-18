import art

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

game_over = False

while not game_over:
    print(art.logo)
    continue_operating = True
    answer = 0
    num1 = int(input("Enter the first number: "))

    while continue_operating:
        operation = input("Enter '+' to add, '-' to subtract, '*' to multiply,"
                          " or '/' to divide: ")
        num2 = int(input("Enter the second number: "))

        if operation == "+":
            answer = operations["+"](num1, num2)
        elif operation == "-":
            answer = operations["-"](num1, num2)
        elif operation == "*":
            answer = operations["*"](num1, num2)
        elif operation == "/":
            answer = operations["/"](num1, num2)
        else:
            print("You did not enter a valid operation.")

        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"Do you want to use {answer} for the next calculation? Type "
                 f"'y' or 'n': ") == "n":
            continue_operating = False
        else:
            print("\n" * 20)
            num1 = answer
            print(answer)
