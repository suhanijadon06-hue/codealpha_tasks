import random
import re
from datetime import datetime

BOT_NAME = "AlphaBot"
LOG_FILE = "chat_log.txt"

# Each intent has a list of keywords/phrases and a list of possible replies.
INTENTS = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "replies": ["Hi{name}! How can I help you?", "Hello{name}!", "Hey there{name}!"],
    },
    "how_are_you": {
        "keywords": ["how are you", "how is it going", "how r u", "whats up"],
        "replies": ["I'm fine, thanks! How about you?", "Doing great! And you?"],
    },
    "feeling_good": {
        "keywords": ["i am fine", "im fine", "i am good", "im good", "great", "awesome"],
        "replies": ["Glad to hear that!", "That's great!"],
    },
    "feeling_bad": {
        "keywords": ["sad", "bad", "tired", "not good", "bored"],
        "replies": ["Sorry to hear that. Want to hear a joke?",
                    "I hope your day gets better! Type 'joke' for a laugh."],
    },
    "bot_name": {
        "keywords": ["your name", "who are you"],
        "replies": [f"I'm {BOT_NAME}, a simple rule-based chatbot."],
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "thx"],
        "replies": ["You're welcome!", "Anytime!", "Happy to help!"],
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "exit", "quit", "see you"],
        "replies": ["Goodbye{name}!", "See you later{name}!"],
    },
}

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer go to the doctor? It had a virus!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Why was the math book sad? It had too many problems.",
]

FALLBACKS = [
    "Sorry, I don't understand that. Type 'help' to see what I can do.",
    "Hmm, I'm not sure about that. Try 'help'.",
]


def clean(message):
    message = message.lower().strip()
    message = re.sub(r"[^\w\s+\-*/.]", "", message)
    return re.sub(r"\s+", " ", message)


def matches(message, keywords):
    """True if any keyword appears in the message as whole word(s)."""
    return any(re.search(rf"\b{re.escape(k)}\b", message) for k in keywords)


def detect_intent(message):
    for intent, data in INTENTS.items():
        if matches(message, data["keywords"]):
            return intent
    return None


def calculate(message):
    """Evaluate simple expressions like '12 * 4' or 'what is 5 + 3'."""
    match = re.search(r"(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)", message)
    if not match:
        return None
    a, op, b = float(match.group(1)), match.group(2), float(match.group(3))
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif b == 0:
        return "I can't divide by zero!"
    else:
        result = a / b
    if result == int(result):
        result = int(result)
    return f"The answer is {result}."


def get_reply(message, memory):
    name = f", {memory['name']}" if memory.get("name") else ""

    name_match = re.search(r"\b(?:my name is|i am called|call me)\s+([a-z]+)", message)
    if name_match:
        memory["name"] = name_match.group(1).capitalize()
        return f"Nice to meet you, {memory['name']}!"
    elif "what is my name" in message or "whats my name" in message:
        if memory.get("name"):
            return f"Your name is {memory['name']}."
        return "I don't know your name yet. Tell me with 'my name is ...'."
    elif message == "help":
        return ("I can: greet you, chat, remember your name ('my name is ...'), "
                "tell the time/date, tell a joke, do math ('5 + 3'), "
                "show 'history', and say bye.")
    elif message == "history":
        if not memory["history"]:
            return "We haven't talked yet!"
        return "You said:\n  - " + "\n  - ".join(memory["history"][-5:])
    elif matches(message, ["joke", "funny"]):
        return random.choice(JOKES)
    elif matches(message, ["time"]):
        return "It's " + datetime.now().strftime("%I:%M %p") + "."
    elif matches(message, ["date", "today", "day"]):
        return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."

    answer = calculate(message)
    if answer:
        return answer

    intent = detect_intent(message)
    if intent:
        return random.choice(INTENTS[intent]["replies"]).format(name=name)
    return random.choice(FALLBACKS)


def log(lines):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n--- Chat on {datetime.now():%Y-%m-%d %H:%M} ---\n")
        f.write("\n".join(lines) + "\n")


def main():
    memory = {"name": None, "history": []}
    transcript = []

    greeting = f"Hello! I'm {BOT_NAME}. Type 'help' to see what I can do."
    print(f"{BOT_NAME}: {greeting}")
    transcript.append(f"{BOT_NAME}: {greeting}")

    while True:
        raw = input("You: ")
        message = clean(raw)
        if not message:
            continue

        reply = get_reply(message, memory)
        if message != "history":
            memory["history"].append(raw.strip())
        print(f"{BOT_NAME}: {reply}")
        transcript += [f"You: {raw.strip()}", f"{BOT_NAME}: {reply}"]

        if detect_intent(message) == "goodbye":
            break

    log(transcript)
    print(f"(Chat saved to {LOG_FILE})")


if __name__ == "__main__":
    main()
