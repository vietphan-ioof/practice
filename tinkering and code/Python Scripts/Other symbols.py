import re

# Caret and Dollar sign characters
# The caret symbol tells that a match musk occur at the beginning of the text and the dollar sign tells that a match must occur at the end of the text


beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))



endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))




wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890')





# The Wildcard Character

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))


#Matching everything with Dot Star
nameRegex = re.compile(r'First Name: (.*) Laste Name: (.*)')
mo = nameRegex.search('First Name: AL last Name: Sweigart')



#Matching newlines with the dot character

# This matches everything except a new line

