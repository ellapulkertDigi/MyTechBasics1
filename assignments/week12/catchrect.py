import pygame
import random


pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Game")

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

player = pygame.Rect(100, 100, 50, 50)
target = pygame.Rect(200, 150, 30, 30)

clock = pygame.time.Clock()
run = True

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    if player.colliderect(target):
        target.x = random.randint(0, 470)
        target.y = random.randint(0, 370)

    screen.fill(white)
    pygame.draw.rect(screen, blue, player)
    pygame.draw.rect(screen, red, target)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
