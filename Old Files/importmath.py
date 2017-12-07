import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Instruction Screen")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Starting position of the rectangle
rect_x = 50
rect_y = 50
 
# Speed and direction of rectangle
changeX = 5
changeY = 5
 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
display_instructions = True
instruction_page = 1
 
# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and posY > 250:
            instruction_page += 1
            changeX = 6
            changeY = 7

            if instruction_page == 2:
                display_instructions = False

        if event.type == pygame.MOUSEBUTTONDOWN and posY < 250:
            instruction_page += 1
            changeX = 3
            changeY = 4

            if instruction_page == 2:
                display_instructions = False
    # Set the screen background
    screen.fill(WHITE)

    pos = pygame.mouse.get_pos()
    posY = pos[1]
 
    if instruction_page == 1:
 
        text = font.render("Choose Your Level", True, BLACK)
        screen.blit(text, [10, 10])
 
        text = font.render("Easy", True, BLACK)
        screen.blit(text, [150,470])

        text = font.render("Hard", True, BLACK)
        screen.blit(text, [350,470])
 
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
 
    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y
 
    # Bounce the ball if needed
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()