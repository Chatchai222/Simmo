import pygame


class Buggy:
    WIDTH = 50
    HEIGHT = 50
    COLOR = (100,100,100)

    def __init__(self, width=50,height=100,x_pos=100, y_pos=100):
        self.surface = pygame.Surface((width,height))
        self.rect = pygame.Rect(x_pos, y_pos,width,height)

        self.surface.fill(Buggy.COLOR)

    def update_movement(self, keys_pressed):
        if keys_pressed[pygame.K_w]: # Up
            self.rect.y -= 1
        if keys_pressed[pygame.K_s]: # Down
            self.rect.y += 1
        if keys_pressed[pygame.K_a]: # Left
            self.rect.x -= 1
        if keys_pressed[pygame.K_d]: # Right
            self.rect.x += 1


