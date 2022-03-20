


infileRonda = open("Lesson 17 - Rousey Data.txt", "r")

line = infileRonda.readline()
firstMatch = line.strip().split(",")

line = infileRonda.readline()
secondMatch = line.strip().split(",")

line = infileRonda.readline()
thirdMatch = line.strip().split(",")

line = infileRonda.readline()
fourthMatch = line.strip().split(",")

line = infileRonda.readline()
fifthMatch = line.strip().split(",")

line = infileRonda.readline()
sixthMatch = line.strip().split(",")

line = infileRonda.readline()
seventhMatch = line.strip().split(",")

line = infileRonda.readline()
eighthMatch = line.strip().split(",")

line = infileRonda.readline()
ninthMatch = line.strip().split(",")

line = infileRonda.readline()
tenthMatch = line.strip().split(",")

cleanFirstMatch = (firstMatch[3], firstMatch[1])
cleanSecondMatch = (secondMatch[3], secondMatch[1])
cleanThirdMatch = (thirdMatch[3], thirdMatch[1])
cleanFourthMatch = (fourthMatch[3], fourthMatch[1])
cleanFifthMatch = (fifthMatch[3], fifthMatch[1])
cleanSixthMatch = (sixthMatch[3], sixthMatch[1])
cleanSeventhMatch = (seventhMatch[3], seventhMatch[1])
cleanEighthMatch = (eighthMatch[3], eighthMatch[1])
cleanNinthMatch = (ninthMatch[3], ninthMatch[1])
cleanTenthMatch = (tenthMatch[3], tenthMatch[1])

threeFastestMatches = [cleanFirstMatch]+[cleanSecondMatch]+[cleanThirdMatch]+[cleanFourthMatch]+[cleanFifthMatch]+[cleanSixthMatch]+[cleanSeventhMatch]+[cleanEighthMatch]+[cleanNinthMatch]+[cleanTenthMatch]
print("Top three fastest matches that Ronda has won and how she won are ", sorted(threeFastestMatches) [0:3])