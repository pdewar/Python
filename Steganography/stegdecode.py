#Purpose: Decode a steganographically coded image
#Author: Dewar P.

from PIL import Image

def hidden_num(pixel):
    
    r,g,b = pixel
    
    lsdr = r%10 *100
    lsdg = g%10 *10
    lsdb = b%10 *1
    
    return(lsdr+lsdg+lsdb)
    
def hidden_char(X):
    return(chr(X))
    
def decode(original_pic, N):
    piclist = original_pic.getdata()
    i = 0 
    letter = ''
    message = ''
    
    while i < N:
        num = hidden_num(piclist[i])
        letter = hidden_char(num)
        message = message + letter

        i = i+1
    return message
##Your functions should be written above this line
##Don't modify any of the code below

def testfunctions():
    sample = [(241, 90, 147), (111 , 51, 31) ]
    if hidden_num(sample[0]) != 107:
        print("Your 'hidden_num' function has an error.")

    if hidden_char(107) != 'k':
        print("Your 'hidden_char' function has an error.")

    class dummy:
        def getdata(self):
            return [(241, 90, 147), (111 , 51, 31) ]

    if decode(dummy(), 2) != 'ko':
        print("Your 'decode' function has an error.")

    return
    
def main():
    print("\n\nTesting your functions.\n\n")
    testfunctions()
    print("\n\nReady to decode.\n\n")
    imgfile = "encoded.png"
    N = 654   # Remeber to set N: given from the decode function
    thepic = Image.open(imgfile)
    print(decode(thepic, N))
    return

###
main()

         
