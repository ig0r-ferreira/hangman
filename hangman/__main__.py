import random

from hangman.art import LOGO, STAGES
from hangman.words import WORD_LIST


def random_word(words: list[str]) -> str:
    return random.choice(words)


def clear_console() -> None:
    print('\033[H\033[J', end='')


def show_logo(word_length: int) -> None:
    clear_console()
    print(LOGO, f'The word has {word_length} letters', sep='\n\n', end='\n\n')


def is_letter(string: str) -> bool:
    return len(string) != 1 or not string.isalpha()


def play(lifes: int) -> None:
    secret_word = random_word(WORD_LIST).upper()
    word_length = len(secret_word)
    display, guessed_letters = ['_'] * word_length, []
    hits = 0

    show_logo(word_length)

    while hits < word_length and lifes > 0:
        guess = input('Guess a letter: ').strip().upper()

        if is_letter(guess):
            print(f"'{guess}' is not a letter. Try again!")
            continue

        if guess in guessed_letters:
            print('You have already used that letter. Try another!')
            continue

        show_logo(word_length)

        guessed_letters.append(guess)
        occurs_in_word = 0

        for pos in range(word_length):
            if secret_word[pos] == guess:
                display[pos] = guess
                occurs_in_word += 1

        if not occurs_in_word:
            lifes -= 1
            print(
                f"The letter '{guess}', is not in the word. "
                f'You lost one life, {lifes} left.'
            )
        else:
            hits += occurs_in_word
            print('Very good! You guessed a letter.')

        print(STAGES[lifes])
        print(*display, end='\n\n')

    if lifes:
        print('You barely survived, congratulations.')
    else:
        print(f'You died. The word is: {secret_word}.')


try:
    play(lifes=6)
except KeyboardInterrupt:
    ...
