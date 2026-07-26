#Adding number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
#print("The sum of {0} and {1} is {2}".format(num1, num2, sum))
print(f"The sum of {num1} and {num2} is {sum}")

#calculating the restaurant tip
bill_amount = float(input("Enter the total bill amount:R "))
tip_percentage = 0.15 #in decimal form 15%
tip_amount = bill_amount * tip_percentage
total_amount = bill_amount + tip_amount

print(f"The tip amount is:R {tip_amount}")
print(f"The tip amount is:R {round(tip_amount,2)} rounded")

print(f"The total Sub amount is:R {bill_amount}")
print(f"The total Sub amount is:R {round(bill_amount,2)} rounded")

print(f"The total bill amount is:R {total_amount}")
print(f"The total bill amount is:R {round(total_amount,2)} rounded")