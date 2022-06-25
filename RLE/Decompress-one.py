#Problem 1(a)
#Author: Dewar P.

def decompress_one(S):

    if S.startswith("*"):
        i = 0
        n = ''
        while i < int(S[1]):
            n = n + (S[2])
            i = i+1
        return n
    else:
        return S[0]

if __name__ == "__main__":
    print(decompress_one("*50"))
    print(decompress_one("100"))
    print(decompress_one("0"))
    print(decompress_one("*410"))