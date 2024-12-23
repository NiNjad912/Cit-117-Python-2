import NumerologyLifePathDetails
def main():
    sName = input("Enter your full name: ")
    while (sName == ""):
        sName = input("Name cannot be empty enter name: ")
    sDOB = input("Enter your date of birth in mm/dd/yyyy format: ")
    while (len(sDOB) != 10):
        sDOB = input("Date of birth needs to be in mm/dd/yyyy format please enter date of birth: ")
    num = NumerologyLifePathDetails.NumerologyLifePathDetails(sName, sDOB) #object for the numerology file which allows everything to work
    num.Name()
    num.BirthDate
    num.LifePath()
    num.Birthday() #calls all the required functions and returns the value needed for the print in string
    num.Attitude()
    num.Personality()
    num.PowerName()
    num.Soul()
    num.LifePathDescription()
main()