# 7.Verify using a regular expression whether a string is a valid CNP.
# https://calculatoare.ha-ha.ro/generator_validator_cnp.php

import re


def is_valid_cnp(cnp):
    if not isinstance(cnp, str):
        raise Exception('Input must be a string')

    # i = 1 - person sex
    # i = 2-3 - last 2 digits of birth year
    # i = 4-5 - birth month
    # i = 6-7 - birth day
    # i = 8-9 - county code [1-46] + [51-52]
    # i = 10-11 - unique number
    # i = 12 - control number

    reg = r'[1-9]' + \
        r'(((00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)' + \
            r'((01|03|05|07|08|10|12)(0[1-9]|1[0-9]|2[0-9]|3[0-1])' + '|' + \
                r'(04|06|09|11)(0[1-9]|1[0-9]|2[0-9]|30)' + '|' + \
                r'(02(0[1-9]|2[0-9]))))' + '|' + \
        r'([0-9][0-9]'+ \
            r'((01|03|05|07|08|10|12)(0[1-9]|1[0-9]|2[0-9]|3[0-1])' + '|' + \
                r'(04|06|09|11)(0[1-9]|1[0-9]|2[0-9]|30)' + '|' + \
                r'(02(0[1-9]|2[0-8])))))' + \
        r'(0[1-9]|[1-3][0-9]|4[1-6]|51|52)' + \
        r'\d{4}'

    return re.fullmatch(reg, cnp) is not None

try:
    print(is_valid_cnp('5080229085324'))
except Exception as e:
    print(e)