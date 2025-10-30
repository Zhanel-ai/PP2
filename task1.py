import pygame
import math
from datetime import datetime

def blitrotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(center=(pos[0], pos[1]))
    rotated_image = pygame.transform.rotate(image, -angle) 
    rotated_rect = rotated_image.get_rect(center=image_rect.center)
    surf.blit(rotated_image, rotated_rect)

pygame.init()
clocks = pygame.image.load("/Users/zhanel/Downloads/clock.png")
minutes = pygame.image.load("/Users/zhanel/Downloads/rightarm.png")
seconds = pygame.image.load("/Users/zhanel/Downloads/leftarm.png")
screen = pygame.display.set_mode(clocks.get_size())
clock = pygame.time.Clock()

center_x, center_y = screen.get_width() // 2, screen.get_height() // 2
minutes_pos = (center_x, center_y)
seconds_pos = (center_x, center_y)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    now = datetime.now()
    second_angle = (now.second / 60) * 360
    minute_angle = (now.minute / 60) * 360
    screen.fill((255, 255, 255)) 
    screen.blit(clocks, (0, 0))
    blitrotate(screen, minutes, minutes_pos, (0, 0), minute_angle)
    blitrotate(screen, seconds, seconds_pos, (0, 0), second_angle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()