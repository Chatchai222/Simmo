import pygame

class Sensor:
    LINE_DETECT_COLOR = (255,0,0)
    NO_LINE_DETECT_COLOR = (255,255,255)

    def __init__(self, width, height, x_pos, y_pos):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.surface = pygame.Surface(width, height)
        self.surface.fill(Sensor.NO_LINE_DETECT_COLOR)

        self.is_detect_line = False

    def




