#Check whether the number is prime number

n=int(input("Enter the number"))
i=0
for i in range(1,n):
    if n%i==0:
        print("It is not prime")
    else:
        print("It is prime")
    break
 
