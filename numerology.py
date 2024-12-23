class Numerology:
    def __init__(self, sName, sDOB):
        global sName1
        sName1 = sName
        global sDOB1
        sDOB1 = sDOB
        global iNum1
        global iNum2
        global iNum3
        global iNum4
        global iNum5
        global iNum6
        global iNum7
        global iNum8
        iNum1 = int(sDOB1[0:1])
        iNum2 = int(sDOB1[1:2])
        iNum3 = int(sDOB1[3:4])
        iNum4 = int(sDOB1[4:5])
        iNum5 = int(sDOB1[6:7])
        iNum6 = int(sDOB1[7:8])
        iNum7 = int(sDOB1[8:9])
        iNum8 = int(sDOB1[9:10])
    def getName(self):
        return sName1.upper()
    def getBirthdate(self):
        return sDOB1
    def getAttitude(self):
        iAttitude = iNum1 + iNum2 + iNum3 + iNum4
        if (iAttitude > 9):
            iAttitude = Numerology.__greaterThan9(iAttitude)
        return iAttitude
    def getBirthDay(self):
        iBirthDay = iNum3 + iNum4
        if (iBirthDay > 9):
            iBirthDay = Numerology.__greaterThan9(iBirthDay)
        return iBirthDay
    def getLifePath(self):
        iLifePath = iNum1 + iNum2 + iNum3 + iNum4 + iNum5 + iNum6 +iNum7 +iNum8
        if (iLifePath > 9):
            iLifePath = Numerology.__greaterThan9(iLifePath)
        return iLifePath
    def getPersonality(self):
        global iPersonality
        iPersonality = 0
        iCurrent = 0
        sCaps = sName1.upper()
        i = 0
        while (i<len(sName1)):
            sCurrent = sCaps[iCurrent]
            if (sCurrent == 'J' or sCurrent =='S'):
                iPersonality += 1
            elif(sCurrent == 'B'or sCurrent == 'K'or sCurrent =='T'):
                iPersonality += 2
            elif(sCurrent =='C'or sCurrent == 'L'):
                iPersonality += 3
            elif(sCurrent =='D'or sCurrent =='M' or sCurrent =='V'):
                iPersonality+=4
            elif(sCurrent =='N' or sCurrent =='W'):
                iPersonality+=5
            elif(sCurrent =='F' or sCurrent =='X'):
                iPersonality+=6
            elif(sCurrent =='G'or sCurrent =='P' or sCurrent =='Y'):
                iPersonality+=7
            elif(sCurrent =='H'or sCurrent =='Q' or sCurrent =='Z'):
                iPersonality+=8
            elif(sCurrent =='R'):
                iPersonality+=9
            i = i+1
            iCurrent = iCurrent + 1
        if (iPersonality>9):
            iPersonality = Numerology.__greaterThan9(iPersonality)
        return iPersonality
    def getPowerName(self):
        iPower = iSoul + iPersonality
        if (iPower > 9):
            iPower = Numerology.__greaterThan9(iPower)
        return iPower
    def getSoul(self):
        global iSoul
        iSoul = 0
        iCurrent = 0
        sCaps = sName1.upper()
        i = 0
        while (i<len(sName1)):
            sCurrent = sCaps[iCurrent]
            if(sCurrent =='A'):
                iSoul+=1
            elif(sCurrent =='U'):
                iSoul+=3
            elif(sCurrent =='E'):
                iSoul+=5
            elif(sCurrent =='O'):
                iSoul+=6
            elif(sCurrent =='I'):
                iSoul+=9
            i = i+1
            iCurrent = iCurrent + 1
        if (iSoul > 9):
            iSoul = Numerology.__greaterThan9(iSoul)
        return iSoul
    def __greaterThan9(i):
        while (i > 9):
            s = str(i)
            s1 = s[0:1]
            s2 = s[1:2]
            i = int(s1) + int(s2)
        return i