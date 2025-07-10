#1. Check if a number is an armsstrong number
i=0
s=0
n=int(input("Enter the number"))
while n!=0:
    i=n%10
    n=n/10
    s=s+i
    break
print(s)