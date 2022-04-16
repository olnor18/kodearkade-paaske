import pygame
import random

class Eggspot(pygame.sprite.Sprite):
    i = 0
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprites/eggs/spot.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hidden = False

    def hideEgg(self):
        self.image = pygame.image.load(f"sprites/eggs/egg{self.i}.png")
        self.hidden = True
        self.image = pygame.transform.scale(self.image, (self.image.get_rect().width/2, self.image.get_rect().height/2))

def generateSpots(n, windowX, windowY, bushes, spots=[]):
    for _ in range(n - len(spots)):
        spots.append(Eggspot(random.randint(20, windowX-20), random.randint(20, windowY-20)))
    for spot in spots:
        for otherSpot in spots:
            if spot != otherSpot and spot.rect.colliderect(otherSpot.rect):
                spots.remove(spot)
                return generateSpots(n, windowX, windowY, bushes, spots)
        for bush in bushes:
            if spot.rect.colliderect(bush.rect):
                spots.remove(spot)
                return generateSpots(n, windowX, windowY, bushes, spots)
                
    color = list(range(n))
    random.shuffle(color)
    for i, spot in enumerate(spots):
        spot.i = color[i]
    return spots