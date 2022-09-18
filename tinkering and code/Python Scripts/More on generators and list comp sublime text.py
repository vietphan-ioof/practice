input_list = [5, 6, 8, 10, 20, 55, 7, 7, 0, 8, 9, ]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


def cunt(x):
    return x + 5


xyz = [print(cunt(i)) for i in input_list if div_by_five(i)]
'''
for x in range(5):
    print(x)
    for xx in range(10):
        print(xx)


xyz1 = (({y, yy} for y in range(5)) for yy in range(5))
print(xyz1)


for word in xyz1:
    for xxx in word:
        print(xxx)
'''

xyz = (x for x in range(100000000)

print(xyz)

for match in xyz:
    print(match)
