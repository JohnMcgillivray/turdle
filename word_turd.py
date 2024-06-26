#!/usr/bin/env python3


class Turdle:

    def __init__(self) -> None:
        with open("wordle.txt") as f:
            self.WORD_LIST = f.readlines()
        self.WORD_LIST = [word.strip() for word in self.WORD_LIST]
        self.status = "playing"

    def guess(self, guess: str, words: list[str]) -> tuple[str, list[str]]:
        if len(guess) != 5:
            raise ValueError("Guess must be a 5-letter word!")

        guess = guess.lower()

        match_groups = {}

        if not words:
            words = self.WORD_LIST

        for word in words:
            s = self._find_matches(guess, word)
            if s not in match_groups:
                match_groups[s] = []
            match_groups[s].append(word)

        best_pattern = max(
            match_groups, key=lambda x: len(match_groups[x]) if x != guess else 0
        )

        if best_pattern == guess:
            self.status = "guessed"

        words = match_groups[best_pattern]
        return best_pattern, words

    def _find_matches(self, guess, word):
        match_string = ""
        for i in range(5):
            if guess[i] == word[i]:
                match_string += guess[i]
            elif guess[i] in word:
                match_string += "+"
            else:
                match_string += "-"
        return match_string


def main():

    turd = Turdle()
    words = []

    while turd.status == "playing":
        guess = ""
        while len(guess) != 5:
            guess = input("Please enter a 5-letter word! ")

        res, words = turd.guess(guess, words)
        print(res)

        if turd.status == "playing":
            print(f"Words left: {len(words)}")
            if len(words) < 30:
                print("Words left: ", words)

    print("You guessed the word!")

    if input("Play again? (y/n) ").lower() in ["y", "yes"]:
        main()


if __name__ == "__main__":
    main()
