moreToEnter = True
guestList = []
#Loop until finished
while moreToEnter :
    guestName = input("Enter guest name ")
    finished = input("Are you finished? Enter y or n ")
    if finished == 'y':
        moreToEnter = False
    guestList.append(guestName)

#Have all the names, now sort the list
#To sort descending use .sort(reverse=True)
guestList.sort()

#Print the guest list
print("Here is the sorted guest list/n")
for curGuest in guestList:
    print(curGuest)

print("All done")


