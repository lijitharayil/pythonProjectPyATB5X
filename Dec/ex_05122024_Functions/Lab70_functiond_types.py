# # 1.They can't return --->no return
# # 2.They can return something
# # 3.They have parameters
# # They don't have parameters/arguments
#
#
# # 1.They can't return --->no return, No retun type, no parameters/arguments
# def greet():#--->parameter
#     print("Hi everyone")#-->return keyword
# greet()
#
# # 2.No retun type with parameter
#
# def greet_with_name(name):
#     print("Hello,",name)
# greet("Liji")

# 3.No retun type with deafult argument

def say_hello_default_name(name="Appu"):
    print("Hello,",name.upper())

say_hello_default_name("Liji Tharayil")
say_hello_default_name()#---->call function is empty so it will take default value


def mul_arguments(name1="A", name2= "B"):
    print("Mul--->",name1,name2)

mul_arguments()    # no parameters so it's empty and default value it will take ie, A and B
mul_arguments("Liji") # Liji will print(it's replaced vth name1)
mul_arguments(name2="Liji") # Liji will print(it's replaced vth name2)
mul_arguments(name1="Appu",name2="Liji") # Liji will print(it's replaced vth name2)


# 4.Argument + Return value

def sum_of_two_num(a,b):
    return a+b
result = sum_of_two_num(56,4)
print(result)

def sum_of_two_default_num(num1=100, num2=200):
    return num1+num2
sum_of_two_default_num()
result = sum_of_two_default_num(num1=30,num2=20)
print(result)
result = sum_of_two_default_num() # default value it will take
print(result)










