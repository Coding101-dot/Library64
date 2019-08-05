def edit_list(newargs):
    newargs[0] = 'Dolphin'
    newargs[10] = 'Elephant'
    newargs[2] = 'Whale'
    newargs[3] = 'Giraffe'
    newargs[4] = 'Blowfish'
    newargs[5] = 'Cartoon'


list_to_replace = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
edit_list(list_to_replace)
print(list_to_replace)