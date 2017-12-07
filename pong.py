import pygame
from paddle import Paddle
from ball import Ball


def end(ball,paddleL,scoreR, scoreL,screen):
    BLACK = (0, 0, 0)
    ball.changeX = 0
    ball.changeY = 0
    font = pygame.font.SysFont('Calibri', 25, False, False)
    text = font.render( "Click to Play Again".format(scoreR, scoreL), True, BLACK)
    screen.blit(text, [280, 300])

def playGame(): 
    scoreL = 0
    scoreR = 0
    changeX = 0
    changeY = 0

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
     
    pygame.init()

    #initclass
    ball = Ball(30,20,10,changeX,changeY,0)
    paddleL = Paddle(60,90,20,50)
    paddleR = Paddle(60,90,20,50)

    # Set the width and height of the screen [width, height]
    size = (700, 500)
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("pong2")
     
    # Loop until the user clicks the close button.
    done = False
    freez = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    display_instructions = True
    instruction_page = 1
 
    # -------- Instruction Page Loop -----------
    while not done and display_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN and posX > 350:
                display_instructions = False
                changeX = 6
                changeY = 7
                ball.setSpeed(changeX,changeY)

            if event.type == pygame.MOUSEBUTTONDOWN and posX < 350:
                display_instructions = False
                changeX = 3
                changeY = 4
                ball.setSpeed(changeX,changeY)
        # Set the screen background
        screen.fill(WHITE)

        pos = pygame.mouse.get_pos()
        posX = pos[0]
     
        if instruction_page == 1:

            font = pygame.font.SysFont('Calibri', 70, False, False)
            text = font.render("Choose Your Level", True, BLACK)
            screen.blit(text, [140, 200])
            font = pygame.font.SysFont('Calibri', 45, False, False)
            text = font.render("Easy", True, BLACK)
            screen.blit(text, [230, 300])

            text = font.render("Hard", True, BLACK)
            screen.blit(text, [380, 300])
     
     
        # Limit to 60 frames per second
        clock.tick(60)
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Game logic should go here
        ball.moveBall(size,screen,paddleL, paddleR)

        # resetGame(ball,scoreL,scoreR)
        if ball.x < 0:
            ball.x = 350
            scoreL += 1
            ball.setSpeed(changeX,changeY)
        if ball.x > 700:
            ball.x = 350
            scoreR += 1
            ball.setSpeed(changeX,changeY)
        # print scoreL
        # print scoreR

        # --- Screen-clearing code goes here
        screen.fill(WHITE)

        # --- Drawing code should go here

        # Draw paddles
        paddleL.buildPaddleL(screen,BLACK,freez)
        paddleR.buildPaddleR(screen,BLACK,ball)

        # Draw ball
        ball.buildBall(screen,BLACK)

        # Draw score
        font = pygame.font.SysFont('Calibri', 25, False, False)
     
        # Render the text. "True" means anti-aliased text.
        text = font.render( "{}:{}".format(scoreR, scoreL), True, BLACK)

        # Put the image of the text on the screen at 250x250
        screen.blit(text, [330, 20])

        # --- Limit to 60 frames per second
        clock.tick(60)

        if scoreL == 10:
            freez = True
            end(ball, paddleL, scoreR, scoreL, screen)
            font = pygame.font.SysFont('Calibri', 70, False, False)
            text = font.render( "You Lost!!".format(scoreR, scoreL), True, BLACK)
            screen.blit(text, [240, 200])
            if event.type == pygame.MOUSEBUTTONDOWN:
                    paddleL.x = 60
                    paddleL.y = 90
                    ball.x = 30
                    ball.y = 50
                    ball.changeX = changeX
                    ball.changeY = changeY
                    scoreL = 0
                    scoreR = 0
                    freez = False

        elif scoreR == 10:
            freez = True
            end(ball,paddleL,scoreR, scoreL,screen)
            font = pygame.font.SysFont('Calibri', 70, False, False)
            text = font.render( "You Won!!".format(scoreR, scoreL), True, BLACK)
            screen.blit(text, [240, 200])
            if event.type == pygame.MOUSEBUTTONDOWN:
                    paddleL.x = 60
                    paddleL.y = 90
                    ball.x = 30
                    ball.y = 50
                    ball.changeX = changeX
                    ball.changeY = changeY
                    scoreL = 0
                    scoreR = 0
                    freez = False

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    # Close the window and quit.
    pygame.quit()

playGame()







