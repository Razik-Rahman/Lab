# Write a program to convert celcius to F and kelvin
while True:
    Cel=int(input("Enter the Celcius"))
    print("Convert to\n 1.Fehran\n 2.Kelvin\n 3.Exit ")
    ch=int(input("Enter your choice"))
    if (ch==1):
        F=(Cel*(9/5))+32
        print("Fahrenheit:",F)
    elif (ch==2):
        K = Cel + 273.15
        print("Kelvin",K)
    
    elif (ch==3):
        print("Exiting....")
        break
    
    else:
        print("Invalid")
