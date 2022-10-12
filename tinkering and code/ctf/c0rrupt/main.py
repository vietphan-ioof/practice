import magic

file = magic.from_file("mystery", mime=False)

print(magic.from_buffer(open("mystery").read(2048)))


