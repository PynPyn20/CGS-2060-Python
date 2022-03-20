#
#Secure Patient Info
#

enterTime = 0
signIn = False

while (enterTime != 3) and signIn == False:
    try:
        enterTime += 1
        passwordNumber = input("Please enter your password: ")
        if passwordNumber == 'password':
            signIn = True
            infile = open("Patient Data.txt", "r")
            for line in infile:
                print(line.strip())
            infile.close()
        else:
            raise ValueError
    except ValueError:
        print ("Incorrect! Please try again")
        print ("You have", 3-enterTime, "times remaining")
        if enterTime == 3:
            print("You are locked out")
    finally:
        continue

