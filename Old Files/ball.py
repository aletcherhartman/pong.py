import math
import pygame
import random

class Ball:
    """
    Class to keep track of a ball's location and vector.
    """

	def __init__(self,BALL_SIZE):
		self.x = 0
		self.y = 0
		self.change_x = 0
		self.change_y = 0
 
 
	def make_ball():
	    """
	    Function to make a new, random ball.
	    """
	    # --- Logic

        for ball
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y
 
            # Bounce the ball if needed
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1

	    	if math.abs(ball.y-leftPadle.padleY)<ballDiam/2+leftPadle.padleH/2 && leftPadle.padleX-leftPadle.padleW/2 <ball.x && ball.x<leftPadle.padleX+leftPadle.padleW/2
		    	ball.change_y *= -1
		    	ball.change_x *= -1

	    	if math.abs(ball.y-rightPadle.padleY)<ballDiam/2+rightPadle.padleH/2 && rightPadle.padleX-rightPadle.padleW/2 <ball.x && ball.x<rightPadle.padleX+rightPadle.padleW/2
		    	ball.change_y *= -1
		    	ball.change_x *= -1
  

		# Draw the balls
        for ball in ball_list:
            pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)

	    ball = Ball()
	    # Starting position of the ball.
	    # Take into account the ball size so we don't spawn on the edge.
	    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
	    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
	 
	    # Speed and direction of rectangle
	    ball.change_x = random.randrange(3, 5)
	    ball.change_y = random.randrange(2, 4)
	 
	    return ball












