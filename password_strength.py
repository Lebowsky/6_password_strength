import getpass
import re
import string


def get_check_list(password):
    min_length = 6
    great_length = 10

    check_list = {
        'min_length'            : len(password) >= min_length,
        'great_length'          : (len(password) >= great_length) * 2,
        'has_lowercase'         : bool(re.search(r'[a-z]', password)),
        'has_uppercase'         : bool(re.search(r'[A-Z]', password)),
        'has_numbers'           : bool(re.search(r'\d', password)),
        'has_symbols'           : bool(re.search(r'[{}]'.format(string.punctuation), password)) * 2,
        'not_has_date'          : not(re.search(r'\d{2,4}[.-]\d{2}[.-]\d{2,4}', password)),
        'not_has_phone_number'  : not(re.search(r'[7-8]\d{10}', password)),
    }

    return check_list


def get_password_strength(password):
    password_strength = 0
    check_list = get_check_list(password)

    for check in check_list.values():
        password_strength += check
    return password_strength


if __name__ == '__main__':
    password = getpass.getpass()
    print('Your password strength is: ',
          get_password_strength(password))
