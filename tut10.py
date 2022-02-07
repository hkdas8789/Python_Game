import pygame

pygame.init()

game_width=400
game_heigth=500

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

# Colors

Green=(0,255,0)
Blue=(0,0,255)

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
                snake_x+=10


    Game_window.fill(Green)
    pygame.draw.rect(Game_window,Blue,[snake_x,snake_y,snake_size,snake_size])
    clock.tick(FPS)
    pygame.display.update()




pygame.quit()
quit()