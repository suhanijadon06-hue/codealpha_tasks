def get_reply(message):
    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def main():
    while True:
        message = input("You: ").lower()
        print("Bot:", get_reply(message))
        if message == "bye":
            break


if __name__ == "__main__":
    main()
