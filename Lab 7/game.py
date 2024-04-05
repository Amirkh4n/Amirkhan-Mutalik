import pygame
import time
import sys
import os

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Clock")

# Load Mickey image
mickey_image = pygame.image.load('mickey.png')

# Set Mickey's position
mickey_rect = mickey_image.get_rect(center=(screen_width//2, screen_height//2))

# Load music files
music_files = ["music1.mp3", "music2.mp3", "music3.mp3"]  # Replace with your music files

# Initialize music player
pygame.mixer.init()
current_music_index = 0

# Load first music
pygame.mixer.music.load(music_files[current_music_index])

clock = pygame.time.Clock()

def draw_clock():
    current_time = time.strftime("%H:%M:%S")
    font = pygame.font.Font(None, 50)
    text = font.render(current_time, True, (255, 255, 255))
    screen.blit(text, (10, 10))

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_music():
    global current_music_index
    current_music_index = (current_music_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_music_index])
    pygame.mixer.music.play()

def prev_music():
    global current_music_index
    current_music_index = (current_music_index - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_music_index])
    pygame.mixer.music.play()

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        mickey_rect.centery -= 20
    if keys[pygame.K_DOWN]:
        mickey_rect.centery += 20
    if keys[pygame.K_LEFT]:
        mickey_rect.centerx -= 20
    if keys[pygame.K_RIGHT]:
        mickey_rect.centerx += 20

    # Check if Mickey is out of screen
    mickey_rect.clamp_ip(screen.get_rect())

    screen.fill((255, 255, 255))
    screen.blit(mickey_image, mickey_rect)
    draw_clock()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
