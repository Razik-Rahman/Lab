s = int(input("Enter the score: "))

if s>100 or s<0:print("Invalid Score")
elif s>=90:print("A")
elif  s>=80:print("B") 
elif s>=70:print("C")
elif s>=60:print("D")
elif s<60:print("F")