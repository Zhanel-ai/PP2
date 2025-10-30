#task1
import pygame
import math
from datetime import datetime

#function for images
def blitrotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(center=(pos[0], pos[1]))
    rotated_image = pygame.transform.rotate(image, -angle) 
    rotated_rect = rotated_image.get_rect(center=image_rect.center)
    surf.blit(rotated_image, rotated_rect)

#Initialization
pygame.init()
clocks = pygame.image.load("/Users/zhanel/Downloads/clock.png")
minutes = pygame.image.load("/Users/zhanel/Downloads/rightarm.png")
seconds = pygame.image.load("/Users/zhanel/Downloads/leftarm.png")
screen = pygame.display.set_mode(clocks.get_size())
clock = pygame.time.Clock()

#center
center_x, center_y = screen.get_width() // 2, screen.get_height() // 2
minutes_pos = (center_x, center_y)
seconds_pos = (center_x, center_y)

#loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#time
    now = datetime.now()
    second_angle = (now.second / 60) * 360
    minute_angle = (now.minute / 60) * 360

#drawing
    screen.fill((255, 255, 255)) 
    screen.blit(clocks, (0, 0))
    blitrotate(screen, minutes, minutes_pos, (0, 0), minute_angle)
    blitrotate(screen, seconds, seconds_pos, (0, 0), second_angle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()








#task2
import pygame
import os
pygame.init()
pygame.mixer.init()

#size
WIDTH, HEIGHT = 600, 150
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)

#mp3
songs = [f for f in os.listdir() if f.endswith(".mp3")]
current_song_index = 0

#function for music playing
def play_music(index):
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()
if songs:
    play_music(current_song_index)

running = True
paused = False

#cycle
while running:
    screen.fill((255, 255, 255)) 
    state_text = "Paused" if paused else "Playing"
    label = font.render(f"{songs[current_song_index]} ({state_text})", True, (0, 0, 0))
    screen.blit(label, (50, HEIGHT // 2))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused

            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(songs)
                play_music(current_song_index)
                paused = False
            elif event.key == pygame.K_LEFT: 
                current_song_index = (current_song_index - 1) % len(songs)
                play_music(current_song_index)
                paused = False
    
    pygame.display.flip()

pygame.quit()








#task3
import pygame

pygame.init()

#size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Movement 🎈")

#colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#parametres
radius = 25
x = WIDTH // 2
y = HEIGHT // 2
speed = 20

running = True
clock = pygame.time.Clock()

#cicle
while running:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#moving
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - radius - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + radius + speed <= HEIGHT:
        y += speed
    if keys[pygame.K_LEFT] and x - radius - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius + speed <= WIDTH:
        x += speed

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
