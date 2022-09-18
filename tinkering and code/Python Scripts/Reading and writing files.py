import os

print(os.path.join('usr', 'bin', 'spam'))


# Current working directory

print(os.getcwd())
# Changing the current working directory
# os.chdir


# Creating new folders with os.makedirs()

# bos.makedirs(path)


# Handling absolute and relative paths

print(os.path.abspath('.\\OneDrive'))

print(os.path.isabs('.\\OneDrive'))

print(os.path.relpath('.\\OneDrive'))


# Calling os.path.dirname(path) will return a string of everything that comes before the last slash

path = 'C:\\Windows\\System32\\calc.exe'

print(os.path.dirname(path))
print(os.path.basename(path))

# If you need the paths dir name and base name together, you can just call os.path.split() to get a tuple value

print(os.path.split(path))

# Finding file sizes and folder contents

print(os.path.getsize(path))  # Will return size of file in bytes
print(os.listdir('C:\\Users\\madhu\\OneDrive\\Desktop\\Megafile'))  # will return a list of filename strings

#totalSize = 0
# for filename in os.listdir('C:\\Windows\\System32'):
#   totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32, filename'))


# Chekcing path validity

print(os.path.exists(path))  # will return true if file or folder exists

print(os.path.isfile(path))  # Will return true is the path argument exists and is a file

print(os.path.isdir(path))


# File reading/Writing process

# 3 steps to reading or writing files in python

# open function
helloFile = open('C:\\Users\\madhu\\OneDrive\\Desktop\\Megafile\\Random\\its ya boi.txt')
print(helloFile)


# Reading and the contents of files


helloContent = helloFile.read()
print(helloContent)

# you can also use the readlines() method to get a list of string values from the file

sonnet = open('C:\\Users\\madhu\\OneDrive\\Desktop\\Megafile\\Random\\sonnet baby.txt')
print(sonnet.readlines())


# Writing to files

baconFile = open('bacon.txt', 'w')
print(baconFile.write('Hello world!\n'))
baconFile.close()
baconFile = open('bacon.txt', 'a')
print(baconFile.write('Bacon is not a vegetable'))

#content = baconFile.read()
# baconFile.close()
# print(content)

# Saving variables with the shelve module

import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
print(os.getcwd())

# Shelves have keys and values just likedictionaries
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

# Saving variables with the pprint.pformat()

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
print(fileObj)

# Since python scripts are just text files with the .py file extension
# your python programs can even generatre other python programs. You can then import these files into scripts

import myCats
print(myCats.cats)
