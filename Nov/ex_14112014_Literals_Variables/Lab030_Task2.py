# #take a 2 input from the users and find Quotient  and reminder

Dividend = int(input("Enter a number"))
Divisor = int(input("Enter the second number"))
# num1 = Dividend
# num2 = Divisor

Quotient = int(Dividend / Divisor)

reminder = int(Dividend -(Divisor * Quotient))

print("Quotient is :",Quotient)
print("reminder is :",reminder)
