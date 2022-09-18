#Matching Specefic Repitions with Curly Brackets

import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')

#Greedy and NonGreedy Matching

# Greedy returns longest string, and non greedy returns the shortest string in the regular expressions.....


nongreedyHaARegex = re.compile(r'(Ha){3,5}?')
mo3 = nongreedyHaARegex.search('HaHaHaHaHa')
print(mo3.group())


#Findall() Method


#UNLIKE the search method, the findall method will search for the text even after the first isntance of it
# it will give a list of strings as long as there are no groups in the regular expression


phoneNumRegex = re.compile(r'd\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

## If there areeee groups in the regex then it will return as tuples

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
'[('415', '555', '9999'), ('212', '555', '0000')]'
