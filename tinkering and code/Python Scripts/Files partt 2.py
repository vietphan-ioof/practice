import os

calc_File_Path =  os.getcwd()
print(os.path.split(calc_File_Path))


#Os path sep

print(calc_File_Path.split(os.path.sep))



#finding file sizes and folder contents


"""
Calling os.path.getsize(path) will return the size in bytes of the file in the path argument.

Calling os.listdir(path) will return a list of filename strings for each file in the path argument. (Note that this function is in the os module, not os.path.)
"""

print(os.path.getsize(os.getcwd()))

print(os.listdir(os.getcwd()))

totalSize = 0

#for x in os.listdir(os.getcwd()):
 #   totalSize += os.path.getsize(os.getcwd(), x)

#print(totalSize)

# Checking path validity