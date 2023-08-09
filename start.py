import guesser
import chooser
import beautify
import urwid

chooser_obj = chooser.Chooser()
word = chooser_obj.choose()
g = guesser.Guesser(word)

print(word)

guess = input("\nChute: ")
stats = g.guess(guess)
beautify.printb(stats)
