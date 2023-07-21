# the list of numbers we enter
startnum = [10,15,3,7,32]
# the number we're checking against
k = 39
# have we found our answer?
found = False
# loop through our startnums and add the current index to the next index
for i in range(len(startnum)-1):
    if startnum[i] + startnum[i+1] == k:
        found = True

print(found)

