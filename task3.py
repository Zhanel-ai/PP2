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
