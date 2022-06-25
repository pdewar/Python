# Given a list L of nanmes ... no has
# the letter "X" somewhere in their name. Assume
# that all names are an uppercase.

# Test 1:
# ["JOE", "DAVE", "STEVE", "DORA", "MAX", "RUBY"]
# Return: 4

# Test 2:
# ["ABE", "ALICE", "ANDI", "ALAN"]
# Return: -1

def namesearch(L):
    """Find a name in L that has the letter X in it."""

    # Strategy: Linear search
    # Go through each name in L until you either
    # (a) find a name wit "X" in L, or
    # (b) you run out of items in L

    i = 0
    # Write the second condition to involve the
    # item L[i]
    # while ¡ < len(L) and L[i] != X:
    while i < len(L) and "X" not in L[i]:
        
        i = i + 1

    if i < len(L):
        return i
    else:
        return -1

if __name__ == "__main__":
    L = ["JOE", "DAVE", "STEVE", "DORA", "MAX", "RUBY"]
    result1 = namesearch(L)
    print ("Result1 =", result1)

    L = ["ABE", "ALICE", "ANDI", "ALAN"]
    result2 = namesearch(L)
    print ("Result2 =", result2)