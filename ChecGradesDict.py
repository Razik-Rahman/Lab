s = {}
n = int(input("Enter the limit "))
for i in range(n):
    score = int(input("Enter the score: ")) 
    name = input("Enter the name: ")             
    s[score] = name
for k,v in s.items():
    print(f"Score: {k}, Name:{v}")

