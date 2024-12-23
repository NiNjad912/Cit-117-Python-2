#Dante McMillan list and real estate analyzer
def getDataInput(): ##Opens file and reads and returns a list based on it
    file = open("RealEstateData.csv", "r")
    listData = file.readlines()[1:]
    file.close()
    return listData
def getMedian(list): ##gets the median of a list and returns it
    if len(list) % 2 == 0:
        fLen = len(list) / 2
        return int(list[fLen]) + int(list[fLen+1])
    else:
        fLen = int(len(list) / 2)
        return list[fLen]
def main():
    listdata = getDataInput()
    dCity = {}
    dProperty = {}
    lPrice = []
    i1 = 0
    i2 = 0
    i3 = 0
    iCount = 0
    sCity = ""
    sProperty = ""
    iPrice = 0
    iTotal = 0
    fAverage = 0.0
    iLen = 0
    iMedian = 0
    for i in listdata:
        i1 = i.find(",")+1
        i2 = i.find(",", i1)
        sCity = i[i1:i2]
        i3 = 0
        iCount = 0
        boolCheck = False
        for x in i:
                if x == ',':
                    i3 = i3 + 1
                if i3 == 7 and boolCheck != True:
                    i1 = i.find(",", iCount)+1
                    i2 = i.find(",", i1)
                    sProperty = i[i1:i2]
                    boolCheck = True
                if i3 == 8:
                    break
                iCount = iCount + 1
        i1 = i.find(",", iCount)+1
        i2 = i.find(",", i1)
        iPrice = int(i[i1:i2])
        iTotal = iTotal + iPrice
        lPrice.append(iPrice)
        if sCity in dCity:
            dCity[sCity] = dCity[sCity] + iPrice
        else:
            dCity[sCity] = iPrice
        if sProperty in dProperty:
            dProperty[sProperty] = dProperty[sProperty] + iPrice
        else:
            dProperty[sProperty] = iPrice
    lPrice.sort()
    iLen = len(lPrice)
    fAverage = iTotal / iLen
    iMedian = getMedian(lPrice)
    print('{:20}'.format("Minimum"), format(lPrice[0], "15,.2f"))
    print('{:20}'.format("Maximum"), format(lPrice[-1], "15,.2f"))
    print('{:20}'.format("Sum"), format(iTotal, "15,.2f"))
    print('{:20}'.format("Average"), format(fAverage, "15,.2f"))
    print('{:20}'.format("Median"), format(iMedian, "15,.2f"))
    print("\nSummary by Property Type:")
    for i in dProperty:
        print('{:20}'.format(i), format(dProperty[i], "15,.2f"))
    print("\nSummary by City:")
    for i in dCity:
        print('{:20}'.format(i), format(dCity[i], "15,.2f"))
main()