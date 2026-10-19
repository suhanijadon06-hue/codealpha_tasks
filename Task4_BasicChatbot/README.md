# Basic Chatbot

A rule-based command-line chatbot written in Python, built as part of the CodeAlpha Python Programming internship (Task 4).

## Features
- **Intent matching**: understands messages by keywords, not just exact text (`hey there!` counts as a greeting)
- **Several replies per intent**, picked at random so the chat doesn't feel repetitive
- **Remembers your name**: say `my name is ...` and the bot uses it in greetings and goodbyes
- **Calculator**: try `what is 12 * 4` or `10 / 2` (supports + - * /)
- **Jokes**: type `joke`
- **Time and date**
- **History**: type `history` to see your last 5 messages
- **Chat log**: every conversation is saved to `chat_log.txt`
- Ignores case and punctuation

## Concepts Used
`if-elif`, functions, loops, dictionaries, lists, input/output, `re` (regular expressions), `random`, `datetime`, file handling

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
You: my name is Suhani
AlphaBot: Nice to meet you, Suhani!
You: how are you?
AlphaBot: I'm fine, thanks! How about you?
You: what is 12 * 4
AlphaBot: The answer is 48.
You: tell me a joke
AlphaBot: Why do programmers prefer dark mode? Because light attracts bugs!
You: bye
AlphaBot: Goodbye, Suhani!
(Chat saved to chat_log.txt)
```
