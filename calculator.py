def calculate(no1, op , no2):
  if op == "+":
    return no1 + no2
  elif op == "-":
    return no1 - no2
  elif op == "*":
    return no1 * no2
  elif op == "/":
    if no2 == 0:
      print("Error: Division by zero")
      return None
    else:
      return no1 / no2
  else:
    print("Invalid operator. Please use +, -, *, or /")
    return None
while True:
  try:
    no1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    no2 = float(input("Enter second number: "))
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    continue
  result = calculate(no1, op, no2)
  if result is not None:
    print(f"Result: {result}")
    choice = input("Do you want to continue calculation? (1/2): ")
  if choice.lower() != "1":
    break
print("Thank you for using the calculator!")
