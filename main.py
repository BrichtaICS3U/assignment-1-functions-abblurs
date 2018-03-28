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
    C = int(input("Enter your temperature in degrees Celsius: "))
    print("This temperature in degrees Fahrenheit is " + str(CtoF(C)))
elif answer == "B":
    F = int(input("Enter your temperature in degrees Fahrenheit: "))
    print("This temperature in degrees Celsius is " + str(FtoC(F)))
else:
    print("Invalid option. Choose either A or B.")
    os.execl(sys.executable, sys.executable, *sys.argv)
    

