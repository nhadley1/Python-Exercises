ninjas = ['ryu', 'crystal', 'yoshi', 'ken']

#naming is arbitrary
# for ninja in ninjas:
#     print(ninja)

#Not inclusive
# for ninja in ninjas[1:3]:
#     print(ninja)

# for ninja in ninjas:
#     if ninja == 'yoshi':
#         print(f'{ninja} - black belt')
#     else:
#         print(ninja)

age = 25
num = 0

#print numbers 1..age
# while num < age:
#     num += 1
#     print(num)

#print even numbers 1..10.
while num < age:
    if num == 0:
        num += 1 
        continue
    if(num % 2 == 0):
        print(num)
    if num > 10:
        break
    num += 1
