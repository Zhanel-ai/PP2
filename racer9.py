import pygame, sys
from pygame.locals import *
import random

pygame.init()

# ==============================
# GAME SETTINGS
# ==============================

FPS = 60                              # Frame refresh rate
FramePerSec = pygame.time.Clock()

# Colors (RGB format)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen and Road settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ROAD_LEFT = 50                        # Left road border
ROAD_RIGHT = 350                      # Right road border
SPEED = 3                             # Initial object speed
SCORE = 0                             # Cars passed score
COINS = 0                             # Coins collected

# Text font
font = pygame.font.SysFont("Verdana", 20)

# Background image + initial background Y position
background = pygame.image.load(r"AnimatedStreet.png")
background_y = 0

# Creating window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# ==============================
# ENEMY CAR CLASS
# ==============================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"Enemy.png")
        self.rect = self.image.get_rect()
        # Random position within road borders
        self.rect.center = (random.randint(ROAD_LEFT, ROAD_RIGHT), 0)

    def move(self):
        """Moves enemy car downward and respawns it when leaving the screen."""
        global SCORE
        self.rect.move_ip(0, SPEED)

        # If enemy passes the screen → give score and respawn
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(ROAD_LEFT, ROAD_RIGHT), 0)

# ==============================
# COIN CLASS
# ==============================
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.randomize_coin()

    def randomize_coin(self):
        """Random coin size and value assignment."""
        # 50/50 chance: big or small coin
        if random.choice([True, False]):
            self.size = (50, 50)
            self.value = 3       # Big coin adds 3 points
        else:
            self.size = (30, 30)
            self.value = 1       # Small coin adds 1 point

        self.image = pygame.image.load(r"coin.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()

        # Random spawn on the road
        self.rect.center = (
            random.randint(ROAD_LEFT, ROAD_RIGHT),
            random.randint(40, SCREEN_HEIGHT - 40)
        )

    def move(self):
        """Moves coin downward, respawns when leaving the screen."""
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        """Respawn coin in a new random location with new size/value."""
        self.randomize_coin()

# ==============================
# PLAYER CAR CLASS
# ==============================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80)

    def move(self):
        """Controls player movement using arrow keys."""
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > ROAD_LEFT and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if self.rect.right < ROAD_RIGHT and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        
# ==============================
# SPRITE CREATION
# ==============================

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# ==============================
# MAIN GAME LOOP
# ==============================

while True:
    # Event handling (quit)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Collision with enemy → Game Over
    if pygame.sprite.spritecollideany(P1, enemies):
        game_over_font = pygame.font.SysFont("Verdana", 40)
        game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Background scrolling effect
    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # Display Score and Coins
    scores = font.render(f"Score: {SCORE}", True, BLACK)
    screen.blit(scores, (10, 10))

    coins_text = font.render(f"Coins: {COINS}", True, BLACK)
    screen.blit(coins_text, (300, 10))

    # Move enemy cars
    for enemy in enemies:
        enemy.move()

    # Draw and move all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Collision with coin
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += C1.value
        C1.respawn()

        # Every 5 coins → increase speed
        if COINS % 5 == 0:
            SPEED += 1
           

    pygame.display.update()
    FramePerSec.tick(FPS)