# Matching zero or more with the star
import re
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')

print(mo1.group())

wo2 = batRegex.search('The Adventures of Batwoman')

print(wo2.group())




mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())


#Matching one or more with the plus


batRegex_1 = re.compile(r'Bat(wo)+man')
var = batRegex.search('The adventures of Batman')

print(var.group())
