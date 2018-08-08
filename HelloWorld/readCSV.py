def main():
    import csv
    with open('osdRFsched.csv', 'r') as myCSV:
        CSVdata = csv.reader(myCSV)
        for currRow in CSVdata:
#prints with [] list format first
            print(currRow[0])
#then prints individual items separated by commas with the []        
            print(', '.join(currRow))
    return

#can define other functions that are used by main
#and then execute main after all are defined

main()
