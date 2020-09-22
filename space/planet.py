#self is similar to the this keyword in Java
#init function is similar to a Java Constructor.

class Planet:

    #Class level attributes describe qualities that all objects in the class should have.
    shape = 'round'


    def __init__(self, name, radius, gravity, system):
        #instance attributes.
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        #instance methods.
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    #cls for class instead of access to instance like with self.
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity.'

    #does not have access to self or the class - 
    # only has access to parameters that are passed to it individually
    @staticmethod
    def spin(speed = '2000 miles per hour'):
        return f'The planet spins and spins at {speed}'







