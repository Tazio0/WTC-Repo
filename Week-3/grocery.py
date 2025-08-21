def grocery():
    grocery_list = {}

    while True:

        try:
            user = input("")
            if user in grocery_list:
                grocery_list[user] += 1
            else:
                grocery_list[user] = 1

        except EOFError:
            break

    print()

    for item, amount in sorted(grocery_list.items()):
        print(amount, item.upper())

grocery()

    
    