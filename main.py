import os
import random
from typing import List


def load_word(path: str) -> List[str]:
    with open(path, 'r') as f:
        list_words = []
        data = f.read()
        data_update = data.split('\n')
        for element in data_update:
            words = element.split(' ')
            list_words.extend(words)

    return list_words


def get_secret_word(list_word: List[str]) -> str:
    index = random.randint(0, len(list_word))
    return list_word[index]


def display_secret_word(secret_word: str, guessed_letters: List[str]):
    result = ''
    for letter in secret_word:
        if letter.lower() in guessed_letters:   #if P is the letter and user entre p string comparaison won't match due to ascii binary number,
                                                # so letter.lower make sure the comparaison is between lowercase
            result += letter
        else:
            result += '_'
    return result


def guess_word(secret_word: str, chances: int):
    guessed_letters = []
    i = 0
    print('You have to guess the word ! Good luck\n')
    size = len(secret_word)
    print('_' * size + '\n')
    while i < chances:
        letter = input("Enter a letter :").lower()  # make sur its lower letter
        while letter == '':
            letter = input("Please enter a letter :")
        while letter in guessed_letters:
            print("You already enter this letter")
            letter = input("Enter a letter :").lower()
        guessed_letters.append(letter)
        if letter in secret_word:
            print('Well done, keep going !')
        else:
            i += 1
            print('Wrong letter')
        result = display_secret_word(secret_word, guessed_letters)
        print('You have {} chances left\n'.format(chances - i))
        if result == secret_word:
            return 1
        else:
            print(result + '\n')
    return 0


if __name__ == '__main__':
    actual_path = os.getcwd()
    word_path = os.path.join(actual_path, "Words.txt")
    list_words = load_word(word_path)
    secret_word = get_secret_word(list_words)
    chances = 10
    play_again = True
    while play_again:
        status = guess_word(secret_word, chances)
        if status == 1:
            print('You won, The word was : {}'.format(secret_word))
        else:
            print('You lost')
        resp = input("Wanna play again ? Y/N").upper()
        if resp == 'Y':
            play_again = True
        else:
            play_again = False
