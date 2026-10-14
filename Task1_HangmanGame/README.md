# Hangman Game

A simple text-based Hangman game written in Python, built as part of the CodeAlpha Python Programming internship (Task 1).

## Features
- Random word picked from a list of 5 predefined words
- Player guesses one letter at a time
- Maximum of 6 incorrect guesses
- ASCII hangman drawing that updates with each wrong guess
- Input validation (single letters only, no repeated guesses)
- Option to play again

## Concepts Used
`random`, `while` loop, `if-else`, strings, lists, functions

## How to Run
Requires Python 3.

```bash
python hangman.py
```

## Example
```
=== Welcome to Hangman ===

  +---+
  |   |
      |
      |
      |
      |
=========
Word: _ _ _ _ _ _
Guess a letter: p
Good guess!
```
