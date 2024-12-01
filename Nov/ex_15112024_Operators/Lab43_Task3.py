#if the user age is 21, then if he can go to the club or not?

user_age = int(input("enter your age"))

if user_age > 21:
    print("the user can go to the club")
else:
    print("User can't go the club")

print("the user can go to the club" if user_age >21 else "User can't go the club" )