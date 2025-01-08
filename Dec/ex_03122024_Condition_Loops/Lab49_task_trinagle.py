# tringle Classififier ----> based on input find the type of tringle

S1 = int(input("Enter the first side value"))
S2 = int(input("Enter the second side value"))
S3 = int(input("Enter the third side value"))

if S1==S2==S3:
    print("the triangle is equilateral")
elif S1==S2 or S1==S3 or S2==S3:
    print("the triangle is isolance")
elif S1!=S2!=S3:
    print("the triangle is solance")
else:
    print("it's not a trianle")





