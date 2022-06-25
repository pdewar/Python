def reverse(S):
    # Base case: if S has 1 or 0 character
    if len(S) == 0:
        return S
    
    #reverse(S) = S[-1] + reverse(S[0:-1])

    return S[-1] + reverse(S[0: -1])

if __name__ == "__main__":
    print(reverse("hofstra")) #artsfoh
    print (reverse("Universal")) #lasrevinU