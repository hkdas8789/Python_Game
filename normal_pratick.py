
"""
import pygame
import random
pygame.init()

# screen size and all veribals

screen_length=1300
screen_bredth=600

game_exit=False
game_quit=False

Game_name="Snake game"

snake_x=30
snake_y=30

velocity_x=0
velocity_y=0



Green=(0,255,0)
Blue=(0,0,255)
Red=(255,0,0)

snake_size=30



clock=pygame.time.Clock()
FPS=60

score = 0
# Game window
Game_window=pygame.display.set_mode((screen_length,screen_bredth))
# Game title ie. name
Game_title=pygame.display.set_caption(Game_name)
# Food
food_x=random.randint(50,screen_length)
food_y=random.randint(50,screen_bredth)
# Game loop
while not game_exit:
    for Event in pygame.event.get():
        if Event.type==pygame.QUIT:
            game_exit=True
        if Event.type==pygame.KEYDOWN:
            if Event.key==pygame.K_UP:
                velocity_y = -10
                velocity_x = 0
            elif Event.key==pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0
            elif Event.key==pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0
            elif Event.key==pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    Game_window.fill(Blue)
    # pygame.draw.rect(Game_window,Green,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(Game_window, Green, [snake_x, snake_y, snake_size, snake_size]) # snake moves in this line (see snake_x and snake_y).
    pygame.draw.rect(Game_window, Red,[food_x,food_y,snake_size,snake_size])
    if abs(snake_x-food_x)<snake_size and abs(snake_y-food_y)<snake_size:
        score = score + 1
        print("Score:",score * 10)
        food_x = random.randint(50, screen_length)
        food_y = random.randint(50, screen_bredth)

    clock.tick(FPS)

    pygame.display.update()


pygame.quit()
quit()

"""




import pygame
from random import randint
pygame.init()

game_bredth=500
game_length=1000
Game_window=pygame.display.set_mode((game_length,game_bredth,))
Game_title=pygame.display.set_caption("Game")
game_exit=False
game_quit=False
snake_x=10
snake_y=40
velocity_x=0
velocity_y=0
yellow=(255,255,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)

snake_size=20
score=0

food_x=randint(50,game_length-100)
food_y=randint(50,game_bredth-100)

font=pygame.font.SysFont(None, 50) # score in screen function (new).
def SCORE(text, color, x, y): # score in screen function (new).
    screen_text=font.render(text,True,color) # score in screen function (new).
    Game_window.blit(screen_text,[x,y]) # score in screen function (new).


clock=pygame.time.Clock()
FPS=120
game_speed=1
while not game_exit:
    for Event in pygame.event.get():
        # print(Event)
        if Event.type==pygame.QUIT:
            game_exit=True
        if Event.type==pygame.KEYDOWN:
            if Event.key==pygame.K_RIGHT:
                velocity_x=game_speed
                velocity_y=0
            elif Event.key==pygame.K_LEFT:
                velocity_x=-game_speed
                velocity_y=0
            elif Event.key==pygame.K_DOWN:
                velocity_y=game_speed
                velocity_x=0
            elif Event.key==pygame.K_UP:
                velocity_y=-game_speed
                velocity_x=0
    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y

    # food_x=food_x+velocity_x
    # food_y=food_y+velocity_y

    Game_window.fill(yellow)
    if abs(food_x-snake_x)<=snake_size and abs(food_y-snake_y)<=snake_size:
        # velocity_x+=2
        # velocity_y+=2
        game_speed+=1
        score+=1
        food_x = randint(50, game_length - 100)
        food_y = randint(50, game_bredth - 100)

    SCORE("Score: " + str(score * 10), black, 2, 1)  # score in screen function (new).


    pygame.draw.rect(Game_window,blue,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(Game_window,red,[food_x,food_y,snake_size,snake_size])
    clock.tick(FPS)

    pygame.display.update()


pygame.quit()
quit()



