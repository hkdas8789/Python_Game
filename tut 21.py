import pygame
from colorss import*
from random import randint
from os import  path
from time import sleep


pygame.mixer.init()

pygame.init()

# Game image



# Creating window
screen_width = 1200
screen_height = 600



gameWindow = pygame.display.set_mode((screen_width, screen_height))
bgimg=pygame.image.load("snake.jpg.png")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
front_image=pygame.image.load("front.jpg.jpg")
front_image=pygame.transform.scale(front_image,(screen_width,screen_height)).convert_alpha()
game_over_image=pygame.image.load("game-over_image.jpg.jpg")
game_over_image=pygame.transform.scale(game_over_image,(screen_width,screen_height)).convert_alpha()



# Game Title
pygame.display.set_caption("Snakes")
pygame.display.update()
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.circle(gameWindow, color, [x, y] ,snake_size - 10)     ###############################################################################
#pygame.draw.circle(gameWindow, red, [food_x, food_y], snake_size - 5)
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(skeen_color)
        # text_screen("Welcome to Snakes", black, 430, 250)
        # text_screen("Press Space Bar To Play", black, 385, 300)
        gameWindow.blit(front_image,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('Back.mp3.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    # Check if hiscore file exists
    if(not path.exists("hiscore.txt")):
        with open("hiscore.txt","w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = randint(20, screen_width - 100)
    food_y = randint(20, screen_height  -100)
    score = 0
    init_velocity = 5
    snake_size = 20
    fps = 60
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(yellow)


            gameWindow.blit(game_over_image,(0,0))

            text_screen("Game Over! Press Enter To Continue",white, 280, 420) ##########################################

            text_screen("Your score : "+ str(score),white,500,460)
            text_screen("Hiscore : " +str(hiscore), white, 500, 500)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_c:
                        score +=1000


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<snake_size and abs(snake_y - food_y)<snake_size:
                score += 10
                food_x = randint(20, screen_width - 100)
                food_y = randint(20, screen_height - 100)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(green)
            gameWindow.blit(bgimg,(0,0))

            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), purple, 5, 5)

            pygame.draw.circle(gameWindow, red, [food_x, food_y], snake_size - 10)


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                sleep(0.5)
                pygame.mixer.music.load('gameover.mp3.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                sleep(0.5)
                pygame.mixer.music.load('gameover.mp3.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow,blue, snk_list, snake_size)  ##############################################################################################
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()