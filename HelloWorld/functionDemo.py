def main():
    myFile = open("testFunctionWrite.txt", 'w+')
    writeMessage("Testing the write", myFile)
    myFile.close()
    return

def writeMessage(message, fileName):
    fileName.write(message)
    return

main()
