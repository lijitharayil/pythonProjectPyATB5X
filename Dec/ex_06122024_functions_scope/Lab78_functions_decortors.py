def add_security(func):

    def wrapper():
        print("1.Before the function is called")
        print("1.wear helmet,2.knee gloves 3.License")

        func() #driving_a_scooty()
        print("After the function is called")
        print("Secure driving,Leave all the items")

    return wrapper()


@add_security

def driving_a_scooty():
    print("Normal functiom")
    print("i'm driving a scooty")