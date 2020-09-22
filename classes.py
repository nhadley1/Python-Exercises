#importing the Planet class from the space package.
from space.planet import Planet
#importing methods from the calc module. (Not a class!)
from space.calc import planet_mass, planet_vol

naboo = Planet('naboo', 300000, 8, 'Naboo System')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(naboo.spin('A very high speed'))
print(f'Name: {naboo.name}')

print(f'{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}')




