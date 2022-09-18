import os
import random


with open('C:\\Users\\madhu\\OneDrive\\Desktop\\Megafile\\Python programs\\wordslist.txt') as e:
    a = [x.strip('\n') for x in e]

    a = list(list(filter(None, a)))

    b = random.choice(a)


letters = []
for x in b:
    letters.append(x)


key_list = []
for lett in letters:
    key_list.append(lett)

if len(letters) > 4:
    ok = letters
    ok[1] = ''
    ok[3] = ''
    ok[4] = ''


amt_guesses = 5

print(key_list)


def main_guess():
    print(ok)

    def first_guess():
        global key_word
        global amt_guesses
        print('What is the first letter of the word?')
        letter1 = str(input())
        if letter1 == key_list[1]:
            ok[1] = letter1
            print(ok)
            print('Good Job! You guessed it right!!!, \n onto the next letter!')
            second_guess()
        elif letter1 != key_list[1]:
            print('OOPSIE.. you got it wrong \n try again loser!')
            amt_guesses -= 1
            print('You have {} guesses left!'.format(amt_guesses))
            if amt_guesses <= 0:
                loser()
            else:
                first_guess()

    def second_guess():
        global amt_guesses
        print('What is the second letter of the word?')
        letter2 = str(input())
        if letter2 == key_list[3]:
            ok[3] = letter2
            print(ok)
            print('Good Job! You guessed it right!!!, \n onto the next letter!')
            third_guess()
        elif letter2 == None or letter2 != key_list[1]:
            print('OOPSIE.. you got it wrong \n try again loser!')
            amt_guesses += 1
            print('You have {} guesses left!'.format(amt_guesses))
            if amt_guesses <= 0:
                loser()
            else:
                second_guess()

    def third_guess():
        global amt_guesses
        print('What is the second letter of the word?')
        letter3 = str(input())
        if letter3 == key_list[4]:
            ok[4] = letter3
            print(ok)
            print('Good Job! You guessed it right!!! Now what is the final word?')
            final_word = input()
            if final_word == key_list:
                WINNER()
        elif letter3 == None or letter3 != key_list[1]:
            print('OOPSIE.. you got it wrong \n try again loser!')
            amt_guesses -= 1
            print('You have {} guesses left!'.format(amt_guesses))
            if amt_guesses <= 0:
                loser()
            else:
                third_guess()

    def loser():
        print('HEY YOU LOST LOSER GO SUCK ON MY BIG BROWN BUTT ;)')

    def WINNER():
        print('WINNER WINNER CHIKEN DINNER :D')

    first_guess()


main_guess()
