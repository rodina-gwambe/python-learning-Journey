first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = f"{first_name.strip()} {last_name.strip()}"

username = f"{first_name[0].lower()}{last_name.lower()}"

bio_message = input("Enter a short bio about yourself: ")
user_bio =bio_message.strip().lower().replace("i am ", "i'm ") 
bio_len = len(bio_message.strip())

print(f"Your full name is: {full_name.title()}")
print(f"Your username is: {username}")
print(f"Your bio is: {user_bio}")
print(f"Your bio is {bio_len} characters long.")
