add=lambda a,b:a+b
mul=lambda a,b:a*b
sub=lambda a,b:a-b
div=lambda a,b:a/b
x = int(input("Enter the number"))
y = int(input("Enter the number"))
while True:
    print("1.Addition,2.Subtraction,3.Multiplication,4.Division,5.Exit")
    ch=int(input("Enter your choice"))
    if (ch==1):
        print("Sum:",add(x,y))
    elif (ch==2):
        print("Difference:",sub(x,y))
    elif (ch==3):
        print("Multiplication:",mul(x,y))
    elif (ch==4):
        print("Division:",div(x,y))
    elif (ch==5):
        print("Exiting....")
        break
    else:
        print("Invalid")