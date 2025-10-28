def multiplication(a, b):
    return a + b 

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b 

while True:
    num1 = float(input("what is the first number?"))
    num2 = float(input("what is the second number?"))
    operation = input("Choose an operation (+, -, *, /) or 'q' to quit: ")

    if operation == "+":
        result = multiplication(num1, num2)
        print(f"{num1} + {num2} = {result}")

    elif operation == "-":
        result = subtraction(num1, num2)
        print(f"{num1} - {num2} = {result}")
    
    elif operation == "*":
        result = multiplication(num1, num2)
        print(f"{num1} * {num2} = {result}")
    
    elif operation == "/":
        result = division(num1, num2)
        print(f"{num1} / {num2} = {result}")
    
    elif operation == "q":
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid operation. Please try again.")
        