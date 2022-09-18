example = ['left', 'right', 'up', 'down']

# BAd way

for i in range(len(example)):
    print(i, example[i])

# good way


for i, j in enumerate(example):
    print(i, j)


new_dict = dict(enumerate(example))

print(new_dict)

[print(i, j) for i, j in enumerate(new_dict)]
