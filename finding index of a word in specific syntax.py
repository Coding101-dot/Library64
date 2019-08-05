music_string = 'doo be doo be doo...'

n = -1
while True:
    n = music_string.find('doo', n + 1)
    if n == -1:
     break
    print(n, end=' ')