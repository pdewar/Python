# Write a function called perfectpair that takes as
# parameter a list L. The function should return
# two numbers in the list that add up to 100. If
# no such pair exists, it should return the special
# value None

#Tests
# perfectpair([12, 24, 36, 49, 60, 64, 77, 89, 90]) --> (36, 64) 
# perfectpair([1, 99, 2, 98]) --> (2, 98) or (1, 99)
# perfectpair([1, 2, 3, 55, 56, 57]) --> None

def perfectpair(L):
    # To work with pairs of items from a list, used nested loops
    i = 0
    while i < len(L):
        # L[i] is one item in the pair

        j = 0
        while j < len(L): 
            # L[j] is the second item in the pair
            # You can use L[i] and L[j] to solve your problem
            if i != j and L[i] + L[j] == 100:
                return L[i], L[j]
            
            j = j + 1 # Watch out for the indents!!

        i = i + 1 # Watch out for the indents!!
    
    return None # This will happen if I don't find a perfectpair

if __name__ == "__main__":
    print(perfectpair([12, 24, 36, 60, 64, 77, 89, 90]))
    print(perfectpair([1, 99, 2, 98]))
    print(perfectpair([1, 2, 3, 55, 56, 57]))