def deep():
    q1 = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    really = q1.strip().lower()

    if really == "42" or really == "forty-two" or really == "forty two" :
        print("Yes")
    else:
        print("No")

deep()