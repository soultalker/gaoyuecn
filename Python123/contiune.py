while True:
    s = input('Enter your word here:')
    if s == 'quit':
        break
    if len(s) <= 3:
        print('Too Samll\
              choose another one.')
        continue
    print('Yes,I got your words.')
