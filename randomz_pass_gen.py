import random
import string

def generate_password(length):
    """
    Generate a password of a given length.

    The password will contain a mix of uppercase and lowercase letters, digits, and special characters.

    :param length: The length of the password to generate.
    :return: A randomly generated password of the specified length.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """
    Main entry point for the password generator script.
    """
    # Define the length of the password to generate
    password_length = 12

    # Generate the password
    password = generate_password(password_length)

    # Print the generated password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()