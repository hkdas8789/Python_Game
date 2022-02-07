from colorss import*

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
score=0 # new
init_velocity=10 # new
# Colors

Green=(0,255,0)
Blue=(0,0,255)
red=(255,0,0)

# Clock
clock=pygame.time.Clock()
FPS=60

font=pygame.font.SysFont(None, 50) # score in screen function (new).
def text_screen(text, color, x, y): # score in screen function (new).
    screen_text=font.render(text,True,color) # score in screen function (new).
    Game_window.blit(screen_text,[x,y]) # score in screen function (new).

def plot_snake(Game_window, color, snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(Game_window,color,[x,y,snake_size,snake_size])

snk_list=[]
snk_length=1
# Game Loop
if __name__ == '__main__':

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
                # Cheet code
                elif event.key==pygame.K_i:
                    score+=10
        snake_x = snake_x + velocity_x
        snake_y = snake_y + velocity_y

        if abs(snake_x - food_x) < snake_size and abs(snake_y - food_y) < snake_size:
            score +=1
            food_x = random.randint(50, game_width-50)
            food_y = random.randint(50, game_heigth-50)
            snk_length +=3


        Game_window.fill(yellow)

        text_screen("Score: "+str(score * 10),red,2,1) # score in screen function (new).
        # print(pygame.font.match_font('bitstreamverasans'))

        pygame.draw.rect(Game_window,red,[food_x,food_y,snake_size,snake_size])
        # pygame.draw.rect(Game_window,Blue,[snake_x,snake_y,snake_size,snake_size])
        head=[]
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if len(snk_list) > snk_length:
            del snk_list[0]

        plot_snake(Game_window,Blue,snk_list,snake_size)
        clock.tick(FPS)

        pygame.display.update()




    pygame.quit()
    quit()