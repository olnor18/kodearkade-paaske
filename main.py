import pygame
import time
import random
from bunny import Bunny, UPDATEBUNNY
from bush import Bush, generateBushes
from eggspot import Eggspot, generateSpots

windowX = 720
windowY = 480
 
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(132, 192, 17)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Easter Bunny Simulator')
screen = pygame.display.set_mode((windowX, windowY))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()

eggsHidden = 0

bunny = Bunny(windowX/2, windowY/2, 15)
bushes = []
spots = []

for bush in generateBushes(10, windowX, windowY):
    bushes.append(bush)

for spot in generateSpots(10, windowX, windowY, bushes):
    spots.append(spot)

all_sprites = pygame.sprite.Group()

all_sprites.add(spots)
all_sprites.add(bunny)
all_sprites.add(bushes)

myfont = pygame.font.SysFont("calibri bold", 32)

pygame.key.set_repeat(500, 500)

begun = False
readManual = False

while True:
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if not begun:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                begun = True
                continue

        if begun and not readManual:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                readManual = True

        if begun and readManual and eggsHidden != 10:
            if event.type == UPDATEBUNNY:
                bunny.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bunny.move('UP')
                if event.key == pygame.K_DOWN:
                    bunny.move('DOWN')
                if event.key == pygame.K_LEFT:
                    bunny.move('LEFT')
                if event.key == pygame.K_RIGHT:
                    bunny.move('RIGHT')
                if event.key == pygame.K_SPACE:
                    for spot in spots:
                        if bunny.rect.colliderect(spot.rect) and spot.hidden == False:
                            eggsHidden += 1
                            spot.hideEgg()
                            break

    if not begun:
        screen.fill(white)
        font = pygame.font.SysFont("calibri bold", 56)
        Title = font.render("Easter Bunny Simulator", 1, black)
        screen.blit(Title, (windowX/2 - Title.get_width()/2, windowY/2 - Title.get_height()/2))
        continuetext = myfont.render("Press space to begin...", 1, black)
        screen.blit(continuetext, (windowX/2 - continuetext.get_width()/2, windowY/2 + Title.get_height() + 20 - continuetext.get_height()/2))
        pygame.display.update()
        fps.tick(30)
        continue

    if not readManual:
        screen.fill(white)
        Title = myfont.render("Place all of the eggs for the easter bunny", 1, black)
        screen.blit(Title, (windowX/2 - Title.get_width()/2, windowY/4 - Title.get_height()/2))
        Instruction1 = myfont.render("Move the bunny with the arrow keys", 1, black)
        screen.blit(Instruction1, (windowX/2 - Instruction1.get_width()/2, windowY/4 + Title.get_height() + 20 - Instruction1.get_height()/2))
        Instruction2 = myfont.render("Go to the signs and press space to place the eggs", 1, black)
        screen.blit(Instruction2, (windowX/2 - Instruction2.get_width()/2, windowY/4 + Title.get_height() + Instruction1.get_height() + 20 * 2 - Instruction2.get_height()/2))
        continuetext = myfont.render("Press space to begin...", 1, black)
        screen.blit(continuetext, (windowX/2 - continuetext.get_width()/2, windowY/4*3 ))
        pygame.display.update()
        fps.tick(30)
        continue

    if eggsHidden == 10:
        screen.fill(white)
        font = pygame.font.SysFont("calibri bold", 56)
        wontext = font.render("You placed all the eggs!", 1, black)
        screen.blit(wontext, (windowX/2 - wontext.get_width()/2, windowY/2 - wontext.get_height()/2))
        pygame.display.update()
        fps.tick(30)
        continue

    #all_sprites.update()
    screen.fill(green)

    scoretext = myfont.render("Eggs Placed: "+str(eggsHidden), 1, white)
    

    #pygame.draw.rect(game_window, white, pygame.Rect(bunny.position['x'], bunny.position['y'], 20, 20))
    all_sprites.draw(screen)
    screen.blit(scoretext, (5, 10))
    pygame.display.update()
    fps.tick(30)
        