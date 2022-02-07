import pygame
from random import randint

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
food_x=randint(50,game_width-50)
food_y=randint(50,game_heigth-50)
score=0 # new
init_velocity=10 # new
# Colors

Green=(0,255,0)
Blue=(0,0,255)
red=(255,0,0)

# Clock
clock=pygame.time.Clock()
FPS=60
# Game Loop

while not game_exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_exit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=init_velocity
                velocity_y=0

            elif event.key==pygame.K_UP:
                velocity_y=-init_velocity
                velocity_x=0

            elif event.key==pygame.K_LEFT:
                velocity_x=-init_velocity
                velocity_y=0

            elif event.key==pygame.K_DOWN:
                velocity_y=init_velocity
                velocity_x=0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
        score +=1
        print(f"Score: {score*10}")
        food_x = randint(50, game_width-50)
        food_y = randint(50, game_heigth-50)


    Game_window.fill(Green)
    pygame.draw.rect(Game_window,red,[food_x,food_y,snake_size,snake_size])
    pygame.draw.rect(Game_window,Blue,[snake_x,snake_y,snake_size,snake_size])
    clock.tick(FPS)
    pygame.display.update()




pygame.quit()
quit()