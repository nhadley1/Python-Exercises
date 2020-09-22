#Function to greet user.
# def greet(name = 'user', time = 'day'):
#     print(f'Good {time} {name}, hope you are well')

# name = input('input your name: ')
# time = input('input time: ')

# if name != '' and time != '':
#     greet(name, time)
# elif name != '':
#     greet(name)
# elif time != '':
#     greet(time)
# else:
#     greet()

#Radius of a circle.
def cirArea(radius):
    print(3.14159 * radius**2)

#Make sure to typecast str to int.
radius = int(input('Radius of circle: '))

#invoke function.
cirArea(radius)
