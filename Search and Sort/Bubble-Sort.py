# Bubble Sort:
# Idea: Find neighboring items in the list that are
# "out of whack" ane swap then

def bubblesort(L):

    N = len(L)
    for reps in range(N):
        i = 0
        while i < len(L) - 1:
            # L[i] and L[i+1] are neighboring items
            if L[i] > L[i+1]: #"Out of whack"
                #Swap numbers in list
                L[i],L[i+1] = L[i+1], L[1]

            i = i + 1

    return L

if __name__ == "__main__":
    L = [34, 14, 24, 6, 18] 
    print(bubblesort(L))