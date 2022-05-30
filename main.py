import random
from words import words

def run():
    print('''Hola! 
    Bienvenidx al ahorcado. Un juego clasico. Las reglas son simples: 
    1- Tenes que adivinar la palabra elegida al azar.
    2- Cada vez que te equivoques con la letra vas a perder 1 vida.
    3- Una vez perdiste todas las vidas perdes y el ahorcado muere :(
    Suerte!''')
    elegir_palabra()

def elegir_palabra():
    word_choice = random.choice(words)
    word_choice = word_choice.lower()
    game_start(word_choice)

def game_start(word_choice):
    cantGuion = len(word_choice)
    word_choice_guion = '-'*cantGuion
    print(word_choice_guion)
    cantLetterFind = len(word_choice)
    game_init(word_choice, cantLetterFind)


def game_init(word_choice, cantLetterFind):
    letterFind = []
    letterIntent = []
    life_status = 6
    endGame = False
    while not endGame:
        flag = False
        letterIntentSet =[]
        letterGuion = []
        letterInsert = str(input('Inserte una letra'))
        for letter in word_choice:
            if letterInsert == letter:
                letterFind.append(letterInsert)
                letterIntent.append(letterInsert)
                flag = True
                cantLetterFind -= 1
            else:
                letterIntent.append(letterInsert)

        letterIntentSet = set(letterIntent)
        if not flag:
            life_status -= 1

        if life_status == 0 or cantLetterFind == 0:
           endGame = True

        if not endGame:
            for letter in word_choice:
                letterFindSet = set(letterFind)
                if letter in letterFindSet:
                    letterGuion.append(letter)
                else:
                    letterGuion.append('-')

        letterGuionWord = ''.join(letterGuion)
        letterIntentWord = '; '.join(list(letterIntentSet))
        print(f'''Intentaste con las letras: {letterIntentWord}.\n{letterGuionWord}\n Te quedan: {life_status} vidas.''')

        if life_status == 0:
            perdiste = True
        else:
            perdiste = False
    byebye(perdiste, life_status, word_choice)

def byebye(perdiste, life_status, word_choice):
    if perdiste:
        print(f'Perdiste! :( La palabra era: {word_choice}')
    elif not perdiste:
        print(f'MUY BIEN! GANASTE EL JUEGO!\n La palabra era: {word_choice}, te quedaron: {life_status} vidas :)')

    play_again = input('¿Queres volver a jugar? \nY: Si\nN: No')
    if play_again == 'y' or play_again == 'Y' or play_again == 'Si' or play_again == 'si':
        run()
    else:
        print("Adios!! Vuelva pronto!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
