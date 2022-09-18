## Join() and split() string methods


print('__Love her__ '.join(['Kaylyn', 'Lucy', 'Emily', 'Sebina']))


#The split value does the opposite. it makes words of a string into separate strings of a list.

## you can ask it to split the whitespace area or any character

"""
MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']

"""

# You can also split a multiline string along the newline characters



spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
spam.split('\n')


print(spam)




##Rjust and ljust and center aruments

guy = 'Hello'
print(guy.rjust(30, '*'))

print(guy.ljust(10))

print('hello'.center(20, '-'))
