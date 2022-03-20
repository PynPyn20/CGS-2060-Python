#
# The UPC Code
#

upcCode = "020357122682"

print ("One digit number {0},Five-digit manufacturer's code {1},Five-digit product code {2},One check digit {3}".format (upcCode [0], upcCode [1:6], upcCode [6:11], upcCode [11]))

itemCost = 275.15
quantity = 12
totalCost = itemCost* quantity

print ("unitCost = ${0:,.2f}, quantity = {1}, totalCost = ${2:,.2f}".format(itemCost, quantity, totalCost))
