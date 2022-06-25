# Problem: Given a list L of items in sorted order,
# and a specific item 
# X, determine if X is in L. If X is in L, what is
# its index (position) in L?

# Sample inputs, outputs
# Test 1:
# L = [0, 1, 8, 12, 15 ,19 26, 81]
# X = 19 
# Result = 5
# Strategy: Use the bisection method
# We "guess" the index of X as the midpoint
# of the list.
# (1) The guess is good. That is, X is exactly
#     where we guested it would be. Woo hoo! Done.
# (2) The guess is not as good because the # we found
#     is smaller than X.
# (3) The guess is not good because the # we found 
#     is bigger than X.

def binaarysearch(L, X):

    minindex = 0
    maxindex = len(L)- 1

    while minindex <= minindex:
        # What is the part of the list we're
        # examining
        print("L =", L[minindex:maxindex+1])

        guess = (minindex + maxindex)//2

        print("guess =", guess)
        print("L[guess] = ", L[guess])

        if X == L[guess]: # Is it a match???
            return guess  # End of story!
        elif X > L[guess]:
            minindex = guess + 1
        else:
            maxindex = guess - 1

    return -1

if __name__ == "__main__":
    L = [0,1,8,12,15,19,26,81]
    X = 19

    result =  binaarysearch(L, X)
    print("Result =", result)