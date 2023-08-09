import random

class Chooser():
    def __init__(self, length):
        with open("palavras/palavras", "r") as f:
           self.lw = f.readlines()
        self.lw = [x.strip() for x in self.lw if len(x.strip()) == length]

    def choose(self):
        word = random.choice(self.lw)
        word = word.strip()
        return word
