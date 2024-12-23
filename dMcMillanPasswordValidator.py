def main():
    sName = input("Enter first and last name: ")
    sPassword = input("Enter new password: ")
    boolValid = False
    iCount = 0
    while boolValid == False:
        sCheck = sName[iCount]
        if sCheck == " ":
            boolValid = True
        iCount = iCount+1
    sInitials = sName[0] + sName[iCount]
    boolValid = False
    while boolValid == False:
        boolValid = True
        if len(sPassword) < 8 or len(sPassword) > 12:
            print("Password must be between 8 and 12 characters")
            boolValid = False
        if sPassword[:4].lower() == "pass":
            print("Password can't start with Pass")
            boolValid = False
        boolUpper = False
        boolLower = False
        boolNumber = False
        boolSpecial = False
        lDupe = []
        sCopy = ""
        boolDupe = False
        boolDupe2 = False
        for c in sPassword:
            if c.isupper() == True:
                boolUpper = True
            if c.islower() == True:
                boolLower = True
            if c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9" or c == "0":
                boolNumber = True
            if c == "!" or c == "@" or c == "#" or c == "$" or c == "%" or c == "^":
                boolSpecial = True
            if c.upper() in sCopy:
                iCount = 0
                boolDupe = True
                boolDupe2 = False
                while boolDupe2 == False:
                    sCheck = sCopy[iCount]
                    if sCheck == c.upper():
                        boolDupe2 = True
                        sGrab = lDupe[iCount]
                        sGrab2 = sGrab[0]
                        iChange = int(sGrab[1])+1
                        lDupe[iCount] = sGrab2 + str(iChange)
                    else:
                        iCount = iCount+1
            else:
                sUpper = c.upper()
                sCopy = sCopy + sUpper
                lDupe.append(sUpper+"1")
        if boolUpper == False:
            print("Password must contain at least 1 uppercase letter")
            boolValid = False
        if boolLower == False:
            print("Password must contain at least 1 lowercase letter")
            boolValid = False
        if boolNumber == False:
            print("Password must contain at least 1 number")
            boolValid = False
        if boolSpecial == False:
            print("Password must contain at least 1 of these special characters: ! @ # $ % ^ ")
            boolValid = False
        if sInitials.upper() in sPassword.upper():
            print("Password must not contain user initials")
            boolValid = False
        if boolDupe == True:
            print("These characters appear more than once: " )
            iCount = 0
            for c in lDupe:
                sGrab = lDupe[iCount]
                sGrab2 = sGrab[0]
                iChange = int(sGrab[1])
                if int(iChange) > 1:
                    sPrint = sGrab2 + ": " + sGrab[1] + " times"
                    print(sPrint)
                iCount = iCount +1
            boolValid = False
        if boolValid == True:
            print("Password is valid and OK to use")
        else:
            sPassword = input("\nEnter new password: ")
main()