import os 

def checkContents():
    with open('log.txt') as f:
        contents = f.read()
        searchSentence = "jeff bezos is everybody's daddy"
        if searchSentence not in contents:
            print("U HAVE FAILED LOL")
            #play audio clip
        else:
            print("U are saved for now.")
            #play audio clip
















