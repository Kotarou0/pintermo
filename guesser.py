BLANK = "_"

def remove_duplicates(x: list):
    return list(dict.fromkeys(x))

class Guesser:
    def __init__(self, correct: str):
        self.correct = correct

    def guess(self, guess: str):
        guessed = []
        left = []
        correct_left = list(self.correct).copy()
        for i in range(0, len(self.correct)):
            if guess[i] == self.correct[i]:
                guessed.append(guess[i])
                left.append(BLANK)
                correct_left.remove(guess[i])
            else: 
                guessed.append(BLANK)
                left.append(guess[i])
        for i in range(0, len(self.correct)):
            if left[i] in correct_left:
                correct_left.remove(left[i])
            else:
                left[i] = BLANK
        #guessed = remove_duplicates(guessed)
        #in_word = remove_duplicates(in_word)

        return [guessed, left]
