import Numerology
def main():
    sName = input("Enter your full name: ")
    while (sName == ""):
        sName = input("Name cannot be empty enter name: ")
    sDOB = input("Enter your date of birth in mm/dd/yyyy format: ")
    while (len(sDOB) != 10):
        sDOB = input("Date of birth needs to be in mm/dd/yyyy format please enter date of birth: ")
    num = Numerology.Numerology(sName, sDOB) #object for the numerology file which allows everything to work
    sName1 = str(num.getName())
    sDOB1 = str(num.getBirthdate())
    sLife = str(num.getLifePath())
    sDay = str(num.getBirthDay()) #calls all the required functions and returns the value needed for the print in string
    sAttitude = str(num.getAttitude())
    sSoul = str(num.getSoul())
    sPersonality = str(num.getPersonality())
    sPower = str(num.getPowerName())
    print("Client Name: "+ sName1 + "\nClient DOB: "+ sDOB1 +"\nLife Path: " + sLife + "\nAttitude: "+ sAttitude +"\nBirthday: " + sDay +"\nPersonality: "+ sPersonality +"\nPower Name: "+ sPower +"\nSoul: " +sSoul)
main()