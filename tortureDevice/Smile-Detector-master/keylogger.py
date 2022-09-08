import os 
import time

def checkContents():
    with open('log.txt') as f:
        contents = f.read()
        searchSentence = "jeff bezos is everybody's daddy"
        if searchSentence not in contents:
            print("U HAVE FAILED LOL")
            os.system('mosquitto_pub -h localhost -p 1883 -t test/topic -m \"fire!\"')
            time.sleep(20)
            #play audio clip
        else:
            print("U are saved for now.")
            #play audio clip
















