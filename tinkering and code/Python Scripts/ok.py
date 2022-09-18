## List function list()

cars = {'Lambhorgini': 435000, 'Telsa': 50000}
print(list(cars.keys()))

##Checking whether a key or value exists in a dictionary

spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys()

##This returns True



## The Get() Method


picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing 2 cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
'I am bringing 0 eggs.'


## Set default method
## Trash way
spam = {'name': 'Pooka', 'age': 5}
if 'Bobby' not in spam:
    spam['Bobby'] = 'black'
##Good way

spam.setdefault('color', 'black')











