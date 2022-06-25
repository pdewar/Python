#Problem 2(b)
#Author Dewar P.

from PIL import Image

def reflect(imgfile):
    img = Image.open(imgfile)
    grid = img.load()

    size = img.size
    width = size[0]
    height = size[1]

    newimg = Image.new( "RGB", (width,2*height))
    newgrid = newimg.load()

    for x in range(width):
        for y in range(height):
            factor = float(y)/360
            newgrid[x,y] = grid[x,y]
            r,g,b,k = grid[x,y]
            grid[x,y] = int(r*factor), int(g*factor), int(b*factor), int(k*factor)
            newgrid[x, (height-y) + height - 1] = grid[x,y]
            
    newimg.show()

    return 

if __name__=="__main__":   
    reflect("castle.png")
    