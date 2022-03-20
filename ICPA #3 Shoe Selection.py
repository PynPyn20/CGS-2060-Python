# Assignment 6
gender = "Male"
location = "Gym"
swimming = False

if (gender == "Male" or "Female") and (location == "Gym"):
    if swimming == True:
        print("Swim Shoes")
    else:
        print("Gym Shoes")
if (gender == "Male"):
    if (location == "Casual") or (location == "Work"):
        print("Top Siders")
    if (location == "Formal"):
        print("Oxfords")
if (gender == "Female"):
    if (location == "Casual"):
        print("Flats")
    if (location == "Work"):
        print("Pumps")
    if (location == "Formal"):
        print("Heels")
