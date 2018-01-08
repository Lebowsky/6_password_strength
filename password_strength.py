import getpass
import re


def get_check_list(password):
    check_list = {}
    min_length = 6
    great_length = 10

    check_list['min_length'] = len(password) >= 6
    check_list['great_length'] = len(password) >= 10
    check_list['has_lowercase'] = bool(re.search(r'[a-z]', password))
    check_list['has_uppercase'] = bool(re.search(r'[A-Z]', password))
    check_list['has_numbers'] = bool(re.search(r'\d', password))
    check_list['has_symbols'] = bool(re.search(r'[!@#$%^&*()_+]', password))
    check_list['has_date'] = not(re.search(r'\d{2,4}[.-]\d{2}[.-]\d{2,4}', password))
    check_list['has_phone_number'] = not(re.search(r'[7-8]\d{10}', password))
    return check_list


def get_password_strength(password):
    password_strength = 0

    check_list = get_check_list(password)

    for key, value in check_list.items():
        if value:
            password_strength += 1
            if key == 'great_length' or key == 'has_symbols' :
                password_strength += 1

    return password_strength


if __name__ == '__main__':
    password = getpass.getpass()
    print('Your password strength is: ',
          get_password_strength(password))
