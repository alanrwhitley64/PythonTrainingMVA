import datetime
curDate = datetime.date.today()
#strftime formats the time
#print(curDate.strftime('%A %d %B,%Y'))
#Assessment for datetime chapter - compute days to completion
dueDateStr = input('Enter the due date in yyyy-mm-dd format ')
dueDate = datetime.datetime.strptime(dueDateStr,"%Y-%m-%d").date()
daysLeft = dueDate - curDate
daysLeftInt = daysLeft.days
weeksLeft = int(daysLeftInt / 7)
extraDays = daysLeftInt%weeksLeft
print("You have {0:d} days to complete the project".format(daysLeft.days))
print("which is also {0:d} weeks and {1:d} days".format(weeksLeft,extraDays))
