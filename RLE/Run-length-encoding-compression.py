#Problem 2(c)
#Author: Dewar P.

def rle_compress(data):
    data = data + "."
    run_length = 0
    i = 1
    run_start = 0
    newlist = ''
    while i < len(data):
        if data[i] != data[i-1]:
            run_length = (i-1) - (run_start) + 1
            run_char = data[i-1]
            if run_length > 3: 
                newlist = newlist + "*" + str(run_length) + str(run_char)
            elif run_length <= 3:
                newlist = newlist + str(data[i-1])* run_length
            else:
                newlist = newlist + str(data[i-1])
            run_start = i
        
            
        i = i+1
        
    return newlist

if __name__ == "__main__":        
    print(rle_compress("11110011110000"))
    print(rle_compress("00"))
