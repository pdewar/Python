# Write a function called simple that takes as parameter
# a list L of numbers. An entry in L is inverted if it
# is smaller than the entry before it. The function
# should count and return how many entries are inverted.
# Test 1:
# [2, 5, 6, 4, 8, 1, 9] --> 2
# Test 2:
# [1, 2, 3, 4, 5, 6, 7, 8] --> 0
# The position of an entry matters (we care about what
# appears BEFORE the entry) ===› use a WHILE loop)

def simple(L):
    count = 0 # Don't start at 0 for this problem
    i = 1
    while i < len(L):
        # Each entry is: L[i]
        # The entry BEFORE it is L[i-1]
        if L[i] < L[i-1]:
            count = count + 1

        i = i + 1

    return count

if __name__ == "__main__":
    print(simple([2, 5, 6, 4, 8, 1, 9]))
    print(simple([1, 2, 3, 4, 5, 6, 7, 8]))