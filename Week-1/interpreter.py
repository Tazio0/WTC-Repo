def interpreter():
    math = input("Expression: ")
    x, y, z = math.split(" ")
    x = float(x)
    z = float(z)

    if y == "+":
        result = x + z
    elif y == "-":
         result = x - z
    elif y == "*":
         result = x * z
    else:
         result = x / z

    print(f"{result:.1f}")

interpreter()