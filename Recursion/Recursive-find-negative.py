#The function has_neg takes as parameter a list L
# of numbers. It returns True if L has at least one
# negative number, and False otherwise.

def has_neg(L):
    # Base case? Empty list
    if L == [ ]:
        return False
    elif has_neg(L[0: -1]) == True: # Python's responsibility
        return True
    elif L[-1] < 0: # Is the last number negative?
        return True
    else:
        return False

if __name__ == "__main__":
    print(has_neg([12, 3, -5, 2, 1]))    # True
    print(has_neg([0, 2, 4, 6, 8, -10])) # True
    print(has_neg([2, 3, 5, 7, 11, 13])) # False
