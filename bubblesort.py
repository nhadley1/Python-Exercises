def bubblesort(nrs):
    #get length of array
    n = len(nrs)
    
    #iterate through array, switching values with adjacent
    # values not in the right place
    for i in range(n-1):
        for j in range(0, n-i-1):
            if nrs[j] > nrs[j+1]:
                nrs[j], nrs[j+1] = nrs[j+1], nrs[j]
    
#array to test with.
nrs = [3, 7, 1, 1, 8, 5]

thisset = set(nrs)

# bubblesort(nrs) 
  
# print ("Sorted array is:") 
# for i in range(len(nrs)): 
#     print ("%d" %nrs[i]),

print(thisset)