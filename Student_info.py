first_Name = input("Enter your First Name: ")
surname = input("Enter your Surname: ")
age_in_months =int(input("Enter your Age: "))*12
favourite_number =round(float(input("Enter your Favourite Number: ")), 2)
print(f"Welcome, {first_Name.upper()} {surname.upper()}!")
print(f"Welcome, {first_Name.title()} {surname.title()}!")
print(f"Your Age in Months is: {age_in_months} months")
print(f"Your Favourite Number is: {favourite_number}") 

print(f"first name is {type(first_Name)}")
print(f"surname is {type(surname)}")
print(f"age is {type(age_in_months)}")
print(f"favourite number is {type(favourite_number)}")
