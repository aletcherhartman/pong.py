import pygame
import math

class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self,x,y,dem,changeX,changeY,direction):
        self.x = x
        self.y = y
        self.dem = dem
        self.changeX = changeX
        self.changeY = changeY
        self.direction = direction

    def setSpeed(self,changeX,changeY):
        if changeX - self.changeX < changeX:
            self.changeX = changeX
        else:
            self.changeX = changeX * -1
        if changeY - self.changeY < changeY:
            self.changeY = changeY
        else:
            self.changeY = changeY * -1

    def buildBall(self,screen,BLACK):

        # Draw a rectangle
    	pygame.draw.circle(screen, BLACK, [self.x, self.y], self.dem)

    	return Ball

    def moveBall(self, size, screen, paddleL, paddleR):

        # Move the ball starting point
        self.x += self.changeX
        self.y += self.changeY

        pos = 1 + abs((paddleL.y-paddleL.demY/2) - self.y)/100
        
        # Bounce the ball L if needed
        if self.y + self.dem/2 > paddleL.y and self.y + self.dem/2 < (paddleL.y + paddleL.demY) and self.x < (paddleL.x + paddleL.demX):
            print("paddle hit")
            self.changeX = self.changeX * -1 * pos

        if self.y + self.dem/2 > paddleR.y and self.y + self.dem/2 < (paddleR.y + paddleR.demY) and self.x + self.dem > paddleR.x:
            print("paddle hit")
            self.changeX = self.changeX * -1 * pos
        # bounc ball off top and botom
        if self.y > 490 or self.y < 0:
            self.changeY = self.changeY * -1 





        