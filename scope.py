#global
my_name = 'Nate'

def print_name():
    #global
    global my_name
    
    #local
    my_name = 'Yoshi'
    
    print('The name inside the function is', my_name)

print_name()

print('Outside the function the name is', my_name)