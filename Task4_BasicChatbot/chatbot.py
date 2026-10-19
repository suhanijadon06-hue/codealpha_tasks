from datetime import datetime

BOT_NAME = "AlphaBot"


def clean(message):
    message = message.lower().strip()
    for ch in "?!.,":
        message = message.replace(ch, "")
    return message


def get_reply(message):
    if message in ("hello", "hi", "hey"):
        return "Hi! How can I help you?"
    elif message in ("how are you", "how are you doing"):
        return "I'm fine, thanks! How about you?"
    elif message in ("i am fine", "im fine", "good", "i am good"):
        return "Glad to hear that!"
    elif message in ("what is your name", "who are you"):
        return f"I'm {BOT_NAME}, a simple rule-based chatbot."
    elif message in ("what time is it", "time"):
        return "It's " + datetime.now().strftime("%I:%M %p") + "."
    elif message in ("what is the date", "date", "today"):
        return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."
    elif message in ("thanks", "thank you"):
        return "You're welcome!"
    elif message == "help":
        return ("You can say: hello, how are you, what is your name, "
                "time, date, thanks, bye")
    elif message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def main():
    print(f"{BOT_NAME}: Hello! I'm {BOT_NAME}. Type 'help' to see what I can do.")
    while True:
        message = clean(input("You: "))
        if not message:
            continue
        reply = get_reply(message)
        print(f"{BOT_NAME}: {reply}")
        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    main()
