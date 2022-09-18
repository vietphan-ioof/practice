def square_numbers(nums):
    for i in nums:
            yield (i*i)
my_nums = square_numbers([1,2,3,4,5,])

print(my_nums)

for i in my_nums:
    print(i)

#print next(my_nums)


my_nums1 = [x*x for x in [1, 2, 3, 4, 5]]

print(my_nums1)


my_nums1 = (x*x for x in range(100000000000))

for x in my_nums1:
    print(x)


