import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    """
    Generate a random password based on the specified criteria.
    
    :param length: Length of the password
    :param use_uppercase: Include uppercase letters (bool)
    :param use_lowercase: Include lowercase letters (bool)
    :param use_numbers: Include numbers (bool)
    :param use_special: Include special characters (bool)
    :return: Generated password as a string
    """
    # Define character sets
    uppercase_chars = string.ascii_uppercase if use_uppercase else ""
    lowercase_chars = string.ascii_lowercase if use_lowercase else ""
    number_chars = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special else ""

    # Combine all selected character sets
    all_chars = uppercase_chars + lowercase_chars + number_chars + special_chars

    # Ensure at least one character set is selected
    if not all_chars:
        raise ValueError("At least one character type must be selected.")

    # Ensure the password contains at least one character from each selected set
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase_chars))
    if use_lowercase:
        password.append(random.choice(lowercase_chars))
    if use_numbers:
        password.append(random.choice(number_chars))
    if use_special:
        password.append(random.choice(special_chars))

    # Fill the rest of the password length with random characters
    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(random.choices(all_chars, k=remaining_length))

    # Shuffle the generated password to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

def main():
    print("Welcome to the Password Generator created by Mr. Sabaz Ali Khan!")
    try:
        # Get user input
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        # Generate the password
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        print(f"Your generated password is: {password}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
