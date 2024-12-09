import os

path = 'D:/bsnes_v115-windows'

def readFilesRecursevly(path):
    for item in os.listdir(path):
        print(item)
        itemPath = path + "/" + item
        if bool(os.path.isfile(itemPath)) is False:
            readFilesRecursevly(itemPath)
    return

readFilesRecursevly(path)