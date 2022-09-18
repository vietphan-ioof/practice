## End and Sep statement

print('hello', end='')
print('World')


##Global Statment

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)