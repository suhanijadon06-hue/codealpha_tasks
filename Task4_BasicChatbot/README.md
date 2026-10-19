# Basic Chatbot

A simple rule-based chatbot written in Python, built as part of the CodeAlpha Python Programming internship (Task 4).

## Features
- Predefined replies to common messages (hello, how are you, bye, etc.)
- Ignores case and punctuation (`Hello!` and `hello` both work)
- Tells the current time and date
- `help` command lists what the bot understands
- Ends the chat on `bye`, `goodbye`, `exit` or `quit`

## Concepts Used
`if-elif`, functions, loops, input/output, strings

## How to Run
Requires Python 3 (no external libraries).

```bash
python chatbot.py
```

## Example
```
AlphaBot: Hello! I'm AlphaBot. Type 'help' to see what I can do.
You: hello
AlphaBot: Hi! How can I help you?
You: how are you
AlphaBot: I'm fine, thanks! How about you?
You: bye
AlphaBot: Goodbye!
```
