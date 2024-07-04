operations = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b, "/": lambda a, b: a / b if b != 0 else print("Error: Division by zero")}
while True:
  # Get user input with error handling
  while True:
    try:
      num1 = float(input("Enter first number: "))
      operator = input("Enter operation (+, -, *, /): ")
      num2 = float(input("Enter second number: "))
      break
    except ValueError:
      print("Invalid input. Please enter numbers only.")

  # Perform calculation using dictionary lookup (reduced if statements)
  try:
    result = operations[operator](num1, num2)
    print(f"Result: {result}")
  except KeyError:
    print("Invalid operator. Please use +, -, *, or /")

  # Ask user if they want to continue
  choice = input("Do you want to perform another calculation? (yes/no): ")
  if choice.lower() != "yes":
    break

print("Thank you for using the calculator!")



