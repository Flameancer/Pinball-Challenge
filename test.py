#Test file
#Jonathan Harris
#February 27, 2015

import graphics

def main():
    win = graphics.GraphWin("test", 1024, 720)
    win.setBackground("black")
    c = graphics.Circle(graphics.Point(512,360),50)
    c.setFill("white")
    c.draw(win)
    print c.getCenter()
    win.getMouse()
    win.close()


main()
