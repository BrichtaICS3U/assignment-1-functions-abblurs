# Assignment 1
# ICS3U
# Abbey Jayne
# March 28, 2018

def CtoF(C):
    """Given a temperature in degrees Celcius, determine the
    temperature in degrees Fahrenheit.
    """
    return round((1.8)*C + 32)

def FtoC(F):
    """Given a temperature in degrees Fahrenheit, determine the
    temperature in degrees Celcius.
    """
    return round((0.55556)*(F-32))

answer = str(input("If you would like to convert temperature from Celsius to Fahrenheit, enter A. If you would like to convert temperature from Fahrenheit to Celsius, type B. "))

if answer == "A":
    C = float(input("Enter your temperature in degrees Celsius: "))
    if C <= -273.15:
        print("Physically impossible temperature. Restart and enter a warmer temperature")
        exit()
    print("This temperature in degrees Fahrenheit is " + int(CtoF(C)))
elif answer == "B":
    F = int(input("Enter your temperature in degrees Fahrenheit: "))
    if F <= -459.67:
        print("Physically impossible temperature. Restart and enter a warmer temperature")
        exit()
    print("This temperature in degrees Celsius is " + str(FtoC(F)))
else:
    print("Invalid option. Choose either A or B.")
    exit()

    

