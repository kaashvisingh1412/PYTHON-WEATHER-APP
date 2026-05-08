# basic_password_generator.py

import random
import string

print("===== Password Generator & Strength Checker =====\n")

while True:
    choice = input("Generate a password? (yes/no): ").lower()
    if choice == "no":
        print("Goodbye! Stay safe!")
        break
    elif choice != "yes":
        print("Please type 'yes' or 'no'.\n")
        continue

    length = input("Enter password length (4 or more): ")
    if not length.isdigit() or int(length) < 4:
        print("Invalid input. Try again.\n")
        continue
    length = int(length)

    # Simple character pool: letters + digits
    chars = string.ascii_letters + string.digits

    # Generate password
    password = ""
    for i in range(length):
        password += random.choice(chars)

    print("\nGenerated Password:", password)

    # Basic strength check
    if any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
        if length >= 8:
            strength = "Strong"
        else:
            strength = "Moderate"
    else:
        strength = "Weak"

    print("Password Strength:", strength, "\n")
