# Finding the minimum value in a list (also index of min val)
# Tournament method
# 1. Assume that item at index #0 is smallest value (champ)
# 2. Conduce N-1 fights each involving the current champ
#    and the next item in the list. The winner of each 
#    fight is the champ for the next fight.
# 3. The winner of the last fight is champ overall (smallest)


def listmin( L ):
    """This function returns the smallest value in
    the list L. """
    champ_index = 0
    # Step 1 above
    i = 1
    while i < len(L):
        
        if L[i] < L[champ_index ]:
            champ_index = i 

        i = i + 1

    smallest = L[champ_index]
    index_smallest = champ_index
    return smallest, index_smallest

if __name__ == "__main__":
    print(listmin([124, 34, 12, -3, 8, 2, -5, 21]))
    print(listmin(["crow", "pigeon", "ant", "frog", "ip"]))