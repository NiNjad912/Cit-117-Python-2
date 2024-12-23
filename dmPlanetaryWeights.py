#Dante McMillan Inter planitary weights assignment
import pickle 
def main():
    dictPlanetHistory = {}
    dictPersonWeights = {}
    listPlanetHistory = ""
    sHistoryName = ""
    surface_gravity_factors = { "Mercury": 0.38, "Venus": 0.91, "our Moon": 0.165, "Mars": 0.38, "Jupiter": 2.34, "Saturn": 0.93, "Uranus": 0.92, "Neptune": 1.12, "Pluto": .066}
    eof = False #declaring variables to be used later
    try:
        output_file = open("dmPlanetaryWeights.db", "rb") #opening the pickle to read if it exists
        while not eof:
            try:
                listPlanetHistory = pickle.load(output_file)
                sHistoryName = listPlanetHistory[0]
                dictPlanetHistory = listPlanetHistory[1]
            except EOFError:
                eof = True
        output_file.close #closing the pickle so it can then be opened later
        input_file = open("dmPlanetaryWeights.db", "wb") #opening the pickle to allow writing to the pickle later

    except FileNotFoundError: #if the file isnt found create a writable file to use and leave the try block
        input_file = open("dmPlanetaryWeights.db", "wb")
        pass
    sHistory = input("Would you like to see the history y/n: ")
    if sHistory.upper() == "Y":# check if they want to see the history and then display the pickle if they do
                        dictPrint(sHistoryName, dictPlanetHistory)
    boolUniqueName = False
    while boolUniqueName == False: #test to see if the name has already been used and get a unique name if it has
        sName = input("What is your name(enter key to quit):")
        if sName == "":
            boolUniqueName = True
        elif sName.upper() == sHistoryName.upper():
            print(sName + "is already in the history file. Enter an unique name.")
        else:
            boolUniqueName = True
    fWeight = float(input("Enter your weight: "))
    for i, key in enumerate(surface_gravity_factors.keys()): #gets weight and creates a dictionary for all the planetary weights
        fCurrent = surface_gravity_factors[key]
        fMath = fCurrent * fWeight
        dictPersonWeights.update({key: fMath})
    dictPrint(sName, dictPersonWeights) #sends name and dictionary to dictPrint
    listDump = [sName, dictPersonWeights]
    pickle.dump(listDump, input_file)#sends info to pickle
    input_file.close#closes pickle
def dictPrint(sName, dictToPrint):# a small function designed to print the dictionary + name in a way to satisfy criteria
    print(sName + ", here are your weights on our Solar System's planets.")
    for i, key in enumerate(dictToPrint.keys()):
        print('{:20}'.format("Weight on " + key + ":"), format(dictToPrint[key], "10.2f"))
main()