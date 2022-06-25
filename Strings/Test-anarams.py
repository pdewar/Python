""" Problem: Write a function called anagams that takes 
as paragrams two strings  S1 and S2. The function should
return True if S1 is an anagrams (rearrangement of letters)
of S2, and False otherwise.
Note: No letter characters (punctuation, spaces, etc.) can
be ignored. Also, there is no difference between upper and
lowercase letters.


#Test cases:
# anagrams ("Dormitory", "dirty room"') --> True
# anagrams ("Presbyterians", "Britney Spears") --> True
anagrams("Krish", "Elvis") --> False
""" 

def clarify(str):
    res = ""
    for ch in str:
        if ch.isalpha():
            res += ch
    return res

def anagrams(S1,S2): 
    """Reuturns True if S1 is an anagram of S2, False otherwise."""
    #First, turn S1 and S2 into lowercase letters
    S1 = S1.lower()
    S2 = S2.lower()
    S1 = clarify(S1) #This will only retain the letters of S1
    S2 = clarify(S2) #Letters only
    if sorted(S1) == sorted(S2) :
        return True
    else:
        return False

if __name__ == "__main__":
    print( anagrams ("Dormitory", "dirty room"))
    print( anagrams ("Presbyterians", "Britney Spears"))
    print( anagrams ("Krish", "Elvis"))