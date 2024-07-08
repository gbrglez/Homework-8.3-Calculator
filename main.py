x = float(input("x: "))
y = float(input("y: "))
operation = input("ukaz (+,-,*,/): ")

if operation == "+":
    print(x+y)
elif operation == "-":
    print(x-y)
elif operation == "*":
    print(x*y)
elif operation == "/":
    print(x/y)
else:
    print("napaka v inputu")
