import pprint

message = 'Hi lucy, I really wanted to tell you I really love you and I really want to express my love to you but I dont know how :('

list = {}
for letters in message:
    list.setdefault(letters, 0)
    list[letters] += 1

print(list)


### Same program but with pprint --- This makes it much neater

message = 'Hi lucy, I really wanted to tell you I really love you and I really want to express my love to you but I dont know how :('

list = {}
for letters in message:
    list.setdefault(letters, 0)
    list[letters] += 1

pprint.pprint(list)



