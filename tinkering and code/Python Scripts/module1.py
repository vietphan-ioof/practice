### Ending a program with sys.exit()
while True:
     print('you must answer this riddle correctly or u will terminate this whole computer HAHAHAHAH')
     print('What is 1+1/1 + 1??')
     answer = input()
     if answer == 2:
        continue
        print('good job my fellow friend u have failed.  i will now terminate in....')
        import time
        def countdown(n) :
            while n > 0:
                print(n)
                n = n - 1
                if n == 0:
                    sys.exit()
            countown(20)



