"""
Number Guessing Game

The computer picks a number between 1 and 100. The player gets five
valid attempts to guess it. Invalid input does not use an attempt.

Run normally: python one.py
Run deterministic test mode (secret number 42): python one.py --test
"""

import random
import sys

MIN_NUM = 1
MAX_NUM = 100
MAX_ATTEMPTS = 5
TEST_SECRET = 42


def pick_secret(test_mode):
    """Return a random secret, or 42 when running in test mode."""
    if test_mode:
        return TEST_SECRET
    return random.randint(MIN_NUM, MAX_NUM)


def read_guess():
    """Read one guess, returning None when the input is invalid."""
    text = input("Enter your guess: ").strip()

    try:
        guess = int(text)
    except ValueError:
        print("Invalid input. Enter a whole number.")
        return None

    if guess < MIN_NUM or guess > MAX_NUM:
        print(f"Out of range. Enter a number between {MIN_NUM} and {MAX_NUM}.")
        return None

    return guess


def play_round(test_mode):
    """Play one game and return True if the player wins."""
    secret = pick_secret(test_mode)
    attempts_used = 0

    print(f"\nI'm thinking of a number between {MIN_NUM} and {MAX_NUM}.")
    print(f"You have {MAX_ATTEMPTS} attempts. Good luck!\n")

    while attempts_used < MAX_ATTEMPTS:
        guess = read_guess()

        if guess is None:
            print(f"Attempts left: {MAX_ATTEMPTS - attempts_used} (no attempt lost)")
            continue

        attempts_used += 1
        attempts_left = MAX_ATTEMPTS - attempts_used

        if guess == secret:
            word = "attempt" if attempts_used == 1 else "attempts"
            print(f"Congratulations! You guessed it in {attempts_used} {word}.")
            return True

        if guess < secret:
            print(f"Too low! Attempts left: {attempts_left}")
        else:
            print(f"Too high! Attempts left: {attempts_left}")

    print(f"Game Over! The number was {secret}.")
    print(f"Attempts used: {attempts_used}")
    return False


def ask_play_again():
    """Ask until the player answers yes or no."""
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type y or n.")


def main():
    test_mode = "--test" in sys.argv

    print("=" * 36)
    print("       NUMBER GUESSING GAME")
    print("=" * 36)
    if test_mode:
        print("[test mode: secret number is fixed]")

    games = 0
    wins = 0

    while True:
        games += 1
        if play_round(test_mode):
            wins += 1
        if not ask_play_again():
            break

    print(f"\nYou won {wins} out of {games} game(s). Thanks for playing!")


if __name__ == "__main__":
    main()
