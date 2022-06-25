#A recursive function that replaces every appearance
# of the letter "a" with the symbol "@"

def replace (S):
    if len(S) == 0:
        return S
    elif S.endswith("a"):
        return replace(S[0:-1]) + "@"
    else:
        return replace(S[0:-1]) + S[-1]

if __name__ == "__main__":
    print(replace("smart")) #sm@rt
print (replace("Peeta"))    #Peet@
print (replace("Python"))   #Python