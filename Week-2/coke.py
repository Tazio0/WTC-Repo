def coke():
    amount = int(50)
    valid_coins = [5, 10, 25]

    while amount > 0:
        print(f"Amount Due: {amount}")
        user_input = int(input("Please enter coin: "))
        if user_input in valid_coins:
            amount -= user_input
        else:
            print("Coin not valid")

    if amount == 0:
        print("Coke Dispensed")
    if amount <= 0 :
        print(f"Change owed: {abs(amount)}")

coke()