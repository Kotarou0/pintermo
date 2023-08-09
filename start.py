import os
import guesser
import chooser
import beautify

MAX_TRIES = 10

def print_divider():
    print('.'*20)

def tutorial():
    print("Tente adivinhar qual é a palavra sorteada. Você tem %d tentativas." % MAX_TRIES)
    print("Letras na posição correta são verdes:")
    word = "Macaco"
    g = guesser.Guesser(word)
    beautify.printb(g.guess("Mxcacy"))
    print("Letras que estão na palavra mas fora de ordem são amarelas:")
    beautify.printb(g.guess("Mcaaoc"))

def clear():
    os.system('clear')

def play():
    while True:
        try:
            length = int(input("Decida o tamanho da palavra sorteada (4-30): "))
            if length < 4 or length > 30:
                raise Exception()
            break
        except:
            print("Digite um NÚMERO no intervalo dado.\n")

    chooser_obj = chooser.Chooser(length)
    word = chooser_obj.choose()
    g = guesser.Guesser(word)

    clear()
    print(word)
    default_stats = g.guess('_'*length)
    tries = MAX_TRIES
    word_tries = []
    while True:
        if tries <= 0:
            print("Você perdeu!\nA palavra correta era")
            beautify.printb(g.guess(word))
            break
        clear()
        print_divider()

        for word_try in word_tries:
            beautify.printb(word_try)
        
        print("Você tem %d tentativa(s) restante(s)." % tries)
        guess = ""

        while len(guess) != length:
            guess = input("\nFaça um chute com %d letras: " % length)

        stats = g.guess(guess)
        word_tries.append(stats)

        tries -= 1
        if guess == word:
            print("Parabéns! Você acertou a palavra.\n")
            break

clear()
print_divider()
print("Bem-vindo ao Pintermo, criado por João Victor Santos.")
print("GitHub: https://github.com/Kotarou0/pintermo.")

while True:
    print_divider()
    print("Comandos:")
    print("\t-> Digite \'tutorial\' para aprender a jogar;")
    print("\t-> Digite \'jogar\' para jogar;") 
    print("\t-> Digite \'sair' para sair.")    
    escolha = input("\nQual é a sua escolha?\n\t>> ")
    clear()
    print_divider()

    match escolha:
        case 'tutorial':
            tutorial()
        case 'jogar':
            play()
        case 'sair':
            print("Obrigado por jogar! Até logo!")
            quit()
        case _:
            print("Por favor, digite um comando válido.")
