current_users =['Eric','Jones','Mark','Joseph','Arnold']
new_users =['James','Jones','Donald','Joseph','Mason']

current_users_lower = [user.lower()for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('you have to enter a new user name')
    else:
        print('great! your username is elligible!')

