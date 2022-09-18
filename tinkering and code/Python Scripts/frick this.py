inventory = {'arrow': 12, 'gold coin': 42, 'rope':  1, 'torch': 6, 'dagger':  1}

def displayInventory(any_inventory):
    global y
    print('inventory : ')
    total = 0
    for x, y in any_inventory.items():
        total += y
        print(y, x)
    print('Total number of items: ' , total)





displayInventory(inventory)

