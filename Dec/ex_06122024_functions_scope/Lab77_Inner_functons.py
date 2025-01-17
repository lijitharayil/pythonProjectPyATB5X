def outer_function():
    var1 = 30

    def inner_functions():
        print(var1)

    def inner_functions_2():
        print(var1)

    inner_functions()
    inner_functions_2()

outer_function()
