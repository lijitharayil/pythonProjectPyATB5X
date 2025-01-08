# write a program to ask the user which browser he want to run the automation
browser_name = input("Enter browser name\n")
match browser_name:
    case "firefox":
        print("Starting firefox!!!!")
    case "Chrome":
        print("Execute the Chrome code")
    case "edge" :
        print("Execute the edge code")
    case "Safari":
        print("Execute the Safari code")
    case _ : # default
        print("Browser not found")

