import pygame
import sys


pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

GREY = (58, 58, 58)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My first game screen")

image = pygame.image.load('image.png')  
image = pygame.transform.scale(image, (300, 300))

image_rect = image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

running = True
while running:
    screen.fill(GREY)  

    screen.blit(image, image_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    pygame.display.flip()

pygame.quit()
sys.exit()
