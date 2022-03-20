#
#The Challenge Of Being Kim Kardashian
#

pant = input ("What color of pant Kim Kardashian wear (W/B/G/Y): ")
time = input ("What time Kim kardashian goes out ")

if pant == "White":
    shoes = "white stilettos"
elif pant == "Black":
    shoes = "blue wedges"
elif pant == "Green":
    shoes = "Mary Jane"
elif pant == "Yellow":
    shoes = "orange pumps"
else:
    shoes = "brown flats"
if time < "13:00":
    destination = "go to beach"
elif time < "14:00":
    destination = "go for lunch at La Petite"
elif time < "16:00":
    destination = "have nails done at Tips R Us"
elif time < "18:00":
    destination = "go to Flat Tummy gym"
elif time < "20:00":
    destination = "go home and ready to go out"
elif time < "21:00":
    destination = "go to dinner at Racks & Stacks BBQ"
elif time < "23:00":
    destination = "go see movie at The 24 Multiplex"
else:
    destination = "hit the club at The Backdoor"

print ("Kim Kardashian wants to wear", shoes, "and will", destination)

