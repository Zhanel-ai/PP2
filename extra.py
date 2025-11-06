#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initializing
pygame.init()

#Setting up FPS 
FPS = 60                              
FramePerSec = pygame.time.Clock()     

#Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3             
SCORE = 0             
COINS = 0            

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


background = pygame.image.load("AnimatedStreet.png")

# --- Set up main screen ---
screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
pygame.display.set_caption("Racer")

# =============================
#      ENEMY CLASS
# =============================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load enemy car image
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        # Start at random x-position at the top of the screen
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        # Move enemy downward
        self.rect.move_ip(0, SPEED)
        # If the enemy moves past the bottom of the screen
        if self.rect.top > 600:
            SCORE += 1   # Add 1 to score
            # Reset enemy position to the top again, at a new random x position
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Flags to control speed increases based on coins collected
c1, c2, c3, c4, c5 = False, False, False, False, False

# =============================
#      COIN CLASS
# =============================
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load coin image and resize it to 40x40 pixels
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        # Spawn at a random position on the road
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

    def move(self):
        """
        Called when player collects a coin.
        Adds to COINS count and increases SPEED gradually
        depending on milestones (10, 20, 30, etc.)
        """
        global COINS, SPEED
        global c1, c2, c3, c4, c5

        # Increase coin count differently depending on vertical position
        if self.rect.bottom < SCREEN_HEIGHT // 3:
            COINS += 3
        elif self.rect.bottom < SCREEN_HEIGHT // 1.5:
            COINS += 2
        else:
            COINS += 1

        # Speed up game after collecting certain numbers of coins
        if not c1 and COINS >= 10:
            SPEED += 1; c1 = True
        if not c2 and COINS >= 20:
            SPEED += 1; c2 = True
        if not c3 and COINS >= 30:
            SPEED += 1; c3 = True
        if not c4 and COINS >= 40:
            SPEED += 1; c4 = True
        if not c5 and COINS >= 50:
            SPEED += 1; c5 = True

        # Move the coin to a new random location after collecting it
        self.rect.top = random.randint(40, SCREEN_WIDTH - 40)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

# =============================
#      PLAYER CLASS
# =============================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load player car image
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        # Start position near bottom center
        self.rect.center = (160, 520)

    def move(self):
        # Move player using arrow keys, with boundary checks
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

# --- Create objects ---
P1 = Player()
E1 = Enemy()
C1 = Coin()

# --- Sprite groups ---
enemies = pygame.sprite.Group()
enemies.add(E1)

coinss = pygame.sprite.Group()
coinss.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# --- Event to increase speed every second ---
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# =============================
#      GAME OVER SCREEN
# =============================
def game_over_screen():
    screen.fill(RED)
    screen.blit(game_over, (30, 250))
    pygame.display.update()

    # Wait until player presses SPACE or ESCAPE
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:  # Restart
                    return True
                elif event.key == K_ESCAPE:  # Exit
                    return False

# Function for crash pause
def handle_crash():
    time.sleep(2)

# --- Background scrolling variable ---
background_y = 0  

# =============================
#       MAIN GAME LOOP
# =============================
while True:
    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1
        if event.type == QUIT:
            pygame.quit(); sys.exit()

    # --- Collision check with enemy ---
    if pygame.sprite.spritecollideany(P1, enemies):
        continue_game = handle_crash()
        if not continue_game:
            pygame.quit(); sys.exit()

    # --- Background scroll effect ---
    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # --- Display scores (top-left) and coins (top-right) ---
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))

    coins = font_small.render(str(COINS), True, BLACK)
    screen.blit(coins, (370, 10))

    # --- Draw all sprites and update their positions ---
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

        # If coin collected by player — move it to new position and update COINS
        if entity == C1:
            if pygame.sprite.spritecollideany(P1, coinss):
                entity.move()
        else:
            entity.move()

    # --- Make coins fall down like enemies (visual movement) ---
    for enemy in enemies:
        enemy.move()

    for coin in coinss:
        coin.rect.y += SPEED
        # Reset coin to top if it goes below screen
        if coin.rect.top > SCREEN_HEIGHT:
            coin.rect.y = -coin.rect.height
            coin.rect.x = random.randint(40, SCREEN_WIDTH - 40)

    # --- Update the screen ---
    pygame.display.update()
    FramePerSec.tick(FPS)
