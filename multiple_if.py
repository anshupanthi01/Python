a = int(input("Enter your age: "))

# If statement no. 1
if(a%2 == 0):
    print("a is even.")
# End of If statement no. 1

# If statement no. 2
if(a>=18):
    print("You are an adult.")

elif(a<0):
    print("Invalid age.")

elif(a==0):
    print("You are entering 0.")

else:
    print("You are not an adult.")
# End of If statement no. 2

 
print("End of program...")
