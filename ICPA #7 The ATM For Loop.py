#
#The ATM Machine Problem For Loop
#

amount = int(input("Enter the amount: "))
for x in range (0, amount, 100):
    if amount >= 100:
        print ("$100")
        amount -= 100
for x in range (0, amount, 50):
    if amount >= 50:
        print ("$50")
        amount -= 50
for x in range (0, amount, 20):
    if amount >= 20:
        print ("$20")
        amount -= 20
for x in range (0, amount, 10):
    if amount >= 10:
        print ("$10")
        amount -= 10
for x in range (0, amount, 5):
    if amount >= 5:
        print ("$5")
        amount -= 5
for x in range (0, amount, 1):
    if amount >= 1:
        print ("$1")
        amount -= 1