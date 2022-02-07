import pygame

pygame.init()

game_width=400*3
game_heigth=300*2

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
velocity_x=2  # new
velocity_y=2   # new

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
                print("Rightwards")
            elif event.key==pygame.K_UP:
                snake_y-=10
                print("Forwards")
            elif event.key==pygame.K_LEFT:
                snake_x-=10
                print("Leftwards")
            elif event.key==pygame.K_DOWN:
                snake_y+=10
                print("Downwards")
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y


    Game_window.fill(Green)
    pygame.draw.rect(Game_window,Blue,[snake_x,snake_y,snake_size,snake_size])
    clock.tick(FPS)
    pygame.display.update()




pygame.quit()
quit()