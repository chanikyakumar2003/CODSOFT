operations = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b, "/": lambda a, b: a / b if b != 0 else print("Error: Division by zero")}
while True:
  while True:
    try:
      num1 = float(input("Enter first number: "))
      operator = input("Enter operation (+, -, *, /): ")
      num2 = float(input("Enter second number: "))
      break
    except ValueError:
      print("Invalid input. Please enter numbers only.")
  try:
    result = operations[operator](num1, num2)
    print(f"Result: {result}")
  except KeyError:
    print("Invalid operator. Please use +, -, *, or /")
  choice = input("Do you want to perform another calculation? (yes/no): ")
  if choice.lower() != "yes":
    break
print("Thank you for using the calculator!")



