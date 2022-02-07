import pygame
pygame.init()
# print(x)
#Creating window
gameWindow = pygame.display.set_mode((1200,500))    # display
pygame.display.set_caption("My first game")     # title
 #Game specific variables
exit_game = False
game_over = False

# Creating a game loop
while  not exit_game:
    for  event in pygame.event.get():   # Event in pygame
        if event.type == pygame.QUIT: # Exit game
            exit_game = True    # Exit game

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You've enter right arrow key")

pygame.quit()
quit()
