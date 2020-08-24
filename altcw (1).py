import random

#checks the password if its valid 
def checkPass(passW):
    numC = 0
    lowC = 0
    upC = 0
    repeatedCount = 0
    for i in range(len(passW)): # Values are checked if they are uppercase, lowercase or a number
        valCh = ord(passW[i])
        if valCh >= 48 and valCh <= 57:
            numC += 1
        elif valCh >= 65 and valCh <= 90:
            upC += 1
        elif valCh >= 97 and valCh <= 122:
            lowC += 1
    for j in range(len(passW)): #Comparison of letters and keeps a record of repeated letters
        if passW[j].lower() == passW[j-1].lower():
            repeatedCount += 1
        else:
            repeatedCount += 0
    if numC == 0 or upC == 0 or lowC == 0:
        print("Invalid")
    elif repeatedCount >= 1:
        print("not Valid")
    else:
        print(passW)


#generates a password
passW = ""
lengthP = random.randint(8,13)
for i in range(lengthP):
    anyCh = random.randint(0,2)
    if anyCh == 0:
        nums = chr(random.randint(48,57))
        passW += nums
    elif anyCh == 1:
        ups = chr(random.randint(65,90))
        passW += ups
    else:
        lows = chr(random.randint(97,122))
        passW += lows
  

checkPass(passW)


