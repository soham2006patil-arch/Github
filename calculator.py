num1=float(input("enter the value of first number:"))
operator= input("+, -, /, *, //")
num2=float(input("enter the value of second number:"))

if operator == "+":
    print("Addition", num1 + num2)
elif operator == "-":
    print("subtraction", num1 - num2)
elif operator == "/":
    print("division", num1 / num2)
elif operator == "*":
    print("multiplication", num1 * num2)
elif operator == "//":
    print("floor division", num1 * num2)
else:
    print("ERROR OCCURED")

    