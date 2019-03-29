number = 23
guess = int(input('please enter an interger:' ))
if guess == number:
    print('Congrtulastions,you guessed it!\nBut you have no prizes!')
elif guess < number:
    print('No,it is a little higher than your guess!')
else:
    print('No,it is a little lower than that!')
print('Finish!')