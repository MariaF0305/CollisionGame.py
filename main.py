import pygame
import random

pygame.init()

WIDTH_OF_SCREEN = 600
HEIGHT_OF_SCREEN = 400

collisionScreen = pygame.display.set_mode((WIDTH_OF_SCREEN, HEIGHT_OF_SCREEN))
pygame.display.set_caption("Square collision with obstacles")

rectangleThatCollides = pygame.Rect(0, 0, 20, 20)
# Here is where I create main rectangle which is the one that is flexible and it can collide with the others

obstacles = []
# It creates an empty list, where in the following can save all the obstacles given
for i in range(1, 20, 1):
    # Here are obstacles with random numbers
    obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
    obstacles.append(obstacle_rect)
# For loop creates 20 square positioned randomly all over the screen

MAGENTA = (255, 0, 255)
BLUE = (0, 255, 0)
RED = (255, 0, 0)
BACKROUND = (50, 50, 50)
# Here are the colors defined

pygame.mouse.set_visible(False)
# Mouse cursor is not visible anymore

is_running = True
while is_running:
    collisionScreen.fill(BACKROUND)
    # Function above updates the screen

    # In the following code it will check collision and change color while they collide
    col = BLUE
    if rectangleThatCollides.collidelist(obstacles) >= 0:
        print(rectangleThatCollides.collidelist(obstacles))
        print(pygame.mouse.get_pos())
        print()
        col = RED

    pygame.draw.rect(collisionScreen, col, rectangleThatCollides)
    for obstacle in obstacles:
        pygame.draw.rect(collisionScreen, MAGENTA, obstacle)
    # The lines above draws all the rectangles randomly on the screen

    # Here it will place the moving square depending on where the mouse courser is placed
    pos = pygame.mouse.get_pos()
    rectangleThatCollides.center = pos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Finally updating the display
    pygame.display.flip()

# After it finishes it is closing the program
pygame.quit()
