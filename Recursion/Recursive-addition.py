# Problem: Write a function called firstsum that takes as parameter a positive
# integer N. The function should compute and return the sum:
# 1 + 2 + 3 + ... + N
# Test cases
# firstsum(3) --> 6
# firstsum(10) --> 55
# firstsum (100) --> 5050

# Use accumulation to solve this problem

# def firstsum(N):
#     # 1, 2, 3, ..., N can be expressed as range(1, N+1)
#     total = 0
#     for X in range(1, N+1):
#         total = total + X
   
#     return total

# Recursive version of firstsum
def firstsum(N):
    # Base case: N = 1
    if N == 1:
        return 1
    else:
        return firstsum(N-1) + N
    # Remember! firstsum(N-1), the smaller problem, will be
    # solved automagically by Python!

if __name__ == "__main__":
    print (firstsum(3))
    print (firstsum(10))
    print (firstsum(100))
