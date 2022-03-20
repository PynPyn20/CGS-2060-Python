#
#The Blizzard Problem
#
candyCravers= ["Reese’s Peanut Butter Cup","Butterfinger","Oreo","Heath","M&M’s"]
classicCreations=["Banana Split","Salted Caramel Truffle","M&M’s Peanut Butter Monster Cookie",
                  "Georgia Mud Fudge","Double Fudge Cookie Dough","Chocolate Xtreme","Peanut Butter Cookie Dough Smash",
                  "Chocolate Chip Cookie Dough","Royal Rocky Road","Chocolate Covered Strawberry","Choco Covered Strawberry",
                  "Royal Rocky Road","Turtle Pecan Cluster","Mint Oreo","Royal New York Cheesecake","Royal Oreo"]

#Print out the lists: one item per line.
for item in candyCravers:
    print(item)
for item in classicCreations:
    print(item)

#In the Candy Cravers list, print the Heath item’s location.
n = candyCravers.index("Heath")
print("Heath location is: ",n)

#In the Classic Creations list, print the Royal Rocky Road item.
if "Royal Rocky Road" in classicCreations:
    print("Royal Rocky Road")

#Add a new Classic Creation: "red licorice". Print new list.
classicCreations.append("Red Licorice")
print(classicCreations)

#Remove the Heath Blizzard from Candy Cravers. Print new list.
candyCravers.remove("Heath")
print(candyCravers)

#Combine the lists and print on one line
newList = candyCravers+classicCreations
print(newList)

#Print a count of the total number of treats provided
print(len(newList))
