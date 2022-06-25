# Insertion Sort:
# Idea:
# 1) Maintain a sorted prefix
# 2) Add one new number at a time into the prefix,
#    and move the new number into place so that the
#    prefix remains sorted.

def insertion_sort(L):
    i = 1 # Start at 1 and not at 0 because
          # the prefix that ends at 0 is already sorted

    while i < len(L):
        # L[i]: The item in the list that we want to add
        newguy = L[i]
        j = i # 'j' tracks the position of newguy
        while j >= 0 and L[j-1] > newguy:
            # Need to shift the big # to the right
            L[j] = L[j-1]
            # Move the new guy in place of the big #
            L[j-1] = newguy
            j = j - 1

        i = i + 1

        