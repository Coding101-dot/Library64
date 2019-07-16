def phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
            if text[7] != '-':
                return False
            for i in range(8, 11):
                if not text[i].isdecimal():
                    return False
                return True


message = 'Call me tomorrow at 052-988-1544,office number is 666-666-6666 khbshcbhkhgwe 041-832-6432'

for i in range(len(message)):
    chunk = message[i:i + 12]
    if phone_number(chunk):
        print('Found following phone number ' + chunk)
        print('Done')


print('012-664-1544 is a phone number')
print(phone_number('982-774-1342'))
print('Hello world is a phone number')
print(phone_number('Hello world'))
