#Opening files with the open() function
import os

helloFile = open('Melodics Key.txt', 'r')
print(helloFile.name) ## print(helloFile.mode)


helloFile.close()















#Shelve Module (Used to save variables)

import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']

shelfFile['cats'] = cats
print(shelfFile.close())
