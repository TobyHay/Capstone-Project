import random
import requests
from bs4 import BeautifulSoup


def intro_message() -> None:
    print('''\nWelcome to Wordle! Your goal is to guess the 5-letter word.

Insert "Q" any time to quit the game.
Insert "1" to receive a list of all possible words left.\n''')


def import_words() -> tuple[list, list]:
    url_1 = 'https://gist.githubusercontent.com/scholtes/94f3c0303ba6a7768b47583aff36654d/raw/d9cddf5e16140df9e14f19c2de76a0ef36fd2748/wordle-La.txt'
    url_2 = 'https://gist.githubusercontent.com/scholtes/94f3c0303ba6a7768b47583aff36654d/raw/d9cddf5e16140df9e14f19c2de76a0ef36fd2748/wordle-Ta.txt'

    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)

    soup_1 = BeautifulSoup(response_1.text, 'html.parser')
    soup_2 = BeautifulSoup(response_2.text, 'html.parser')

    words_1 = soup_1.get_text()
    words_2 = soup_2.get_text()

    answer_list = words_1.split("\n")
    word_list = words_1.split("\n") + words_2.split("\n")

    return (answer_list, word_list)


def output(guesses, results, attempt, keyboard) -> None:
    for n in range(attempt):
        print("    {} <- {}\n".format(" ".join(results[n-1]), guesses[n]))

    for n in range(attempt, 6):
        print("    {}\n".format(" ".join(results[n-1])))

    print(" ".join(keyboard))


def user_input(attempt) -> str:
    value = input("Guess {}/6: ".format(attempt+1)).lower()
    return value


def valid_input(value, alphabet) -> bool:
    if len(value) != 5:
        print('Guess must be 5 letters long')
        return False

    elif not value in word_list:
        print('Guess is not in word list ')
        return False

    for letter in value:
        if not letter in alphabet:
            print('Guess must only contain letters')
            return False
        print()
        return True


def letter_result(current_guess, guesses, results, n, keyboard) -> None:
    guesses.append(current_guess.upper())

    letters_left = remove_correct_letters(current_guess, wordle)
    for i, letter in enumerate(current_guess):
        # Correct Spot
        if letter == wordle[i]:
            results[n-1][i] = ('{}'.format(letter.upper()))

        # Wrong Spot
        elif letter in letters_left:
            results[n-1][i] = ('{}'.format(letter.lower()))
            letters_left.remove(letter)

        else:  # No Spot
            if letter.upper() in keyboard:
                letter_index = keyboard.index(letter.upper())
                keyboard[letter_index] = ' '


def remove_correct_letters(current_guess, wordle) -> list:
    letters_left = wordle[::]
    for i, letter in enumerate(current_guess):
        if letter == wordle[i]:
            letters_left.remove(letter)
    return letters_left


def win_game(wordle, guess) -> bool:
    if list(guess) == wordle:
        print('Well done, you win!')
        return True


def lose_game(attempt, wordle) -> bool:
    if attempt > 5:
        print('You lost! The word was {}'.format("".join(wordle).upper()))
        return True


# ---------------------- Incomplete ----------------------
def get_current_info(guesses, wordle) -> dict:
    current_info = {}
    for guess in guesses:

        print(guess)

        for i, letter in enumerate(guess.lower()):
            # Correct Spot
            if letter == wordle[i]:
                current_info[letter] = [i]

            # Wrong Spot
            # elif letter in wordle:
            #    current_info[letter] = list(range(5))
            #    current_info[letter].remove(i)
            #    print(f"{letter} in {guess} in in wrong Spot")

#     for key in current_info:
#       if len(key.values()) == 1:
#            remove all other key values with this value
    print(current_info)
    return current_info

# example -> current_info = {'a': [0, 1, 2, 3],'b': [1, 2, 3, 4]}


def get_words_left(answer_list, current_info):
    answer_clone = answer_list[::]

    print("Possible answers:")
    for word in answer_list:
        remove_word = False
        if word not in answer_clone:
            continue

        # word[0]:
        if word[0] in current_info and 0 in current_info[word[0]]:
            ...
        if current_info.get(word[0], None).get(0) is not None:
            ...

        for i, letter in enumerate(word):
            if letter not in current_info.keys() or i not in current_info[letter]:
                remove_word = True

        if remove_word:
            answer_clone.remove(word)

    print(answer_clone)
    print(len(answer_clone))


# ---------------------- Main Game Code ---------------------
def playgame() -> None:

    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    keyboard = list('QWERTYUIOP\nASDFGHJKL\n ZXCVBNM\n')

    guesses = []
    results = [['_']*5, ['_']*5, ['_']*5, ['_']*5, ['_']*5, ['_']*5,]

    intro_message()

    attempt = 0
    current_guess = []
    while True:
        output(guesses, results, attempt, keyboard)

        if win_game(wordle, current_guess):
            break

        if lose_game(attempt, wordle):
            break

        current_guess = user_input(attempt)

        if current_guess.upper() == "Q":
            print('Task quit successfully')
            break

        if current_guess == "1":
            current_info = get_current_info(guesses, wordle)
            get_words_left(answer_list, current_info)

            if input("Press enter to continue playing:").upper() == "Q":
                print('Task quit successfully')
                break
            print()
            continue

        if not valid_input(current_guess, alphabet):
            continue

        letter_result(current_guess, guesses, results, attempt, keyboard)

        attempt += 1


# ------------------- Start Game -------------------
answer_list, word_list = import_words()
wordle_num = random.randint(0, len(answer_list))

wordle = list(answer_list[wordle_num])

current_info = {}

playgame()
