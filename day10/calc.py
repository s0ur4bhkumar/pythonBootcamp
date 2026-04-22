def calculate(operator: str, operand1: int | float, operand2: int | float):
    if operator == "/":
        return operand1 / operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2


def calculator():
    result = 0
    operand1 = int(input("enter your first number"))
    operator = str(input("select operator (/,*,+,-): "))
    operand2 = int(input("Enter your second number"))
    result = calculate(operator, operand1, operand2)
    while True:
        proceed = input(f"Do you want to continue with {result}: ")
        if proceed != "yes":
            print("The result is: ", result)
            break
        operator = str(input("select operator (/,*,+,-): "))
        operand2 = int(input("enter the second number: "))
        if result is not None:
            result = calculate(operator, result, operand2)


calculator()
