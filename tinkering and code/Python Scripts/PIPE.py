import re


phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My phone number is (415) 555-4242')

print(mo.group(1))

print(mo.group(2))

#The \( and \) escape characters in the raw string passed to re.compile() will match actual parenthesis characters.




# matching multiple groups with pipe


heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()
mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()

"""

You can also use pipe to match several patterns with the same word in it"""


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo_3 = batRegex.search('Batmobile lost a wheel')

print(mo_3.group())

print(mo_3.group(1))

# Optional Matching with question mark


batRegex_1 = re.compile(r;Bat(wo)?man')
m0_3 = batRegex_1.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
'Batwoman'