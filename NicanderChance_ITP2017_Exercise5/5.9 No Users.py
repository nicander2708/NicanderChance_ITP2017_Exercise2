list =[]
if list:
    for x in list:
        if x == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello '+ x +' thank you for loggin in again.')
else:
    print('we need to find some users')
