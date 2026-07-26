#Basic if/else statements

age = int(input("Enter your age: "))
section_passed = input("Do you have VIP ticket? (yes/no): ").strip().lower()

if age >= 18 and section_passed == "yes":
    print("ACCESS GRANTED to VIP section!!!!!")
elif age >= 18 and section_passed == "no":
    print("ACCESS GRANTED to general section!!!!!")
else: 
    print("ACCESS DENIED!!!!!")