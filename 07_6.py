# 5 X 4 X 3 X 2 X 1 (factorial)

n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
    
print(f"The factorial of {n} is: {fact}")