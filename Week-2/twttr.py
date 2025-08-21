def twttr():
    vowels = "aeiouAEIOU"
    tweet = input("Input: ")

    for letter in tweet:
        if letter in vowels:
            tweet = tweet.replace(letter, "")
    print(f"Output: {tweet}")

twttr()