"""Бейглз, (c) Эл Свейгарт al@inventwithpython.com"""
"""Теги: короткая, игра, головоломка"""

import random

NUM_DIGITS = 1
MAX_GUESES = 10


def main():
    print('''Бейглз это дедуктивная логическая игра на угадывание числа по подсказкам.'
          'Я задумал {}-значное число без повторяющихся знаков.Попробуй угадать это число'
          'Вот некоторые подсказки:'
          'Pico - одно число верное ,но неверная позиция'
          'Farmi - одно число верное и верная позиция'
          'Bagels - нет верных чисел'
          'Например я загадал 248 и твой ответ 281,подсказки будут Fermi Pico'''.format(NUM_DIGITS))
    while True:
        sercretNum = getSecretNum()
        print('Я задумал число')
        print('У вас есть {} - подсказок чтобы угадать.'.format(MAX_GUESES))
        numGuesses = 1
        while numGuesses <= MAX_GUESES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Подсказка №{}:'.format(numGuesses))
                guess = input('> ')
            clues = getClues(guess, sercretNum)
            print(clues)
            numGuesses += 1
            if guess == sercretNum:
                break
            if numGuesses > MAX_GUESES:
                print('У вас закончились подсказки')
                print('Правильный ответ {}.'.format(sercretNum))
            print('Хотите сыграть еще раз?(yes or no)')
            if not input('> ').lower().startswith('y'):
                break
            print('Спасибо за игру')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
        return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Вы угадали!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append['Pico']
        if len(clues) == 0:
            return 'Bagels'
        else:
            clues.sort()
            return ''.join(clues)


if __name__ == '__main__':
    main()
