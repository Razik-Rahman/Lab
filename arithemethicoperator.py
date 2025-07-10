a = int(input("Enter the number"))
b = int(input("Enter the number"))
r=0
while True:
    print("1.Addition","2.Subtraction","3Multiplication","4.Division","5.Exit")
    ch = int(input("Enter your choice"))
    if(ch==1):
        r=a+b
        print("The Sum is ",r)
    elif(ch==2):
        r=a-b
        print("The Difference is ",r)
    elif(ch==3):
        r=a*b
        print("The Multiplication is ",r)
    elif(ch==4):
        r=a/b
        print("The Quotient is ",r) 
    elif(ch==5):
        print("Exiting")
        break
    else:
        print("Invalid")   

