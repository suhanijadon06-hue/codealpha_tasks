# Hangman Game

A text-based Hangman game written in Python, built as part of the CodeAlpha Python Programming internship (Task 1).

## Features
- **3 difficulty levels** (easy / medium / hard), each with 5 predefined words
- Player guesses one letter at a time, with a maximum of 6 incorrect guesses
- **Hints**: type `hint` to get a clue (costs 1 guess)
- **Whole-word guessing**: guess the full word at once (a wrong guess costs 2)
- **Scoring system**: points based on difficulty and guesses left (a hint costs 5 points)
- Tracks score and wins over multiple rounds
- ASCII hangman drawing that updates with each wrong guess
- Input validation (letters only, no repeated guesses, correct word length)

## Scoring
| Difficulty | Base points |
|---|---|
| Easy | 10 |
| Medium | 20 |
| Hard | 30 |

Bonus: +2 points for every unused guess. Using a hint: -5 points.

## Concepts Used
`random`, `while` loop, `if-elif-else`, strings, lists, dictionaries, functions

## How to Run
Requires Python 3 (no external libraries).

```bash
python hangman.py
```

## Example
```
=== Welcome to Hangman ===
Choose difficulty (easy / medium / hard): easy

  +---+
  |   |
      |
      |
      |
      |
=========
Word: _ _ _ _ (4 letters)
Wrong guesses left: 6
Guess a letter, the whole word, or type 'hint': o
Good guess! 'o' appears 2 time(s).
...
Guess a letter, the whole word, or type 'hint': book

You won! The word was: book  (+22 points)

Score: 22 | Wins: 1/1
Play again? (y/n):
```
