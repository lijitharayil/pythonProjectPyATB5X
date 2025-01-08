for i in range(1,10):
    if i == 5:
        print("five")
    else:
        print(i)

    # i  | conditions | o/p
    # 1  | 1==5   | o/p = false, print 1
    # 2  | 2==5   | o/p = false, print 2
    # 3  | 3==5   | o/p = false, print 3
    # 4  | 4==5   | o/p = false, print 4
    # 5  | 5==5   | o/p = True, print Five
    #  6 | 6==5   | o/p = false, print 6
    #  9 | 9==5   | o/p = false, print 9
    #  10 | 10==5   | o/p = false, Exit
