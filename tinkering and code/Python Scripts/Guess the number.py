import random
total = 0
the_random_number = random.randint(1, 19)

print('''guess the input or else you die


you have 8 tries!

''')

while total < 8:
    guess = int(input())

    if guess > the_random_number:
        print('Damn, you suck.... Ur guess was wayy too high ;)')
        total += 1
        continue
    elif guess < the_random_number:
        print('Damn U suck..... Ur guess was wayy to low')
        total += 1
        continue
    elif guess == the_random_number:
        print('goood job u guess it right ')
        break




print('you guessed the number in ' + str(total) + ' tries')
