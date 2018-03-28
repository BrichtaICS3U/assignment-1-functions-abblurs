# Assignment 1
# ICS3U
# Abbey Jayne
# March 28, 2018

# FUNCTIONS
def CtoF(C):
    """Given a temperature in degrees Celcius, determine the
    temperature in degrees Fahrenheit.
    """
    return round((1.8)*C + 32) #Rounds to nearest whole degree

def FtoC(F):
    """Given a temperature in degrees Fahrenheit, determine the
    temperature in degrees Celcius.
    """
    return round((0.55556)*(F-32)) #Rounds to nearest whole degree


# DECIDING WHICH CONVERSION USER WANTS
answer = str(input("If you would like to convert temperature from Celsius to Fahrenheit, enter A. If you would like to convert temperature from Fahrenheit to Celsius, type B. "))


# CONVERSION PROCESS
while True: #allows program to continue if user wants to convert again or makes mistake entering input
    if answer == "A": #User wants to convert CtoF
        C = float(input("Enter your temperature in degrees Celsius: ")) #allows user to input decimal temperatures
        if C <= -273.15:    #absolute zero or colder = impossible
            print("Physically impossible temperature. Restart and enter a warmer temperature")
            continue #Allows user to try again with warmer temperature
        print("This temperature in degrees Fahrenheit is " + str(CtoF(C)))
        cont = str(input("Would you like to make another conversion? Type yes or no: "))
        if cont == "yes" or cont == "Yes": #decide whether or not to do another conversion
            continue
        else:
            print("Have a nice day!")
            exit()

    elif answer == "B": #User wants to convert FtoC
        F = int(input("Enter your temperature in degrees Fahrenheit: "))
        if F <= -459.67: 
            print("Physically impossible temperature. Restart and enter a warmer temperature")
            continue 
        print("This temperature in degrees Celsius is " + str(FtoC(F)))
        cont = str(input("Would you like to make another conversion? Type yes or no: "))
        if cont == "yes" or cont == "Yes":
            continue
        else:
            print("Have a nice day!")
            exit()

    else: #User did not enter A or B because they clearly can't read
        print("Invalid option. Choose either A or B.")
        answer = str(input("If you would like to convert temperature from Celsius to Fahrenheit, enter A. If you would like to convert temperature from Fahrenheit to Celsius, type B. "))
        continue

    

