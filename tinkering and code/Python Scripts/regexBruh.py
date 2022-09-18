

def parseAuthors(string):
    list = []
    for x in range(0, len(string)):
       if(string[x] == "'") :
        x+=1
        while string[x] != "'":
            list.append(string[x])



    return list



text = "[{'name': 'Ahmed Osman'}, {'name': 'Wojciech Samek'}]"
print(parseAuthors(text))
print('p[ease')

