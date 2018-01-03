import getpass
import re


def get_check_list():
    check_list = {}

    check_list['min_length'] = 6
    check_list['middle_length'] = 10
    check_list['has_lowercase'] = re.search(r'[a-z]', password)
    check_list['has_uppercase'] = re.search(r'[A-Z]', password)
    check_list['has_numbers'] = re.search(r'\d', password)
    check_list['has_symbols'] = re.search(r'[!@#$%^&*()_+]', password)
    check_list['has_date'] = re.search(r'\d{2,4}[.-]\d{2}[.-]\d{2,4}', password)
    check_list['has_phone_number'] = re.search(r'[7-8]\d{10}', password)
    return check_list


def get_password_strength(password):
    password_strength = 0

    check_list = get_check_list()

    if len(password) >= check_list['min_length']:
        password_strength += 1

    if len(password) >= check_list['middle_length']:
        password_strength += 1

    if check_list['has_lowercase'] and check_list['has_uppercase']:
        password_strength += 1

    if check_list['has_numbers']:
        password_strength += 1

    if check_list['has_symbols']:
        password_strength += 2

    if not check_list['has_date']:
        password_strength += 2

    if not check_list['has_phone_number']:
        password_strength += 2

    return password_strength


if __name__ == '__main__':
    password = getpass.getpass()
    print('Your password strength is: ',
          get_password_strength(password))
