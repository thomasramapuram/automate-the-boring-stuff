import re
passwords = {
    'aAbbC123': True,  # Valid Password
    'aBc123': False,  # Password too short
    'ABCDEFGHI1234': False,  # Does not contain lowercase
    'abcdefghi1234': False,  # Does not contain uppercase
    'aAbBCcDdEe': False,  # Does not contain numbers
    'abcABC12345%!@#': True  # Also a valid Password
}

data = {
    '  abcDef  ': 'abcDef',  # Valid Password
    'aBc123': False,  # Password too short
    'ABCDEFGHI1234': False,  # Does not contain lowercase
    'abcdefghi1234': False,  # Does not contain uppercase
    'aAbBCcDdEe': False,  # Does not contain numbers
    'abcABC12345%!@#': True  # Also a valid Password
}


def is_strong_password(password):
    eight_char = re.compile(r'.{8,}')
    lower_case = re.compile(r'[a-z]')
    upper_case = re.compile(r'[A-Z]')
    numbers = re.compile(r'[0-9]')
    if (
            eight_char.search(password) is None or
            lower_case.search(password) is None or
            upper_case.search(password) is None or
            numbers.search(password) is None
    ):
        return False
    else:
        return True


for (key, value) in passwords.items():
    print('%s\t%s\t%s' % (is_strong_password(key), value, key))

# phoneRegex = re.compile(r'''(
# (\d{3}|\(\d{3}\))?              # area code
# (\s|-|\.)?                      # separator
# \d{3}                           # first 3 digits
# (\s|-|\.)                       # separator
# \d{4}                           # last 4 digits
# (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
# )''', re.VERBOSE)
#
# result = phoneRegex.findall("My Phone number is 415-555-1234 or (123) 234 3456")
# print(result)
#
