#create a program to sum of 3 numbers from the user input
# if user not entered any value use 100,200 and 300

num1 = int(input("Enter a first number\n"))
num2 = int(input("Enter a second number\n"))
num3 = int(input("Enter a third number\n"))

def sum_of_three_num(num1=100,num2=200,num3=300):
    return num1+num2+num3
result =sum_of_three_num(num1,num2,num3)
print(result)

result =sum_of_three_num()
print(result)

result =sum_of_three_num(num1=1,num2=2)
print(result)



