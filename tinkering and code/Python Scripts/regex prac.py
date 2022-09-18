import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

KaylynSwapp@gmail.com
'''

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z]+\.(com|edu|net)')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern1 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

#subbed_urls = pattern1.sub(r'\2\3', urls)

match1 = pattern1.findall(urls)
for yo in match1:
    print(yo[0])
# print(subbed_urls)
