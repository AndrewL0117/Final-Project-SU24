# -*- coding: utf-8 -*-

import random
import string

def generate_password(length=12, include_digits=True, digits_min=2, include_special_chars=True, special_chars_min=1):
    """Generate a random password."""
    chars = string.ascii_letters  # Letters
    if include_digits:
        chars += string.digits  # Add digits
    if include_special_chars:
        chars += string.punctuation  # Add special characters

    # Ensure password has min. required numbers and special characters
    password = ''
    if include_digits:
        password += ''.join(random.choice(string.digits) for _ in range(digits_min))
    if include_special_chars:
        password += ''.join(random.choice(string.punctuation) for _ in range(special_chars_min))
    
    # Add remaining characters to meet the length requirement
    remaining_length = length - len(password)
    password += ''.join(random.choice(chars) for _ in range(remaining_length))

    # Shuffle the password characters to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def main():
    print("Password Generator")

    # Get password length
    while True:
        try:
            length = int(input("Enter the length of the password (at least 6 characters): "))
            if length < 6:
                print("Password length should be at least 6 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Digits and minimum number of digits
    include_digits = input("Include digits (0-9)? (yes/no or y/n): ").lower() in ['yes', 'y']
    digits_min = 0
    if include_digits:
        while True:
            try:
                digits_min = int(input("Enter minimum number of digits in the password: "))
                break
            except ValueError:
                print("Please enter a valid integer.")

    # Special characters and minimum number of special characters
    include_special_chars = input("Include special characters (!@#$% etc.)? (yes/no or y/n): ").lower() in ['yes', 'y']
    special_chars_min = 0
    if include_special_chars:
        while True:
            try:
                special_chars_min = int(input("Enter minimum number of special characters in the password: "))
                break
            except ValueError:
                print("Please enter a valid integer.")

    # Password length check
    total_min = digits_min + special_chars_min
    if total_min > length:
        print("Error: The sum of minimum digits and minimum special characters exceeds the password length. Please extend the password length.")
        return

    # Generation
    password = generate_password(length, include_digits, digits_min, include_special_chars, special_chars_min)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
    