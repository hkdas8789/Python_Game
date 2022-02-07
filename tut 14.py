import pygame
import random

pygame.init()

game_width=1200
game_heigth=600

# Game Window

Game_window=pygame.display.set_mode((game_width,game_heigth))

# Game Title

Game_title=pygame.display.set_caption("Snake")

# Game Veribals

game_exit=False
game_quit=False
snake_x=50
snake_y=50
snake_size=20
velocity_x=0
velocity_y=0
food_x=random.randint(50,game_width-50)
food_y=random.randint(50,game_heigth-50)

# Colors

Green=(0,255,0)
Blue=(0,0,255)
red=(255,0,0)

# Clock
clock=pygame.time.Clock()
FPS=30
# Game Loop

while not game_exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_exit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=10
                velocity_y=0
                print("Rightwards")
            elif event.key==pygame.K_UP:
                velocity_y=-10
                velocity_x=0
                print("Upwards")
            elif event.key==pygame.K_LEFT:
                velocity_x=-10
                velocity_y=0
                print("Leftwards")
            elif event.key==pygame.K_DOWN:
                velocity_y=10
                velocity_x=0
                print("Downwards")
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y


    Game_window.fill(Green)
    pygame.draw.rect(Game_window,red,[food_x,food_y,snake_size,snake_size])
    pygame.draw.rect(Game_window,Blue,[snake_x,snake_y,snake_size,snake_size])
    clock.tick(FPS)
    pygame.display.update()




pygame.quit()
quit()