from unidecode import unidecode 

BLANK = "_"

class Guesser:
    def __init__(self, correct: str):
        self.correct = correct

    def guess(self, guess: str):
        guess = list(guess)
        wrong = guess.copy()
        guessed = []
        left = []
        correct_left = list(self.correct).copy()
        for i in range(len(self.correct)):
            if unidecode(guess[i]) == unidecode(self.correct[i]):
                guess[i] = self.correct[i]
                guessed.append(guess[i])
                left.append(BLANK)
                correct_left.remove(guess[i])
            else: 
                guessed.append(BLANK)
                left.append(guess[i])
        for i in range(len(self.correct)):
            if left[i] in correct_left:
                correct_left.remove(left[i])
                wrong[i] = BLANK
            else:
                wrong[i] = left[i]
                left[i] = BLANK

        return [guessed, left, wrong]
