import re


def phonenumreg():
    regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    print(regex.findall('My number is 073-689-1544, and other numbers include 406-323-8417, 333-777-69696'))


phonenumreg()

