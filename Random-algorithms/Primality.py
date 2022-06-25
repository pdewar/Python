# Primality as a filtering problem

def prime(N) :
    """This function returns True is N is prime, otherwise
    returns False."""
    # Idea: Count how many divisors N has.
    # If there are exactly 2 divisors, ==› Prime is true
    # More than 2 divisors ==› Prime is false

    # Filtering part
    count = 0
    for X in range(1, N+1):     # Potential divisors
        if N % X == 0:          # X is a divisor of N
            count = count+1     # Increase the count

    # Filtering is done, now comes the check
    if count == 2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(prime(5))  # This must return True
    print(prime(10)) # This must return False