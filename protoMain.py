import pygame
from Buggy.Buggy import Buggy

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Simmo")

buggy = Buggy()

# Color
BLACK = (0,0,0)

clock = pygame.time.Clock()
FPS = 60
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update movement
    keys_pressed = pygame.key.get_pressed()
    buggy.update_movement(keys_pressed)

    # Drawing onto screen
    WIN.fill((0, 0, 0))
    WIN.blit(buggy.surface, buggy.rect)

    pygame.display.update()

pygame.quit()

