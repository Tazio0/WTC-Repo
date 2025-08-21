def convert(string):
    string = string.replace(":)", "🙂").replace(":(", "🙁")
    return string

def main():
    user_input = input("How are you feeling today? ")
    print(convert(user_input))

main()
