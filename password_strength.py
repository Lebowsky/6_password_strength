import getpass
import re


def get_password_strength(password):
    password_strength = 0

    min_length = 6
    middle_length = 10
    has_lowercase = re.search(r'[a-z]', password)
    has_uppercase = re.search(r'[A-Z]', password)
    has_numbers = re.search(r'\d', password)
    has_symbols = re.search(r'[!@#$%^&*()_+]', password)
    has_date = re.search(r'\d{2,4}[.-]\d{2}[.-]\d{2,4}', password)
    has_phone_number = re.search(r'[7-8]\d{10}', password)

    if len(password) >= min_length:
        password_strength += 1

    if len(password) >= middle_length:
        password_strength += 1

    if has_lowercase and has_uppercase:
        password_strength += 1

    if has_numbers:
        password_strength += 1

    if has_symbols:
        password_strength += 2

    if not has_date:
        password_strength += 2

    if not has_phone_number:
        password_strength += 2

    return password_strength


if __name__ == '__main__':
    password = getpass.getpass()
    print('Your password strength is: ',
          get_password_strength(password))
