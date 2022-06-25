# Problem: Define a function called min max that takes
# as paramerer as list L of #s. It should return both
# the smallest and the largest value in L.

# Idea: Have two champions: One for the "small" fights,
# the other for the big fights

def min_max(L):
    champ_small = 0
    champ_big = 0

    i = 0
    while i < len(L):
        # The small fight
        if L[i] < L[champ_small]:
            champ_small = i
        
        if L[i] > L[champ_big]:
            champ_big = i
    
        i = i + 1

    return L[champ_small], L[champ_big]

if __name__ == "__main__":
    print(min_max([24, 34, 12, -3, 8, 2, -5, 21]))