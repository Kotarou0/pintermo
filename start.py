import guesser
import chooser

chooser_obj = chooser.Chooser()

word = chooser_obj.choose()
print(word)

g = guesser.Guesser(word)
guess = input("Qual é a palavra?")
print(g.guess(guess))
