# You have the following list of names:
# ["Zoe", "Adam", "Lionel", "Abby", "Percy", "Sir Topham Hatt"]
# Sèlectively print out only those nanes that' begin with the letter "A"

#DON'T: Find the names that begin with "A" by yourself! Let Python do it
#for you.

def A_names() :
    names = ["Zoe", "Adam", "Lionel", "Thomas", "Abby", "Percy", "Sir Topham Hatt"]
    for X in names:
        if X.startswith("A"):
            print(X, "begins with A")

    print("All done!")
    return

if __name__ == "__main__":
    A_names()
