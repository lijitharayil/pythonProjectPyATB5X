# for i in range(1,10):
#     if i == 5:
#         print("five")
#         break;
#     else:
#         print(i)

    # i  | conditions | o/p
    # 1  | 1==5   | o/p = false, print 1
    # 2  | 2==5   | o/p = false, print 2
    # 3  | 3==5   | o/p = false, print 3
    # 4  | 4==5   | o/p = false, print 4
    # 5  | 5==5   | o/p = True, print Five


#
# for i in range (1,10,1):
#     if i==6:
#         print(i)
#     else:
#         print("No O/p")
#     # i  | conditions | o/p
    # 1  | 1==6   | o/p = false, print No O/p
    # 2  | 2==5   | o/p = false, print No O/p
    # 3  | 3==5   | o/p = false, print No O/p
    # 4  | 4==5   | o/p = false, print No O/p
    # 5  | 5==5   | o/p = True, print No O/p
    #  6 | 6==5   | o/p = True, print 6 No O/p
   #  10 | 10==5   | o/p = false, Exit


for i in range(1,10,1):
    if i==5 or i==6:
        print(i)
    else:
        print("Pass")



for i in range(1,10,1):
    if i==5 or i==6:
        print(i)
    else:
        pass
    
