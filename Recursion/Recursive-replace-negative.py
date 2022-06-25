# Write a function called smooth that takes as parameter
# a list L of numbers. The fumction should return a new list
# that has the same numbers as in L, except that all
# negative numbers in L should be replaced by 0.

# test cases
# smooth([3, -5, 2, 1]) --> [3,0,2,1]
# smooth([4, 3, 2, 1, 0, -1]) --> [4, 3, 2, 1, 0, 0])
# smooth ([1, 3, 5, 7, 9]) --> [1, 3, 5, 7, 9]

def smooth(L):
    # base case
    if len(L) == 0:
        return [ ]
    elif L[-1] < 0:
        LL = smooth(L[0: -1])
        LL.append(0)
        return LL
    else:
        return smooth(L[0:-1]) + [L[-1]]

if __name__ == "__main__":
    print (smooth([3, -5, 2, 1]))
    print (smooth([4, 3, 2, 1, 0, -1]))
    print (smooth ([1, 3, 5, 7, 9]))