numb1 = int(input("Enter first number: "))
numb2 = int(input("Enter second number: "))
op = input("Enter operator: ")

if op == "+":
    print(numb1 + numb2)
elif op == "-":
    print(numb1 - numb2)
elif op == "*":
    print(numb1 * numb2)
elif op == "/":
    print(numb1 / numb2)
else:
    print("Invalid operator")