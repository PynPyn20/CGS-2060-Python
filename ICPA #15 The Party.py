#
# The Party
#


foodList = [["Frank", "pizza", 10], ["Mary", "wings", 8], ["Bob", "cookies", 15], ["Lisa", "dip", 20], ["Mark", "brownies", 12], ["Ann", "burgers", 7], ["Henry", "mints", 30], ["Ruth", "hotdogs", 22]]


for loop in range (len(foodList)):
    print("People will bring food: ",foodList[loop][0])
    print("Food will be there are: ", foodList[loop][1])

foodList.pop()
sum = 0
for loop in range (len(foodList)):
    sum += foodList[loop][2]
print("Number of people can be fed if Ruth cancel: ", sum)