def fuel():
    while True:
        user_input = input("Fraction: ")

        if not "/" in user_input:
            continue

        numerator, denominator = user_input.split("/")

        try:
            result = int(numerator) / int (denominator)
            result = round(result*100)
            if result <= 100 and result >= -1:
                if result <= 1:
                    return print("E")
                elif result >= 99:
                    return print("F")
                else:
                    return print(result , "%", sep="")

        except (ValueError, ZeroDivisionError):
            continue

fuel()
