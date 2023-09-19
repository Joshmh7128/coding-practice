# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

input = [3, 4, 5, 7, -1, 1, 2, 3, 6, 10]

# print out list
print(input)

# loop through the array, and for each instance check if it has the index +1
lowest = 1000 # this is our lowest number
for i in range(len(input)):
    if input[i] +1 not in input:
        if (input[i]+1 < lowest) & (input[i]+1 > 0):
            lowest = input[i] +1

print(lowest)
