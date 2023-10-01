# To test my module
import mymodule
name = input("Please enter your name : ")
mymodule.greet(name)
calc = mymodule.Calculator()
a = int(input("Enter the first no : "))
b = int(input("Enter the second no: "))
operator = input(
    "enter the arithmatic symbol to do the operation ex +,-*,/ : ")
if operator == "+":
    result = calc.add(a, b)
elif operator == "-":
    result = calc.sub(a, b)
elif operator == "*":
    result = calc.multiply(a, b)
elif operator == "/":
    result = calc.divide(a, b)
else:
    result = "Invalid input."

print("Result:", result)
