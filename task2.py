import pygame
import os
pygame.init()
pygame.mixer.init()

#
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