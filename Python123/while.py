number = 23
running = True
while running:
    guess = int(input('Enter an integar:'))
    if guess == number:
        print('Congratulations,you guessd it .')
        running = False
    elif guess < number:
        print('No,it is a little higher !')
    else:
        print('No,it is a little lower than the number!')
else:
    print('The while loop is over.')
print('done')