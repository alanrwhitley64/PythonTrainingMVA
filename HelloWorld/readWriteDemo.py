print("Starting test")
fileName = 'testWrite2.txt'
WRITE = 'w'
APPEND = 'a'
myFile = open(fileName, mode = WRITE) 
 
myFile.write('Hello There\n') 
myFile.write('Writing a file\n') 
myFile.write('and this is another line.\n') 
myFile.write('This works fine.\n') 
 
myFile.close() 
print("All done with write test")

print("Starting the append test")

file = open(fileName, mode = APPEND) 
 
file.write('Hello Again\n') 
file.write('Writing more lines to the file\n') 
file.write('and this is another line.\n') 
file.write('This works fine, too.') 
 
file.close() 
print("All done with append test")
