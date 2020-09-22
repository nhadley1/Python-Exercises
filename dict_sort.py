

# Sorts strings by length, prints length, string
def sortLen(dictionary):
    sort_dic = sorted(dictionary.items(), key=lambda key: key[1])
    for i in sort_dic:
        print(i[1], i[0])

#Set up empty dictionary that will be filled with user input.
dic = {}

#Allows user to input string
while True:
    string = input('Enter String: ')

    #Sets string length.
    dic[string] = len(string)

    another = input('Enter another? (y/n): ')

    #Doesn't account for any other string being input,
    #anything other than 'y' will break out of loop.
    if another == 'y':
        continue
    else:
        break

#Print sorted dictionary.
sortLen(dic)