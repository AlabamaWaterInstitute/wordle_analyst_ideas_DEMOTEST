import sys

sys.path.append("five-letter-words")
from get_words import get_words
import random
import word_matcher as wm

# print(get_words())


def main():
    while True:
        game_options = """Choose from the following:
        1) Regular play
        2) Guided play
        3) Solver
        X) Exit

        """
        game_choice = input(game_options)
        if game_choice.lower() == "x":
            print("bye!")
            quit()
        elif int(game_choice) == 1:  # Normal play
            game_play(1)
        elif int(game_choice) == 2:  # Guided play
            game_play(2)
        elif int(game_choice) == 3:  # Solver for another game
            game_play(3)
        else:
            print("boo hoo. try typing 1, 2, or 3.")


def game_play(game_type=None, answer=None):
    all_words = get_words()
    results = {}
    if not answer:
        answer = random.choice(all_words).lower()  # Just in case, pun intended
    results = {"answer": answer, "guesses": {}}
    attempts = 0
    while True:
        guess = input("Enter guess: ").lower()
        if len(guess) != 5:
            print("Guess must be 5 letters long.")  # TODO: make this more user friendly
            continue
        attempts += 1
        results = wm.guess_game(guess, results)
        print(f"Attempts {attempts}: {results}")
        show_results(results)
        if results["guesses"][guess][0] = [0,1,2,3,4]:
            print(f"You win!!! in {attempts} attempts.\n")  # TODO: make this more user friendly
    print(answer)

    still_guessing = 1
    while still_guessing == 1:
        while True:
            guess = input("Enter guess: ").lower()
            if len(guess) != 5:
                print("Must be 5 letters!")
            else:
                break
        results = wm.guess_game(guess, results)
        print(results)
        show_results(results)
        if results["guesses"][guess][0] == [0, 1, 2, 3, 4]:
            print("You WON!!!!\n")
            still_guessing = 0


def show_results(results=None):
    for g, wr in results["guesses"].items():
        show_positions(g, *wr)


# show_positions(guess, *results["guesses"][guess])
def show_positions(guess, rightpos, wrongpos):
    # print(guess, rightpos, wrongpos)
    display = ""
    for i, l in enumerate(guess):
        if i not in (set(rightpos) | set(wrongpos)):
            _l = "_"
        elif i in rightpos:
            _l = l.upper()
        else:
            _l = l

        display += _l

    print(guess + ": " + " ".join(display) + " ")


if __name__ == "__main__":
    main()
