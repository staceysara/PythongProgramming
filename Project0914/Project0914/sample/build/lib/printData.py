
def printData(data,level=0):
    for item in data:
        if isinstance(item,list): #item¿Ã list¿Ã∏È
            printData(item,level+1)
        else:
            for i in range(level):
                print('\t',end='')
            print(item)

