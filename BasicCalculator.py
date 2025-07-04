# BasicCalculator.py

print("Simple Calculator")

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Show operation options
print("Choose an operation:")
print("1. + (Addition)")
print("2. - (Subtraction)")
print("3. * (Multiplication)")
print("4. / (Division)")

# Input operation
operation = input("Enter your choice (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
    print("Result: ", result)
elif operation == "-":
    result = num1 - num2
    print("Result: ", result)
elif operation == "*":
    result = num1 * num2
    print("Result: ", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")
