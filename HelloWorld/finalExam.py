def main():
#open the CSV translation file
    import csv
    myCSV = open('C:\\txtMsgAbbrev.csv', 'r')
    print("CSV Abbreviation File opened successfully")
#get the input and output file names
    inFileName, outFileName = getTxtMsg() 
#translate the abbreviations into full text
    translateTxt(inFileName, outFileName, myCSV)

    myCSV.close()
    return


def getTxtMsg():
#get the input file
    import time
    import sys
    print("Enter the input file name to be translated")
    inFileName = input("> ")
    try :
        with open(inFileName, 'r') as myInFile:
            print("Input file validated")
            myInFile.close()
    except FileNotFoundError:
        print("Sorry. " + inFileName + " could not be found")
        print("Program must be shut down")
        time.sleep(5)
        sys.exit()
    except:
        errorMsg = sys.exc_info()[0]
        print(errorMsg)
        time.sleep(5)
        sys.exit()
#Now get the output file
    print("Enter the file name of the translated file(output)")
    outFileName = input("> ") 
    
    return inFileName, outFileName


def translateTxt(inFileName, outFileName, myCSV):
    import csv
# open the output file
    txtOutFile = open(outFileName, 'w+')
    print("Output file is ready")
#open the input that was pre-validated
    txtInFile = open(inFileName, 'r')
    print("Input file opened")
#check for EOM
    eofIn = False
    txtInLine = txtInFile.readline()
    txtOutLine = ""
    if txtInLine == "":
        eofIn = True
#loop thru the file until we reach EOF
    while not eofIn:
        wordList = txtInLine.split(" ")
        numWords = len(wordList)
        txtOutLine = ""
#process each word after removing new line, periods, and commas
        for wordIdx in range(numWords):
            newTxt = wordList[wordIdx].replace('\n', '')
            newTxt = newTxt.replace(".","")
            newTxt = newTxt.replace(",","")
#reset the myCsv pointer to the first row
            myCSV.seek(0)
            CSVdata = csv.reader(myCSV)
#check each row in translation file and replace it if a match is found
            for currRow in CSVdata:
                if currRow[0] == newTxt:
                    newTxt = currRow[1]
#append each word until entire line is processed
            txtOutLine = (txtOutLine + newTxt + " ")
        txtOutFile.write(txtOutLine + "\n")
#read the next line and check for EOF
        txtInLine = txtInFile.readline()
        if txtInLine == "":
            eofIn = True
            print("Set EOF on input")

    txtInFile.close()
    txtOutFile.close()
    print("The translated file " + outFileName + " has been created")
    return

#execute the main function
main()
