#Problem 1
#Author: Dewar p.

def printfile():
    myfile = open("student_names.txt")
    i = 0
    for line in myfile:
        print(i,line)
        i = i+1
    myfile.close()
    return
                    
if __name__=="__main__":
    printfile()