password = input("Enter your password: ")
password_hint = f"Your password hint: It starts with {password.strip()[0].upper()} and ends with {password.strip()[-1].upper()}"
print(password_hint)