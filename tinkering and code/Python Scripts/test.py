import asyncio
import websockets
import random


random.seed(2)

async def hello(websocket, path):

    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    #await websocket.send("0x4555, ffff, fff")
    await websocket.send("0x4555, ffff, fff {}".format(random.random()))
    print(f">{greeting}")



    '''

    data = []
    while True:
        message = await websocket.recv()
        print(f"< {message}")

        data.append(message)


        if message == "done":
            returnData(data)


    '''
'''
    bruh = False
    data = []

    message = await websocket.recv()
    print(f"< {message}")

    data.append(message)

    if message == "done":
       bruh = processData(data)
       break

    await websocket.send("hey shawty")
'''


           # await websocket.send("blockdata")
'''
    consumerTask = asyncio.ensure_future(receiveMessage(websocket, path))
    producerTask = asyncio.ensure_future(produceMessage(websocket, path))

    done, pending = await asyncio.wait([consumerTask, producerTask], return_when=asyncio.FIRST_COMPLETED)

    for task in pending:
        task.cancel()

'''
#The server only communicates by the the host server starting up and then the computer contacts it when its ready
   # when the computer sends in the data to the server you would check if the block is mined already
    # if its mined already then you send a new block and new data
    # if it mined successfully then process the data
    # if it is the first time connecting then process then send block data and await for future messages

print('hi')
startServer = websockets.serve(hello, "localhost", 8765)
print("works!")


asyncio.get_event_loop().run_until_complete(startServer)
asyncio.get_event_loop().run_forever()


