def gameRanks(dictionary):
    for key,val in dictionary.items():
        print(f'{key} is the #{val} ranked game in the list.')

gameList = {}

while True:
    game = input('Enter game: ')

    rank = input('Enter rank: ')
    gameList[game] = rank

    another = input('Enter another? (y/n): ')

    if another == 'y':
        continue
    else:
        break

gameRanks(gameList)

    

    