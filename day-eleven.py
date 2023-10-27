## Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

## For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

## the words we are completing
autowords = ["aadvark", "abdominal", "active", "banana", "basic", "cat", "clock", "cthonic"]

## get our input
input = input()

## the suggestions for what we might want to use
suggestions = []
s = 0 ## counter for our suggestions

## compare our input to out autowords
for i in range(len(autowords)):
    ## for every character in our input check that many characters of each element, are they the same?
    keep = True
    for z in range(len(input)):
        ## if all characters are the same as we cycle through, we're good
        if input[z] != autowords[i][z]:
            keep = False
    ## if we found no mis-matches, keep this word for the print
    if keep == True:
        suggestions.append(autowords[i]) 
        s += 1

## once we have all the words we want to print, return what we have found
print(suggestions)

## end the program
quit()