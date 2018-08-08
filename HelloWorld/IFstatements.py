deposit = float(input("How much do you want to deposit? "))
if deposit > 1000.00 :
    print("You get a free TV")
    print("Ask your teller for details")
elif deposit > 100.00 :
    print("You get a free toaster")
    print("Have a bagel")
else:
    print("You get a $10 gift certificate")
    print("It will be mailed to you within 10 days")
print("Have a nice day!")
