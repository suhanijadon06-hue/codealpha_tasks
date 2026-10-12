import random

WORDS = ["python", "hangman", "computer", "keyboard", "program"]
MAX_WRONG = 6


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    while wrong < MAX_WRONG:
        display = " ".join(ch if ch in guessed else "_" for ch in word)
        print("\nWord:", display)

        if "_" not in display:
            print("You won! The word was:", word)
            return

        guess = input("Guess a letter: ").lower()
        guessed.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            wrong += 1
            print("Wrong! Guesses left:", MAX_WRONG - wrong)

    print("\nYou lost! The word was:", word)


if __name__ == "__main__":
    play()
