#email slicer

email = input ('Enter your email: ')

index = email.index('@')

username = email[:email.index("@")] #display email
domain = email[email.index("@") + 1:] #display domain without @

print(f'Your username is {username} and domain is {domain}')