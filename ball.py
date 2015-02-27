#This is the ball class for pinball
#Jonathan Harris
#February 27, 2015

import graphics
from time import sleep

class PinBall:
    def __init__(self, color, window):
        self.color = color
        self.window = window


        """This draws the ball on to the screen"""

    def drawBall(self):
        self.point = graphics.Point(self.window.getWidth()/2,self.window.getHeight()/2)
        self.ball = graphics.Circle(self.point, 50)
        self.ball.setFill(self.color)
        self.ball.draw(self.window)

    def moveBall(self):
        while  not self.detectColl():
            self.ball.move(.02,1)
            sleep(.01)

    def detectColl(self):
        self.hit = False
        '''if (self.ball.getRadius() > self.point - self.window.getWidth()) \
         or (self.ball.getRadius() > self.point - self.window.getHeight()):
            self.hit = True
            return self.hit'''
        return self.hit









def main():
    window = graphics.GraphWin("Test Field", 1280, 720)
    window.setBackground('black')
    testball = PinBall('white', window)
    testball.drawBall()
    window.getMouse()
    testball.moveBall()
    window.close()



main()
