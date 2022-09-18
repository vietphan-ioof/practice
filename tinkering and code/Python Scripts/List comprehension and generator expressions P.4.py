input_list = [5, 6, 8, 10, 20, 55, 7, 7, 0, 8, 9, ]

def div_by_five(num):
    if num % 5 ==0:
        return True
    else:
        return False
    yield num
xyz = (i for i in input_list if div_by_five(i) )
print(xyz)
#xyz = []
#or i in input_list():
 #   if div_by_five(i):

[print(i) for i in xyz]




bruh = (((i, ii) for ii in range(500)) for  i in range(5))

print(bruh)


#for i in range(5):
 #      for x in range(5):
  #          print(x)




for x in xyz:
    for xx in xyz:
        print(x)