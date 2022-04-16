import pygame

UPDATEBUNNY = pygame.USEREVENT + 1
class Bunny(pygame.sprite.Sprite):   
    inmotion = False

    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("sprites/bunny/up-sit.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.direction = "UP"

    def move(self, direction):
        if self.inmotion:
            return
        self.direction = direction
        self.image = pygame.image.load(f"sprites/bunny/{self.direction.lower()}-jump.png")
        self.inmotion = True
        pygame.time.set_timer(UPDATEBUNNY, 200)
        

    def update(self):
        if self.inmotion:
            self.inmotion = False
            self.image = pygame.image.load(f"sprites/bunny/{self.direction.lower()}-sit.png")
            if self.direction == 'UP':
                self.rect.y -= 1*self.speed
            elif self.direction == 'DOWN':
                self.rect.y += 1*self.speed
            elif self.direction == 'LEFT':
                self.rect.x -= 1*self.speed
            elif self.direction == 'RIGHT':
                self.rect.x += 1*self.speed
