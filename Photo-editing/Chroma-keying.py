#Problem 1
#Author Dewar P.

from PIL import Image

def chromakey(grid1, grid2):
    im1 = Image.open(grid1)
    im2 = Image.open(grid2)
    
    backpix = list( im1.getdata() )
    
    forepix = list( im2.getdata() )
    
    i = 0
    
    while i<len(forepix):
        
        R,G,B = forepix[i]
        
        if G > (R+B) and G > 50:
            forepix[i] = backpix[i]
            
        i = i+1
        
    im2.putdata( forepix )
        
    im2.show()
        
    return im2

if __name__=="__main__":
    chromakey("background.png", "foreground.png")
