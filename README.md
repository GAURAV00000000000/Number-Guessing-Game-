# Number Guessing Game

A small, interactive command-line game written in Python. The computer
selects a number from 1 to 100, and the player has up to five valid guesses
to find it.

## Objectives

- Practice Python input/output, conditionals, loops, functions, and random
  number generation.
- Provide helpful higher/lower feedback and keep invalid input from consuming
  an attempt.
- Allow multiple rounds and display a final win/game count.

## Features

- Random secret number from 1 through 100 during normal play.
- Five valid guesses per round.
- “Too low” and “Too high” hints after incorrect guesses.
- Validation for non-integer and out-of-range guesses.
- Replay prompt and session win statistics.
- Deterministic `--test` mode, which fixes the secret at 42.
- No third-party packages or external data files required.

## Requirements

- Python 3.8 or newer.
- A terminal or command prompt.

## Run the game

Open a terminal in this project folder and run:

```text
python one.py
```

On Windows, if `python` is not on `PATH`, use the Python launcher:

```text
py one.py
```

To play with a predictable secret number (42), run:

```text
python one.py --test
```

The deterministic mode is also useful for reproducing the test scenarios in
the screenshots and PDF in `test-evidence/`.

## Input and output

- At each `Enter your guess:` prompt, enter a whole number from 1 to 100.
- An invalid number or non-number is reported and does not use an attempt.
- Valid incorrect guesses produce a higher/lower hint and the remaining
  attempt count.
- A correct guess ends the round with a win message. Five incorrect valid
  guesses end the round and reveal the secret.
- At `Play again? (y/n):`, enter `y`/`yes` to start another round or `n`/`no`
  to exit. Other answers are rejected and the prompt repeats.
- On exit, the game reports the total wins and games played.

## Test evidence

The eleven test cases were executed as separate program runs with `--test`;
all expected-output checks passed. Inputs in the table are entered in order,
including the final replay response.

| Case | Inputs | Expected behavior |
|---|---|---|
| 1. First-try win | `42`, `n` | Win in one attempt; final result is 1 win out of 1 game. |
| 2. Too-low hint | `25`, `42`, `n` | Shows “Too low”, then wins in two attempts. |
| 3. Too-high hint | `75`, `42`, `n` | Shows “Too high”, then wins in two attempts. |
| 4. Non-integer input | `abc`, `42`, `n` | Shows the whole-number error; invalid input uses no attempt. |
| 5. Out-of-range input | `0`, `42`, `n` | Shows the range error; invalid input uses no attempt. |
| 6. Five incorrect guesses | `10`, `20`, `30`, `50`, `100`, `n` | Uses five attempts, loses, and reveals 42. |
| 7. Replay answer validation | `42`, `maybe`, `n` | Rejects `maybe`, asks again, then exits with correct statistics. |
| 8. Replay a round | `42`, `y`, `42`, `n` | Plays two rounds and reports 2 wins out of 2 games. |
| 9. Minimum valid guess | `1`, `42`, `n` | Accepts 1 as in range, reports “Too low”, then wins. |
| 10. Maximum valid guess | `100`, `42`, `n` | Accepts 100 as in range, reports “Too high”, then wins. |
| 11. Above-range input | `101`, `42`, `n` | Rejects 101; invalid input uses no attempt, then wins. |

`test-evidence/` contains one transcript image (SVG) per case and a PDF with
all eight transcript pages. The images show the exact scripted input and
corresponding program output from each run.

## Project files

- `one.py` — complete game implementation.
- `README.md` — project documentation and test-case descriptions.
- `test-evidence/` — test transcript images and their combined PDF.
