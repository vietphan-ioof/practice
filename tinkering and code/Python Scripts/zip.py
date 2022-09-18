x = [1, 2, 3, 4, 5, 6]
y = [4, 5, 6, 7, 8, 9]
z = ['car', 'bus', 'goat', 'Cute']

for x, z, y in zip(x, y, z):
    print(z, y, x)
# ZIp is a zip object

#print(list(zip(x, y, z)))


# for a in zip(x, y, z):
#   print(a)


#[print(x, y) for a, b, c in zip(a, b)]


def car(a, b):
    return (a == 6 or b == 6)


print(car(5, 6))
