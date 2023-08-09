def remove_duplicates(x: list):
    return list(dict.fromkeys(x))

class Guesser:
    def __init__(self, correct: str):
        self.correct = correct

    def guess(self, guess: str):
        guessed = []
        in_word = []
        for i in range(0, len(self.correct)):
            if guess[i] == self.correct[i]:
                guessed.append(guess[i])
            elif guess[i] in self.correct:
                in_word.append(guess[i])
        guessed = remove_duplicates(guessed)
        in_word = remove_duplicates(in_word)

        return [guessed, in_word]
