def playback():
    sentence = input("Enter your speech here if you like to talk fast ")
    words = sentence.split(" ")

    for i in range(len(words)-1):
        words[i] += "..."
    sentence = "".join(words)

    print(sentence)

playback()