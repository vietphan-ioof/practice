

def isPrime(num):

    x =2

    while x*x <=num:
        if num % x ==0:
            return False

        x+=1

    return True



num = 600851475143
count = 600851475143-1
largestPrimeFactor = 0


for x in range(600851375144, 2, -1):
    print(x)
    if x%2 == 0:
        continue
    else:
        val = isPrime(x)
        if val == True and num%x == 0:
            largestPrimeFactor = x
            break


print(largestPrimeFactor)
