s1 = int(input("Enter the marks for subject1: "))
s2 = int(input("Enter the marks for subject2: "))
s3 = int(input("Enter the marks for subject3: "))

#check for totol percentage
total_percentage = (100*(s1+s2+s3))/300

if(total_percentage >=40 and s1 <=33 and s2 <=33 and s3 <=33 ):
    print("you are pass", total_percentage)
else:
    print("You failed",total_percentage)
     



