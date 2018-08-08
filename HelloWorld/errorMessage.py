def main():
    import csv
    import sys
    myFile = input("Please enter the CSV file name to be read and written - ")
    try :
        with open(myFile, 'r') as myCSV:
            CSVdata = csv.reader(myCSV)
            for currRow in CSVdata:
                print(', '.join(currRow))
            print("Success!!!")
    except FileNotFoundError:
        print("Sorry. " + myFile + " could not be found")
    except:
        errorMsg = sys.exc_info()[0]
        print(errorMsg)
    return

#can define other functions that are used by main
#and then execute main after all are defined

main()
