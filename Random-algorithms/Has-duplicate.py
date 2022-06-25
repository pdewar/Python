# Write a function called has_dup that takes as parameter
# list L of items. The function should return True
# if the list has at least one item that is duplicated,
# and False otherwise.

# Tests
# has_dup([1,2,3,4,5]) --> False
# has_dup([1,2,3,1,5]) --> True
# has_dup([1,2,3,2,1]) --> True
# has dup([1) --› False

def has_dup(L):
    """Returns True if L has duplicated entries, False
    otherwise."""
    
    i = 0
    while i < len(L):
        
        j = i + 1
        while j < len(L):
            if L[i] == L[j]: # Found a match!
                return True

            j = j + 1

        i = i + 1

    return False

if __name__ == "__main__":
    print(has_dup([1,2,3,4,5]))
    print(has_dup([1,2,3,1,5]))
    print(has_dup([1,2,3,2,1]))
    print(has_dup([]))