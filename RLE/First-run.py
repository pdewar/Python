#Probelm 2(a)
#Author: Dewar P.

def find_run(S):
    i = 0
    p = 0
    while i < len(S):
        if S[0] == S[i]:
            p = p+1
        else:
            p = p
        i = i +1
    return p
    
if __name__ == "__main__":
    print(find_run("00001"))
    print(find_run("11111"))
    print(find_run("01111"))
    print(find_run("1"))