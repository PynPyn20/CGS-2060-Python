#
# The ATM Machine
#

amount = int(input())
if amount <= 200:
    if amount > 100:
        print ("$100")
        amount -= 100
    if amount > 99:
        print ("$100")
        amount -= 100
    if amount > 20:
        print ("$20")
        amount -= 20
    if amount > 20:
        print ("$20")
        amount -= 20
    if amount > 20:
        print ("$20")
        amount -= 20
    if amount > 20:
        print ("$20")
        amount -= 20
    if amount > 10:
        print ("$10")
        amount -= 10
    if amount > 5:
        print ("$5")
        amount -= 5
    if amount > 0:
        print ("$1")
        amount -= 1
    if amount > 0:
        print ("$1")
        amount -= 1
    if amount > 0:
        print ("$1")
        amount -= 1
    if amount > 0:
        print ("$1")
        amount -= 1
    if amount > 0:
        print ("$1")
        amount -= 1
