import random

MAX_WRONG = 6

WORDS = {
    "easy": {
        "cat": "A small pet that says meow",
        "book": "You read it",
        "tree": "It has leaves and branches",
        "fish": "It lives in water",
        "rain": "Water falling from clouds",
    },
    "medium": {
        "python": "A programming language named after a comedy group",
        "planet": "Earth is one of these",
        "guitar": "A string instrument",
        "bridge": "Helps you cross a river",
        "rocket": "It flies to space",
    },
    "hard": {
        "keyboard": "You type on it",
        "algorithm": "Step-by-step instructions to solve a problem",
        "volcano": "A mountain that can erupt",
        "labyrinth": "A complicated maze",
        "oxygen": "The gas we breathe",
    },
}

POINTS = {"easy": 10, "medium": 20, "hard": 30}

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


def choose_difficulty():
    while True:
        level = input("Choose difficulty (easy / medium / hard): ").strip().lower()
        if level in WORDS:
            return level
        print("Invalid choice, try again.")


def get_guess(guessed, word_length):
    """Return a single letter, a full-word guess, or 'hint'."""
    while True:
        guess = input("Guess a letter, the whole word, or type 'hint': ").strip().lower()
        if guess == "hint":
            return guess
        if not guess.isalpha():
            print("Letters only, please.")
        elif len(guess) == 1 and guess in guessed:
            print("You already guessed that letter.")
        elif len(guess) not in (1, word_length):
            print(f"Enter one letter or a {word_length}-letter word.")
        else:
            return guess


def play(level):
    """Play one round. Returns the points earned (0 if lost)."""
    word, hint = random.choice(list(WORDS[level].items()))
    guessed = []
    wrong = 0
    hint_used = False

    while wrong < MAX_WRONG:
        print(STAGES[wrong])
        display = " ".join(ch if ch in guessed else "_" for ch in word)
        print("Word:", display, f"({len(word)} letters)")
        if guessed:
            print("Guessed:", ", ".join(sorted(guessed)))
        print("Wrong guesses left:", MAX_WRONG - wrong)

        if "_" not in display:
            break

        guess = get_guess(guessed, len(word))

        if guess == "hint":
            if hint_used:
                print("Hint:", hint)
            elif MAX_WRONG - wrong <= 1:
                print("Not enough guesses left to use a hint!")
            else:
                hint_used = True
                wrong += 1
                print("Hint (cost 1 guess):", hint)
            continue

        if len(guess) == len(word) and len(word) > 1:
            if guess == word:
                guessed.extend(set(word))
                break
            wrong += 2
            print("That's not the word! (-2 guesses)")
            continue

        guessed.append(guess)
        if guess in word:
            print(f"Good guess! '{guess}' appears {word.count(guess)} time(s).")
        else:
            wrong += 1
            print(f"Sorry, '{guess}' is not in the word.")

    if wrong >= MAX_WRONG:
        print(STAGES[-1])
        print("\nYou lost! The word was:", word)
        return 0

    points = POINTS[level] + (MAX_WRONG - wrong) * 2
    if hint_used:
        points -= 5
    print(f"\nYou won! The word was: {word}  (+{points} points)")
    return points


def main():
    print("=== Welcome to Hangman ===")
    score = 0
    wins = 0
    rounds = 0

    while True:
        level = choose_difficulty()
        points = play(level)
        rounds += 1
        score += points
        if points:
            wins += 1

        print(f"\nScore: {score} | Wins: {wins}/{rounds}")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break

    print(f"\nFinal score: {score} | You won {wins} of {rounds} round(s).")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
