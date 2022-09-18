CORRECT_COMBO = (3, 6, 5)
'''
found_combo = False
for x in range(10):
    if found_combo:
        break
    for y in range(10):
        if found_combo:
            break
        for z in range(10):
            if found_combo:
                break
            if (x, y, z) == CORRECT_COMBO:
                print('Found the combo: {}'.format((x, y, z)))
                break
            print(x, y, z)
'''


def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)


for (c1, c2, c3) in combo_gen():
    if (c1, c2, c3) == CORRECT_COMBO:
        print(print('Found the combo: {}'.format((c1, c2, c3))))
        break
    print(c1, c2, c3)

for x in range(5):
    for y in range(x):
        print(x, y)
