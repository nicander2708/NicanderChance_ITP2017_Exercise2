a = input('Enter the word:')
a = a.lower()
rev_a = reversed(a)
if list(a) == list(rev_a):
    print('It is a palindrome')
else:
    print('It is not a palindrome')
