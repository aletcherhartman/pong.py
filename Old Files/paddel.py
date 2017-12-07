VIPERimport pygame
import math

class paddel(object):
     """docstring for paddel"""
    def __init__(self, arg):
        self.X = 30
        self.Y = 30
        self.change_x = 0
        self.change_y = 0

    def makePaddel(self):
        
        paddel = paddel()

        # Hide the mouse cursor
        pygame.mouse.set_visible(0)
        
        # Draw the paddelangle
        pygame.draw.paddel(screen, WHITE, [paddel.X, paddel.Y, 30, 60])
        
    def playerMotion(self):
        pos = pygame.mouse.get_pos()
        paddel.Y = pos[1]

    def compMotion(self,ballY):
        paddelY = math.abs(ball.y - ball.y*0.2);
    
        if paddelY-paddelX/2<0
          paddel.y += paddel.change_y
        
        if paddelY+paddelX/2>height 
          paddel.y -= paddel.change_y
        


    return paddel