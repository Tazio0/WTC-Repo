import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            guess = random.randrange(level)
            break
        else:
            continue

    except ValueError:
        continue

while True:

    try:
        guessed = int(input("Guess: "))

        if guessed < 1:
            continue

        if guess > guessed:
            print("Too small!")
            continue

        elif guess < guessed:
            print("Too large!")
            continue

        else:
            print("Just right!")
            break

    except (ValueError):
        continue
