import pygame
import random


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (255, 255, 255)
FPS = 60


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("cute_dachshunds_:)")
clock = pygame.time.Clock()

class Dachshund:
    def __init__(self):

        self.image = pygame.image.load("dachshund_image.jpeg").convert_alpha()

        self.size = random.randint(50, 120)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        self.y = random.randint(50, SCREEN_HEIGHT - self.size)

        self.speed_x = random.randint(3, 8)

        self.x = 0

    def update(self):
        self.x += self.speed_x

        if self.x > SCREEN_WIDTH:
            self.x = -self.size

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


num_dachshunds = random.randint(1,8)
dachshunds = []
for _ in range(num_dachshunds):
    dachshunds.append(Dachshund())


running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    for dachshund in dachshunds:
        dachshund.update()
        dachshund.draw(screen)

    pygame.display.flip()


pygame.quit()
exit(0)
