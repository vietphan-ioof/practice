import os

# if you want to make your programs work on all operarting systems: You have to write the python scripts to handle both cases


car = os.path.join('usr', 'bin,', 'Documents')
print(car)


# current working dictionary
print(os.getcwd())

#Use this function to change it


os.chdir('C:\\Windows\\System32')
print(os.getcwd())


#absoluite vs relative paths





#Creating new folders with os.makedirs()

os.makedirs('C:\\delicious\\walnut\\waffles')


# Handling absolute and relative paths

"""

Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.

Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.

Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path.
"""

#print(os.path.abspath('.'))





#Finding the file sizes and folder contents

# using os.path.dirname(path)
# using os.path.basename(path)


#f you need a path’s dir name and base name together, you can just call os.path.split() to get a tuple value with these two strings, like so:

calc_File_Path =  os.getcwd()
os.path.split(calc_File_Path)



