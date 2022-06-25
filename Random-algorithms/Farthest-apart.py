# Write a function called farthest that takes as parameter a list
# L. The function should return a pair of numbers that are the
# farthest apart (that is, the difference between the numbers
# is maximum.

# Tests
# farthest([23, 16, 3, 24, 78, 9, 6]) --> (3, 78)
# farthest([94, 120, 118, 65, 142, 37, 188]) --> (37, 188)

def farthest(L):
    winning_diff = 0
    winning_pair = ()

    i = 0
    while i < len(L): # Outer loop
    # First item of pair: L[i]

        j = 0
        while j < len(L):
            # Second item of pair: L[j]
            difference = abs(L[i] - L[j])
            if difference > winning_diff:
                winning_pair = (L[i], L[j])
                winning_diff = difference

            j = j + 1 # Check the indents
        i = i + 1     # Check the indents

    return winning_pair

if __name__ == "__main__":
    print(farthest([23, 16, 3, 24, 78, 9, 6]))
    print(farthest([94, 120, 118, 65, 142, 37, 188]))