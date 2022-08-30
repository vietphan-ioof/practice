import random
from wonderwords import RandomSentence

s = RandomSentence()
badWords = []


with open("profanityBanned.txt") as text_file:
    text = text_file.read()

for x in text:
    badWords.append(x)

print(badWords)
























