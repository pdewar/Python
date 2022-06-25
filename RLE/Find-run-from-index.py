#Problem 2(b)
#Author: Dewar P.

def find_run_gen(S, i):
    m = 0
    p = 0
    if len(S[i:-1]) == 0:
        p = p+1
        return p 
    while m < len(S[i:-1])+1:
        if S[i] == S[i+m]:
            p = p+1
        else:
            p = p
        m = m+1
    return p
    
if __name__ == "__main__":
    print(find_run_gen("00001",1))
    print(find_run_gen("1110000",3))
    print(find_run_gen("00001",4))
    print(find_run_gen("00001",0))