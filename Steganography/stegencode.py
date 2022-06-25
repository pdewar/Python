#Purpose: Encode a steganographically coded image
#Author: Dewar P.

from PIL import Image

def hide_num(pixel, X):

    r1,g1,b1 = pixel
    
    dig1 = X//100%100

    dig2 = X//10%10

    dig3 = X//1%10
    
    r = ((r1//10)*10) + dig1
    
    g = ((g1//10)*10) + dig2
    
    b = ((b1//10)*10) + dig3
    
    # if r>225:
    #     r=r-10
    # if g>225:
    #     g=g-10
    # if b>225:
    #     b=b-10
    
    return (r,g,b)

def hide_char(C):
    X = ord(C)
    return X

def encode(original_pic, message):
    N = len(message)
    
    piclist = list(original_pic.getdata())
    
    i = 0
    
    while i < N:
        pix = piclist[i]
        
        letter = message[i]
        
        ascii = hide_char(letter)
        
        newpix = hide_num(pix, ascii)
        
        piclist[i] = newpix

        original_pic.putdata(piclist)
        
        i = i+1
        
    return original_pic

###Your functions should be written above this line
###Don't modify any of the code below
def main():
    thepic = Image.open(input("Image file name: "))
    message = input("\nMessage to hide? ")
    newpic = encode(thepic, message)
    newpic.save("encoded.png")
    print("\nN =", len(message))
    print("\nSaved in encoded.png")
    return

###
main()
