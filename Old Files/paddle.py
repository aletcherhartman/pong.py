class Paddle:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self,x,y,demX,demY,changeX,changeY):
        self.x = x
        self.y = y
        self.demX = demX
        self.demY = demY
        self.changeX = changeX
        self.changeY = changeY

    def buildPaddle(self,Paddle):
    	# paddle = Paddle()

    	# paddle.x = 60
    	# paddle.y = 90
    	# paddle.demX = 20
     #    paddle.demY = 30
    	# paddle.changeX = 0
     #    paddle.changeY = 0

        # Draw a rectangle
    	pygame.draw.rect(screen, BLACK, [paddle.x, paddle.y, paddle.demX, paddle.demY], 2)

    	return Paddle