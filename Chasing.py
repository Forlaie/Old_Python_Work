import sys
import pygame
import math

def playGame():
    pygame.init()

    screen = pygame.display.set_mode((1000, 700))
    clock = pygame.time.Clock()

    background = pygame.image.load(r'C:\Users\jessi\Downloads\city landscape.jpg')
    player = pygame.image.load(r'C:\Users\jessi\Downloads\spidey character.png')
    enemy = pygame.image.load(r'C:\Users\jessi\Downloads\kingpin character (2).png')

    gameFinished = False
    colour = (66, 244, 212)
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 153)
    red = (255, 0, 0)
    player_x = 100
    player_y = 100
    enemy_x = 800
    enemy_y = 500

    time = 0
    lose = "You have lost!"
    stop = "Quit? (Press Q)"
    restart = "Restart? (Press R)"
    keepGoing = "Continue? (Press C)"
    single = "Single Player? (Press S)"
    multi = "Multi Player? (Press M)"
    myFont = pygame.font.SysFont("Times New Roman", 30)
    beginning = True
    inProgress = False
    singlePlayer = False
    multiPlayer = False

    while gameFinished == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameFinished = True

        time += 1
        t = str(time/50)
        tscreen = myFont.render(t, 1, white)
        lscreen = myFont.render(lose, 1, white)
        qscreen = myFont.render(stop, 1, white)
        rscreen = myFont.render(restart, 1, white)
        cscreen = myFont.render(keepGoing, 1, white)
        sscreen = myFont.render(single, 1, white)
        mscreen = myFont.render(multi, 1, white)

        keys = pygame.key.get_pressed()

        if keys[ord('q')]:
            gameFinished = True

        if inProgress == False and beginning == False:
            if keys[ord('r')]:
                beginning = True
                inProgress = False
                singlePlayer = False
                multiPlayer = False

            if keys[ord('c')]:
                time = 0
                player_x = 100
                player_y = 100
                enemy_x = 800
                enemy_y = 500
                inProgress = True

        if beginning == True:
            time = 0
            player_x = 100
            player_y = 100
            enemy_x = 800
            enemy_y = 500
            screen.blit(background, (0, 0))
            screen.blit(sscreen, [100, 350])
            screen.blit(mscreen, [600, 350])
            pygame.display.update()
            if keys[ord('s')]:
                beginning = False
                inProgress = True
                singlePlayer = True
                multiPlayer = False
            if keys[ord('m')]:
                beginning = False
                inProgress = True
                singlePlayer = False
                multiPlayer = True

        if inProgress == True:
            if keys[pygame.K_UP]:
                player_y -= 10
            if keys[pygame.K_DOWN]:
                player_y += 10
            if keys[pygame.K_LEFT]:
                player_x -= 10
            if keys[pygame.K_RIGHT]:
                player_x += 10

            if singlePlayer == True:
                if enemy_x > player_x:
                    enemy_x -= 5
                if enemy_x < player_x:
                    enemy_x += 5
                if enemy_y > player_y:
                    enemy_y -= 5
                if enemy_y < player_y:
                    enemy_y += 5

            if multiPlayer == True:
                if keys[ord('w')]:
                    enemy_y -= 10
                if keys[ord('s')]:
                    enemy_y += 10
                if keys[ord('a')]:
                    enemy_x -= 10
                if keys[ord('d')]:
                    enemy_x += 10

            if player_x > 1000:
                player_x = 0
            if player_y > 700:
                player_y = 0
            if player_x < -100:
                player_x = 1000
            if player_y < -100:
                player_y = 700

            if enemy_x > 1000:
                enemy_x = 0
            if enemy_y > 700:
                enemy_y = 0
            if enemy_x < -100:
                enemy_x = 1000
            if enemy_y < -100:
                enemy_y = 700

            if math.sqrt((player_x - enemy_x)**2 + (player_y - enemy_y)**2) <= 110:
                inProgress = False
                # screen.fill(colour)
                screen.blit(background, (0, 0))
                screen.blit(player, (player_x, player_y))
                # pygame.draw.rect(screen, blue, [player_x, player_y, 40, 20])
                screen.blit(enemy, (enemy_x, enemy_y))
                # pygame.draw.rect(screen, red, [enemy_x, enemy_y, 40, 20])
                screen.blit(tscreen, [475, 50])
                screen.blit(lscreen, [400, 200])
                screen.blit(qscreen, [200, 350])
                screen.blit(rscreen, [600, 350])
                screen.blit(cscreen, [350, 500])
                pygame.display.update()
            else:
                #screen.fill(colour)
                screen.blit(background, (0, 0))
                screen.blit(player, (player_x, player_y))
                #pygame.draw.rect(screen, blue, [player_x, player_y, 40, 20])
                screen.blit(enemy, (enemy_x, enemy_y))
                #pygame.draw.rect(screen, red, [enemy_x, enemy_y, 40, 20])
                screen.blit(tscreen, [475, 50])
                pygame.display.update()

            clock.tick(80)

    pygame.quit()
    quit()

playGame()