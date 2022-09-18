import re

phoneNumRegex = re.compile(r'(\d{3}).(\d{3}).(\d{4})')

mo = phoneNumRegex.search('My numer is 626-747-5873')

print('Phonenumber found : ' + mo.group())

# to retrieve all the groups you can use mo.groups


heroRegex = re.compile(r'Batman|Tina Fey')  # First element in the pipe is the first thing going to be printed out if second one is not there
m01 = heroRegex.search('Batman and Tina Fey')
print(str(m01.group()))


# The findall method

phoneNumRegex1 = re.compile(r'\d{3}.\d{3}.\d{4}')
print(phoneNumRegex1.findall('Cell: 626-747-5873 Work: 616 216 2964'))


# Making your own character classes


vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))

# Caret and Dollar Sign Characters

# Matching new lines with Dot character

newLineRegex = re.compile('.*', re.DOTALL)
print(newLineRegex.search('Serve the askdfjal;ksfdjt Sebbina is really cute \n I love her cute face omg').group())


# Case sensitive matching

robocop = re.compile(r'robocop', re.I)
print(robocop.search('Robocop is part man, part machine, all cop.').group())

# substituting strings with the sub() method

#namesRegex = re.compile(r'Agent \w+')

#rint(namesRegex.sub('Censored', 'Agent alice gave me the secret documents to Agent Bob')

#Combining ignorecase, dotall and verbose

