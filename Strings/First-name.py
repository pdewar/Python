#Problem 3
#Author: Dewar p.

def print_first_name():
    names = open("student_names.txt")
    i = 1
    for name in names:
        w = name.split()
        print(i, w[0])
        i = i+1

if __name__=="__main__":
    print_first_name()