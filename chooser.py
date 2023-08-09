import random

class Chooser():
    def __init__(self):
        with open("palavras/palavras", "r") as f:
           self.lw = f.readlines()

    def choose(self):
        word = random.choice(self.lw)
        word = word.strip()
        return word
