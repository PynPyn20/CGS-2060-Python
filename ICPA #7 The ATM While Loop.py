#
#The ATM Machine Problem While Loop
#

amount = int(input("Enter the amount: "))
while (amount >= 1):
    if (amount >= 100):
        print ("$100")
        amount = amount - 100
    elif (amount >= 50):
        print("$50")
        amount = amount - 50
    elif (amount >= 20):
        print("$20")
        amount = amount - 20
    elif (amount >= 10):
        print("$10")
        amount = amount - 10
    elif (amount >= 5):
        print("$5")
        amount = amount- 5
    elif (amount >= 1):
        print("$1")
        amount = amount - 1
