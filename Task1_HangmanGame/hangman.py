import random

WORDS = ["python", "hangman", "computer", "keyboard", "program"]
MAX_WRONG = 6

STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


def get_guess(guessed):
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed:
            print("You already guessed that letter.")
        else:
            return guess


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    while wrong < MAX_WRONG:
        print(STAGES[wrong])
        display = " ".join(ch if ch in guessed else "_" for ch in word)
        print("Word:", display)
        if guessed:
            print("Guessed:", ", ".join(guessed))

        if "_" not in display:
            print("\nYou won! The word was:", word)
            return

        guess = get_guess(guessed)
        guessed.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            wrong += 1
            print("Wrong! Guesses left:", MAX_WRONG - wrong)

    print(STAGES[wrong])
    print("\nYou lost! The word was:", word)


def main():
    print("=== Welcome to Hangman ===")
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
