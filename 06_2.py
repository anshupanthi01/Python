eng = int(input("Enter marks for english: "))
math = int(input("Enter marks for math: "))
science = int(input("Enter marks for science: "))
 
# Check for total percentage
total_percentage = (100*(eng + math + science))/300

if(total_percentage>=40):
    print("You are pass...", total_percentage)

else:
    print("You have failed...", total_percentage)