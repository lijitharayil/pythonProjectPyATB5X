# Find out leap year

year = int(input("Enter the year\n"))

if year % 4==0 and year % 100!=0:
    print("This is a leap year")
else:
    print("This is not a leap year")


