# 1.

# Write a function called median that takes a list as an input and returns the median value of the list. For example: median([1, 1, 2]) should return 1.

#     The list can be of any size and the numbers are not guaranteed to be in any particular order. Make sure to sort it!
#     If the list contains an even number of elements, your function should return the average of the middle two.

def median(sequence):
    # Sort the sequence
    sorted_sequence = sorted(sequence)
    
    # Save the length of the sequence
    sequence_length = len(sequence)
    # if the sequence length is even
    if sequence_length % 2 == 0:
        # get the left index
        leftIndex = int((sequence_length / 2) - 1)

        # get the right index
        rightIndex = int(sequence_length - ((sequence_length / 2)))

        # find the difference
        difference = sorted_sequence[rightIndex] - sorted_sequence[leftIndex]

        # add the difference to the left index
        return sorted_sequence[leftIndex] + (difference / 2)
    else:
        oddIndex = int((sequence_length - 1) / 2)
        return sorted_sequence[oddIndex] 

# print(median([7, 3, 1, 4]))
# print(median([7, 3, 1, 4, 9]))
print(median([4, 5, 5, 4]))
print(median([1, 34, 1, 6, 8, 0]))