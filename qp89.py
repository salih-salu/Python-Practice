# 89. Check a given password is valid or not 
# A valid password must contain 
# -more than 6 characters 
# -at least one uppercase letter 
# -at least one lowercase letter 
# -at least one digit 
# -at least one special character 

import re

ps = input('Enter the password: ')

if (len(ps) > 6
    and re.search(r'[A-Z]', ps)
    and re.search(r'[a-z]', ps)
    and re.search(r'[0-9]', ps)
    and re.search(r'[^A-Za-z0-9]', ps)):

    print('Strong Password')
else:
    print('Invalid Password')