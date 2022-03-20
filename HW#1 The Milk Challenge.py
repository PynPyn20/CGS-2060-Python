# 
# CGS 2060 Homework #1 - The Milk Challenge 
# 
# Phat Tiet, Reyda Rodriguez 
#

# Step 1: Open data file and read in control variables [HW#1 Data.txt]

infile = open("HW #1 Data.txt", "r")
numOfGallons = int(infile.readline())
pasTemp = int(infile.readline())
coolTemp = int(infile.readline())
numOfNozzle = int(infile.readline())
ultraPressure = int(infile.readline())
reverseOsPressure = int(infile.readline())

# Step 2: Do the pasteurisation processing.
timeOfDay = 0
pasGallons = 0
for x in range (0, numOfGallons):
   timeOfDay += 20
   pasGallons += 1
   print("Process time: ", timeOfDay, "seconds")
   print("Milk process: ", pasGallons)
   print("Current milk temperature: ", pasTemp, "\n")

for x in range (0, numOfGallons):
   timeOfDay += 300
   timeOfDay == 2300
   print("Process time: ", timeOfDay, "seconds")
   print("Current milk temperature: ", coolTemp, "\n")
   break

pasteurisationTime = timeOfDay
print ("    Pasteurisation process took: ", pasteurisationTime, "seconds")
print("    Number of gallon have been pasteurisation: ", numOfGallons)

print ("------------------------------------------------------------------------")
# Step 3: perform homogenisation

homoGallons = 0
for x in range (0, numOfGallons):
   timeOfDay += 10
   homoGallons += 1
   print("Process time: ", timeOfDay, "seconds")
   print("Milk process: ", homoGallons)
   print ("Number of nozzle to use: ", numOfNozzle, "\n")

homogenisationTime = timeOfDay - pasteurisationTime
print ("    Homogenisation process took: ", homogenisationTime,"seconds")
print("    Number of gallon have been homogenisation: ", numOfGallons)

print ("------------------------------------------------------------------------")
# Step 4: The next step will be Ultrafiltration
ultraGallons = 0
for x in range (0, numOfGallons):
   timeOfDay += 5
   ultraGallons += 1
   print("Process time: ", timeOfDay, "seconds")
   print("Milk process: ", ultraGallons)
   print ("Pressure of ultrafiltration: ", ultraPressure, "\n")

ultrafiltrationTime = timeOfDay - pasteurisationTime - homogenisationTime
print ("    Ultrafiltration process took: ", ultrafiltrationTime,"seconds")
print("    Number of gallon have been ultrafiltration: ", numOfGallons)

print ("------------------------------------------------------------------------")

# Step 5: The final step is reverse osmosis
reverseOsGallons = 0
for x in range (0, numOfGallons):
   timeOfDay += 10
   reverseOsGallons += 1
   print("Process time: ", timeOfDay, "seconds")
   print("Milk process: ", reverseOsGallons)
   print ("Pressure of reverse osmosis: ", reverseOsPressure, "\n")

reverseOsmosisTime = timeOfDay - pasteurisationTime - homogenisationTime - ultrafiltrationTime
print ("    Reverse Osmosis process took: ", reverseOsmosisTime,"seconds")
print("    Number of gallon have been reverse osmosis: ", numOfGallons)

print ("------------------------------------------------------------------------")

# Step 6: Final statistics

print("Number of gallon have been process: ", numOfGallons)
print("Total process time           : ", timeOfDay, "\n")
print("Pasteurisation process took  : ", pasteurisationTime)
print("Homogenisation process took  : ", homogenisationTime)
print("Ultrafiltration process took : ", ultrafiltrationTime)
print("Reverse osmosis process took : ", reverseOsmosisTime, "\n")
timeOfDay = 0
for x in range (1,2):
    timeOfDay += 20
    print("One gallon pasteurized in", timeOfDay, "seconds")
for x in range (1,2):
    timeOfDay += 300
    print("One gallon has cooled after", timeOfDay, "seconds")
for x in range (1,2):
    timeOfDay += 10
    print("One gallon homogenised in", timeOfDay, "seconds")
for x in range (1,2):
    timeOfDay += 5
    print("One gallon filtered in", timeOfDay, "seconds")
for x in range (1,2):
    timeOfDay += 10
    print("One gallon osmosized in", timeOfDay, "seconds")

print("Total time one gallon of milk took to process: ", timeOfDay)


infile.close()