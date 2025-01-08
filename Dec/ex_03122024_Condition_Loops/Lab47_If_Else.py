# Find the max numbers from given input

num1=float(input("Enter a first number\n"))
num2=float(input("Enter a second number\n"))
num3=float(input("Enter a third number\n"))


# num1 > num2 and num1 >num3 --> num1
# num2 > num1 and num2> num3 --> num2

if num1 > num2 and num1 >num3:
    print("the max number is",num1)
elif num2 > num1 and num2> num3:
    print("the max number is",num2)
else:
    print("the max number is",num3)


