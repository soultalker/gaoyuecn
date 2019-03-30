def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)
something = input('Enter text: ')

for i in range(len(something)):
    if something[i] in (' ','.')
    del something[i]

if is_palindrome(something):
    print('YES,This is a palindrome')
else:
    print('No,it is not a palindrome')