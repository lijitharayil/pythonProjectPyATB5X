# Grade Caliculator

# step 1
# Enter user input -->score or mark -->int
# o/p --> str -->"A" or "B", or etc

# Step 2
# score = int(input("enter your score\n"))
# score >=90 and score <=100 ="A"
# score >=80 and score <=89 ="B"
# score >=70 and score <=79 ="C"
# score >=60 and score <=69 ="D"
# score >=0 and score <=59 ="E"

score = int(input("enter your score"))

if score >=90 and score <=100 :
    print("your grade is","A")
elif score >=80 and score <=89:
    print("your grade is","B")
elif score >=70 and score <=79:
    print("your grade is", "C")
elif score >=60 and score <=69:
    print("your grade is", "D")
elif score >=1 and score <=59:
    print("your grade is","E")
elif score >100:
    print("This is invalid score, please enter a valid score")
else:
    print("Enter a valid score")

