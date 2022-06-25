# Problem: Write a function called shortest that takes
# as parameter a list L of strings. The function should
# return the shortest string in L.
# Note: This may or may not be the earliest word in the
# dictionary.
# Tests:
# ["grover", "cookie monster", "elmo", "snuffy"] -> "elmo'
# ["dfsdf", "kkghg", "porridge", "", "bear"] -> ""

def shortest( L ):
    champ_index = 0
    i = 1
    while i < len(L):
        if len( L[i] ) < len( L[champ_index] ) :
            champ_index = i # Same as before.
        i = i + 1

    shortest = L[champ_index]
    index_shortest = champ_index
    return shortest, index_shortest

if __name__ == "__main__":
    print(shortest(["grover", "cookie monster", "elmo", "snuffy"]))
    print(shortest(["dfsdf", "kkghg", "porridge", "", "bear"]))
