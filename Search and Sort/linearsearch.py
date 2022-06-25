#problem: Given a list L of items, and a specific item
# X,  determine if x is in L. If X is in L, what is
# its index (position) in L?
#
# sample inputs, outputs
# Test1
# L = [12, 15, 8, 1, 19, 26, 81, 0]
# x = 19
# Return value: 4 [this is index of 19 in L]
# Test 2
# L = [12, 15, 8, 1, 19, 26, 81, 0]
# x = 33
# Return value: -1
# Test 3
# L = ["Ben", "Cher", "Dru", "Franny", "Peppa"]
# X = "Dru"
# Return value: 2

def linsearch(L,X):
    """Looks for X in L. If found, it returns the
    index of the first occurrence of x in L. Otherwise
    it returns -1. """

    # Go, throught each item in the sequence until
    # a) you find the item in L that matches X,
    # b) you run out of items
    
    i = 0
    while i < len(L) and L[i] != X:

        i = i + 1
    
    # If it is a legitimate index (that is a match is found)
    if i < len(L):
        return i # Returns the index where a match is found
    else:
        return -1

if __name__ == "__main__":
    L = [12, 15, 8, 1, 19, 26, 81, 0]
    X = 19
    result1 = linsearch(L, X)
    print("Test 1 output =", result1)

    X2 = 33
    result2 = linsearch(L, X2)
    print("Test 2 output =", result2) #Should be -1

    L2 = ["Ben", "Cher", "Dru", "Franny", "Peppa"]
    X3 = "Dru"
    result3 = linsearch(L2, X3)
    print("Test 3 output =",result3)