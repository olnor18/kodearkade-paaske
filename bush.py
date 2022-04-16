import pygame
import random

class Bush(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprites/bush.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

def generateBushes(n, windowX, windowY, bushes=[]):
    for _ in range(n - len(bushes)):
        bushes.append(Bush(random.randint(0, windowX), random.randint(0, windowY)))
    for bush in bushes:
        for otherBush in bushes:
            if bush != otherBush and bush.rect.colliderect(otherBush.rect):
                bushes.remove(bush)
                return generateBushes(n, windowX, windowY, bushes)
    return bushes