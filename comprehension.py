#List comprehension makes code shorter.

prizes = [5, 10, 50, 100, 1000]

dbl_prizes = []

#regular for loop.
for prize in prizes:
    dbl_prizes.append(prize*2)
print(dbl_prizes)

# comprehension method.
dbl_prizes = [prize*2 for prize in prizes]
print(dbl_prizes)

#squaring numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sq_even_nums = []

for num in nums:
    if(num**2) % 2 == 0:
        sq_even_nums.append(num**2)

print(sq_even_nums)

#comprehension squaring evens.
sq_even_nums = [num ** 2 for num in nums if (num**2) % 2 == 0]
print(sq_even_nums)