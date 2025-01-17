def add_beroe_test_UI_after_test_UI(func):

    def wrapper():
        print("before open the brower")
        func()
        print("After close the browser")
        
    return wrapper()

@add_beroe_test_UI_after_test_UI
def test_ui():
    print("i will test the UI")