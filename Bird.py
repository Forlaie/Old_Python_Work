import pygame
import time
import random
import math

pygame.init()

screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

bird = pygame.image.load(r'C:\Users\jessi\Downloads\rsz_1rsz_bird_character.png')

green = (0, 255, 128)
blue = (0, 191, 255)
white = (255, 255, 255)
black = (0, 0, 0)

myFont = pygame.font.SysFont("Times New Roman", 30)

start = "Start (Press S)"
lose = "You have lost!"
restart = "Restart? (Press R)"
stop = "Quit? (Press Q)"
sscreen = myFont.render(start, 1, black)
lscreen = myFont.render(lose, 1, black)
rscreen = myFont.render(restart, 1, black)
qscreen = myFont.render(stop, 1, black)

key_press_interval = 0.3
moving_interval = 0.002
max_up_steps = 20

last_time = 0.0
action = ""

player_x = 100
player_y = 250
#enemy_x = 1000
width = 50
#enemy_x = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
space = 150
num = 0

def height():
    listOfTop = []
    listOfBottom = []
    enemy_x = list(range(1000, 2500, 150))
    for i in range(10):
        top_height = random.randint(100, 250)
        bottom_height = random.randint(450, 600)
        listOfTop.append(top_height)
        listOfBottom.append(bottom_height)
    return enemy_x, listOfTop, listOfBottom

gameFinished = False
beginning = True
inProgress = False

while gameFinished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameFinished = True

    keys = pygame.key.get_pressed()

    if keys[ord('q')]:
        gameFinished = True

    if inProgress == False and beginning == False:
        if keys[ord('r')]:
            beginning = True

    if beginning == True:
        num = 0
        player_x = 100
        player_y = 250
        enemy_x, listOfTop, listOfBottom = height()
        #enemy_x = 1000
        #enemy_x, listOfTop, listOfBottom = height()
        screen.fill(white)
        screen.blit(bird, [player_x, player_y])
        #pygame.draw.rect(screen, green, [1000, 0, width, listOfTop[0]])
        #pygame.draw.rect(screen, green, [1000, listOfBottom[0], width, 250])
        screen.blit(sscreen, [400, 300])
        pygame.display.update()
        if keys[ord('s')]:
            beginning = False
            inProgress = True

    if inProgress == True:

        #space -= 1

        for i in range(10):
            enemy_x[i] -= 3
            if enemy_x[i] > -50 and enemy_x[i] <= 1000:
                pygame.draw.rect(screen, green, [enemy_x[i], 0, width, listOfTop[i]])
                pygame.draw.rect(screen, green, [enemy_x[i], listOfBottom[i], width, 250])
        pygame.display.update()

        for i in range(10):
            if player_y < listOfTop[i] and abs(player_x - enemy_x[i]) <= 30:
                inProgress = False
                screen.blit(lscreen, [400, 200])
                screen.blit(rscreen, [550, 350])
                screen.blit(qscreen, [250, 350])
                pygame.display.update()
            if abs(player_y - listOfBottom[i]) < 100 and abs(player_x - enemy_x[i]) <= 30:
                inProgress = False
                screen.blit(lscreen, [400, 200])
                screen.blit(rscreen, [550, 350])
                screen.blit(qscreen, [250, 350])
                pygame.display.update()

        if enemy_x[0] < -50:
            x = enemy_x[-1] + 150
            enemy_x = enemy_x[1:]
            enemy_x.append(x)

            listOfTop = listOfTop[1:]
            listOfTop.append(random.randint(100, 250))

            listOfBottom = listOfBottom[1:]
            listOfBottom.append(random.randint(450, 600))

        # if space == 0:
        #     num += 1
        #     space = 150

        # if num == 10:
        #     listOfTop, listOfBottom = height()
        #     # space = 150
        #     #enemy_x = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
        #     num = 0

        # if keys[pygame.K_SPACE]:
        #     player_y -= 1
        # else:
        #     player_y += 1

        if keys[pygame.K_SPACE]:
            if (time.time() - last_time) > key_press_interval:
                last_time = time.time()
                action = "up"
                up_count = 0

        if action == "up":
            up_count += 1
            if up_count <= max_up_steps:
                player_y -= 5
                pygame.display.update()
            else:
                action = ""
        else:
            player_y += 2
            pygame.display.update()

        time.sleep(moving_interval)

        if player_y <= -102:
            inProgress = False
            screen.blit(lscreen, [400, 200])
            screen.blit(rscreen, [550, 350])
            screen.blit(qscreen, [250, 350])
            pygame.display.update()
        elif player_y >= 700:
            inProgress = False
            screen.blit(lscreen, [400, 200])
            screen.blit(rscreen, [550, 350])
            screen.blit(qscreen, [250, 350])
            pygame.display.update()
        else:
            screen.fill(white)
            screen.blit(bird, [player_x, player_y])

pygame.quit()
quit()
