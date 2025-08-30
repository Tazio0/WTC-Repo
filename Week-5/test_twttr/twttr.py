def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    vowels = "aeiouAEIOU"
    for letter in word:
        if letter in vowels:
            word = word.replace(letter, "")
    return word


if __name__ == "__main__":
    main()