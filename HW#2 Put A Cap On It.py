# 
# CGS 2060 – Spring Semester 2022 
# 
# Homework #2: Put A Cap On It 
# 
# Phat Tiet, Reyda Rodriguez 
# 
 
infile = open("HW #2 Data.txt", "r")
amountMilkToBeBottled = int(infile.readline())
numberBottleInLot = int(infile.readline())

milkBottle = []   # list to hold information on a single milk bottle
bottleRecord = [] # list to hold the lists with information on all the milk bottles
 
bottlesInBox = 0            # Number of bottles in current box being packed 
currentBoxID = 1            # ID of current box that is being loaded 

milkBottleInOz = amountMilkToBeBottled * 128
ozOfMilkInALot = numberBottleInLot * 16
numberOfLotsNeeded = milkBottleInOz / ozOfMilkInALot
numberOfMilkBottles = numberBottleInLot * numberOfLotsNeeded

#Step 1: Depalletizing

trackingNumEachBottles = 10
for i in range (0, len(numberOfMilkBottles), trackingNumEachBottles):
    print(numberOfMilkBottles[i: i + trackingNumEachBottles])



#Step 2: Filling


#Step 3: Cold Glue Labelling

#Step 4: Packing