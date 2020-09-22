# for n in range(5):
#     #do something
#     print(n)

#Step by 4 from 3..20.
for n in range(3, 20, 4):
    print(n)

pizzas = ['cheese', 'chicken', 'supreme', 'veggie']

# #prints pizza index and name.
# for n in range(len(pizzas)):
#     print(n, pizzas[n])

print('\n')

for n in range(len(pizzas)-1, -1, -1):
    print(n, pizzas[n])