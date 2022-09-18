import shelve
import re
import pprint
import os
import pprint
import glob
path = 'C:\\Users\\madhu\\OneDrive\\Desktop\\Megafile\\Random\\regex_files'
for y in glob.glob(os.path.join(path, '*.txt')):
    with open(y, 'r') as f:
        t = f.read()

        bee = re.compile(str(input()))
        match = bee.findall(t)
        print(match)
