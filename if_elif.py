age = int(input('Enter your age: '))

if age < 10:
    print('You are young')
elif age > 40:
    print('You are old')
else:
    print('You are cool')

meaty = input('Do you eat meat? (y/n): ')

if meaty == 'y':
    print('here is the meaty menu...')
elif meaty == 'n':
    print('here is the veggie menu...')
else:
    print('invalid input')