def camel():
    letters = input("Enter your words please: ")
    what = ""

    for letter in letters:
        if letter.isupper():
            what += "_" + letter.lower()
        else:
            what += letter
    print(what)

camel()
