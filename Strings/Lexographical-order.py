# Write a function called 'earlier' that takes two strings N1 and N2 as
# parameters. The function should return the string that is lexicographically
# earlier (appears earlier in the dictionary). Case should be ignored.
# Test cases:
# 1) earlier("dog", "cat") --> "cats"
# 2) earlier("pillaipakkamnatt", "Zavou") --> "pillaipakkamnatt"
# 3) earlier("zebra", "Lion") --> "Lion'

#Solution
# AVOID PRINT (use return instead)
# AVOID INPUT (use params instead)

def earlier (N1, N2):
    """This function will return one of N1 or N2, whichever is
    lexicographically earlier."""

    if N1.lower() > N2.lower(): #Compare the lowercase versions of N1, N2
                                # N1 and N2 themselves remain as they are!
        return N2
    else:
        return N1

if __name__ == "__main__":
    print(earlier("dog", "cat"))
    print(earlier("pillaipakkamnatt", "Zavou"))
    print(earlier("zebra", "Lion"))