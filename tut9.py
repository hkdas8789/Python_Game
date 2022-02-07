import pygame
pygame.init()

Screen_width=500
Screen_hight=600

Screen_window=pygame.display.set_mode((Screen_width,Screen_hight))
Screen_title=pygame.display.set_caption("Snake game")

game_exit=False
game_quit=False
snake_x=45
snake_y=55
snake_size=10


# Colors
green=(0,255,0)
white=(255,255,255)
blue=(0,0,200)



pygame.display.update()
while not game_exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_exit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                print("Knife")
    Screen_window.fill(blue)
    pygame.draw.rect(Screen_window,green,[snake_x,snake_y,snake_size,snake_size] )
    pygame.display.update()

pygame.quit()
quit()