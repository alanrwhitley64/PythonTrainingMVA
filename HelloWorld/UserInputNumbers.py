
# This calculates the monthly payment amount from user input
loanAmt = input("Enter loan amount ")
intRate = input("Enter the annual interest rate as 0.xx ")
numPays = input("Enter the total number of payments ")
L = float(loanAmt)
i = float(intRate) / 12
n = float(numPays)
M = L*(i*(1+i)**n) / (((1+i)**n)-1)
print("Monthly payment = $ {0:.2f}".format(M))