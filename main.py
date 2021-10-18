import pygame
from gpiozero import LED

LEFT_LIGHT_BULB_PIN = 17
RIGHT_LIGHT_BULB_PIN = 3

SENSOR_DETECT_LINE_COLOR = "Red"
SENSOR_NOT_DETECT_LINE_COLOR = "White"

def update_sensor_color_and_light_bulb(in_sensor, in_sensor_rect, in_line_rect, in_light_bulb=None):
    if(in_sensor_rect.colliderect(in_line_rect)):
        in_sensor.fill(SENSOR_DETECT_LINE_COLOR)
        #in_light_bulb.on()
    else:
        in_sensor.fill(SENSOR_NOT_DETECT_LINE_COLOR)
        #in_light_bulb.off()

def main():
    WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Simmo")

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    FPS = 60

    # Buggy info
    BUGGY_WIDTH, BUGGY_HEIGHT = 50, 100
    buggy = pygame.Surface((BUGGY_WIDTH, BUGGY_HEIGHT))
    buggy.fill('Grey')
    buggy_rect = pygame.Rect(200, 200, BUGGY_WIDTH, BUGGY_HEIGHT)

    # Line information
    LINE_WIDTH, LINE_HEIGHT = 10, WINDOW_HEIGHT
    line = pygame.Surface((LINE_WIDTH, LINE_HEIGHT))
    line.fill('Yellow')
    line_rect = pygame.Rect(WINDOW_WIDTH / 2, 0, LINE_WIDTH, LINE_HEIGHT)

    # Sensors information
    LEFT_SENSOR_WIDTH, LEFT_SENSOR_HEIGHT = BUGGY_WIDTH / 2, BUGGY_WIDTH / 2
    left_sensor = pygame.Surface((LEFT_SENSOR_WIDTH, LEFT_SENSOR_HEIGHT))
    left_sensor.fill('Orange')
    left_sensor_rect = pygame.Rect(buggy_rect.topleft, (buggy_rect.width / 2, buggy_rect.width / 2))

    RIGHT_SENSOR_WIDTH, RIGHT_SENESOR_HEIGHT = BUGGY_WIDTH / 2, BUGGY_WIDTH / 2
    right_sensor = pygame.Surface((RIGHT_SENSOR_WIDTH, RIGHT_SENESOR_HEIGHT))
    right_sensor.fill('Green')
    right_sensor_rect = pygame.Rect(buggy_rect.midtop, (buggy_rect.width / 2, buggy_rect.width / 2))

    # The LED information
    # left_light_bulb = LED(LEFT_LIGHT_BULB_PIN)
    # right_light_bulb = LED(RIGHT_LIGHT_BULB_PIN)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            buggy_rect.y -= 1
        if keys_pressed[pygame.K_s]:
            buggy_rect.y += 1
        if keys_pressed[pygame.K_a]:
            buggy_rect.x -= 1
        if keys_pressed[pygame.K_d]:
            buggy_rect.x += 1

        # Update the position of the sensor relative to the buggy
        left_sensor_rect.update(buggy_rect.topleft, (left_sensor_rect.width, left_sensor_rect.width))
        right_sensor_rect.update(buggy_rect.midtop, (right_sensor_rect.width, right_sensor_rect.width))

        # Update the color of sensor if it detect that it's overlap the line as well as the actual physical light bulb
        update_sensor_color_and_light_bulb(left_sensor, left_sensor_rect, line_rect, None)
        update_sensor_color_and_light_bulb(right_sensor, right_sensor_rect, line_rect, None)

        # Update the screen
        WIN.fill(BLACK)
        WIN.blit(buggy, buggy_rect) # Stands for block image transfer
        WIN.blit(line, line_rect)
        WIN.blit(left_sensor, left_sensor_rect)
        WIN.blit(right_sensor, right_sensor_rect)
        pygame.display.update()


    pygame.quit()

main()