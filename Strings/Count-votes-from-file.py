#Problem 2
#Author: Dewar p.

def addition():
    votes = open("votes.txt")
    count = 0
    for num in votes:
        count = count + int(num)

    print(count)

if __name__=="__main__":
    addition()