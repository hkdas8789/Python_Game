import pygame
pygame.init()

# Colors
white = (255, 255, 255) #
red = (255, 0, 0)   #
black = (0, 0, 0)   #

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snakes_With_Abhishek")
pygame.display.update() # This is your choise. comment or not comment.

# Game specific variables
exit_game = False
game_over = False

# Game Loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True

    gameWindow.fill(red) # new
    pygame.display.update() # new

pygame.quit()
quit()

