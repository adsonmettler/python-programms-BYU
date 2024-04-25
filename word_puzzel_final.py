"""
Author: Anderson Mettler do Nascimento

Creative addition: I added a list of possible secret words. The program randomly selects one
of the words from the list.
"""
from random import randint

list_of_words = [
    'amor', 'beleza', 'cachoeira', 'diamante', 'escultura',
    'floresta', 'gratidao', 'horizonte', 'inspiracao', 'justica',
    'luz', 'melodia', 'natureza', 'orquidea', 'paz',
    'dinheiro', 'saudade', 'tesouro', 'universo', 'vento',
    'xadrez', 'yoga', 'zero', 'agua', 'brilho',
    'canto', 'desejo', 'mulher', 'fe', 'gentileza',
    'harmonia', 'chule', 'jubilo', 'liberdade', 'maravilha',
    'nascer', 'ousadia', 'pureza', 'carro', 'resplendor',
    'sorriso', 'tempo', 'casa', 'valente', 'hino',
    'alegria', 'bencao', 'criatividade', 'dadiva', 'menino'
]
secret_word = list_of_words[randint(0, len(list_of_words) - 1)]
# print(secret_word)
guess = ''
num_guesses = 0

print('Welcome to the word guessing game!\n')

while guess != secret_word:
    print('Your hint is: ', end='')
    for i in range(len(secret_word)):
        if guess == '':
            print('_ ', end='')
        elif secret_word[i] == guess[i]:
            print(f'{secret_word[i].upper()} ', end='')
        elif guess[i] in secret_word:
            print(f'{guess[i]} ', end='')
        else:
            print('_ ', end='')

    print()
    guess = ''
    while len(guess) != len(secret_word):
        guess = input('What is your guess? ').lower()
        if len(guess) != len(secret_word):
            print('Sorry, the guess must have the same number of letters as the secret word.\n')
        num_guesses += 1

print('Congratulations! You guessed it!')
print(f'It took you {num_guesses} guesses.')