a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if(a>b and a>c and a>d):
    print("a is the largest number.", a)

elif(b>a and b>c and b>d):
    print("b is the largest number.", b)
   
elif(c>a and c>b and c>d):
    print("c is the largest number.", c) 

else:
    print("d is the largest number.", d)

print("End of program....")