import pygame

class Paddle:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self,x,y,demX,demY):
        self.x = x
        self.y = y
        self.demX = demX
        self.demY = demY

    def buildPaddleL(self,screen,BLACK,freez):
        self.x = 30
        if self.y > 460:
        	self.y = 460

        if freez == False:
	        pos = pygame.mouse.get_pos()
	        self.y = pos[1]

        if freez == True:
	        self.y = 200


        # Draw a rectangle
    	pygame.draw.rect(screen, BLACK, [self.x, self.y, self.demX, self.demY], 2)

    	return Paddle

    def buildPaddleR(self,screen,BLACK,ball):
        self.x = 650
        self.y = abs(ball.y-ball.y*0.2)

        # Draw a rectangle
        pygame.draw.rect(screen, BLACK, [self.x, self.y, self.demX, self.demY], 2)

        return Paddle









