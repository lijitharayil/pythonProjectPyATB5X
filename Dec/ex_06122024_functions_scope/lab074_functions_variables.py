pb_global_b=12

def my_functions():
    pb_a=10 # local variable within the functions
    print(pb_a)
    print(pb_global_b)

my_functions()
print(pb_a) # it is a local varibale so we can't this value outside function
print(pb_global_b) # it is a global varibale so we can print this value outside function


