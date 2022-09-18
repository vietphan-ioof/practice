##Validateinput.py


while True:
    print('enter your age')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')


while True:
    print('select a new password (letters and numbers only): ')
    password = input()
    if password.isalnum():
        break
    print('passwords can only have letters and numbers.')


## Startswith and endswith string methods ---- Very self explanitory what they do (wink wink...)

"""
>>> 'Hello world!'.startswith('Hello')
True
>>> 'Hello world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
False
>>> 'Hello world!'.startswith('Hello world!')
True
>>> 'Hello world!'.endswith('Hello world!')
True

"""
#The join and split string methods

