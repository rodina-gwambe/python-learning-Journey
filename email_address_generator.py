#Professional email address generator
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
username = (f"{first_name[0].lower()}{last_name.lower()}@company.com")
print(f"Your professional email address is: {username}")