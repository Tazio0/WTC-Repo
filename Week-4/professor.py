import random

def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        tries = 0

        while tries < 3:
            correct = x + y
            answer = input(f"{x} + {y} = ")
            answer = int(answer)

            if answer != correct:
                print("EEE")
                tries+= 1
                continue
            else:
                if answer == correct:
                    score += 1
                    break

        if tries == 3:
            print(correct)

    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
            else:
                continue
        except ValueError:
            continue

#The random interger gets generated based on the level the user wants
def generate_integer(level):
    if level == 1:
        numb = random.randint(0, 9)
        return numb

    elif level == 2:
        numb = random.randint(10, 99)
        return numb

    elif level == 3:
        numb = random.randint(100, 999)
        return numb

    else:
        raise ValueError

if __name__ == "__main__":
    main()
