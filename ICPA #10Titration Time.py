#
#Titration Time
#

pressButton = 0.5
titration = 0

while titration != 18:
   titration = float(titration + pressButton)
   print (titration)
   if titration == 10:
      print ("The titration turn to blue")
      answer = input ("Do you want to add more? ")
      if answer == "yes":
           continue
      if answer == "no":
            break
if titration == 18:
    print ("You cannot add anymore")