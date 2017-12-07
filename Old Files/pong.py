import pygame
import ball
import paddel
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25

def main():

    """
    This is our main program.
    """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Pong")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    ball = Ball.make_ball()


    # # -------- Main Program Loop -----------
    # while not done:
    #     # --- Event Processing
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             done = True
    #         elif event.type == pygame.KEYDOWN:
    #             # Space bar! Spawn a new ball.
    #             if event.key == pygame.K_SPACE:
    #                 ball = make_ball()
    #                 ball_list.append(ball)

        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
        
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()