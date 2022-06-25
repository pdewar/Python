#Problem 1 Program that draws a bullseye
#Peter D.

from graphics import GraphWin, Point, Circle, Text

def One():
    #Create the windows and set up coordinate system
    win = GraphWin("Bullseye", 500, 500)
    win.setCoords(0,0,500,500)

    for x in range(100,200,30):
        center = Point(250, 250)  #This is the middle of the screen
        C = Circle(center, x)     
        C.setOutline("red")
        C.setWidth(15)
        C.draw(win)
    
    #Wait for user to click in the windows, then close the window
    T = Text(Point(250, 100), "Click inside the windows th close")
    T.draw(win)
    win.getMouse()
    win.close()
    return

###
One()
