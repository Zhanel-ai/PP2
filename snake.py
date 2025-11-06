import pygame, sys, copy, random, time

# Initializing
pygame.init()
scale = 15
score, level, SPEED = 0, 0, 10
food_x, food_y = 10, 10

# Display setup
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Colors
snake_colour = (255, 137, 0)
snake_head = (255, 247, 0)
food_colour = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
font_colour = (255, 255, 255)
defeat_colour = (255, 0, 0)
background_top = (0, 0, 50)
background_bottom = (0, 0, 0)

class Snake:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.w, self.h = scale, scale
        self.x_dir, self.y_dir = 1, 0
        self.history = [[x, y]]
        self.length = 1

    def reset(self):
        self.__init__(250 - scale, 250 - scale)

    def show(self):
        for i in range(self.length):
            color = snake_head if i == 0 else snake_colour
            pygame.draw.rect(display, color, (*self.history[i], self.w, self.h))

    def check_eaten(self):
        # (3) Snake eats food → score increases
        return abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale

    def check_level(self):
        # (3) Level up condition (every 3)
        return self.length % 3 == 0

    def grow(self):
        self.length += 1
        self.history.append(self.history[-1])

    def death(self):
        # (1) Collision with itself
        for i in range(1, self.length):
            if self.history[0] == self.history[i] and self.length > 2:
                return True

    def update(self):
        # Movement
        for i in range(self.length - 1, 0, -1):
            self.history[i] = copy.deepcopy(self.history[i - 1])
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale

class Food:
    def new_location(self):
        # (2) Generate random food position
        global food_x, food_y
        food_x = random.randint(1, 33) * scale
        food_y = random.randint(1, 33) * scale

    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))

def show_text(text, x, y, size=20, color=font_colour):
    # (5) Show score and level counters
    font = pygame.font.SysFont(None, size)
    render = font.render(text, True, color)
    display.blit(render, (x, y))

def gameLoop():
    global score, level, SPEED
    snake = Snake(250, 250)
    food = Food()
    food.new_location()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_q):
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if snake.y_dir == 0:
                    if e.key == pygame.K_UP: snake.x_dir, snake.y_dir = 0, -1
                    if e.key == pygame.K_DOWN: snake.x_dir, snake.y_dir = 0, 1
                elif snake.x_dir == 0:
                    if e.key == pygame.K_LEFT: snake.x_dir, snake.y_dir = -1, 0
                    if e.key == pygame.K_RIGHT: snake.x_dir, snake.y_dir = 1, 0

        # Background gradient
        for y in range(500):
            c = [background_top[i] + (background_bottom[i] - background_top[i]) * y / 500 for i in range(3)]
            pygame.draw.line(display, c, (0, y), (500, y))

        snake.show()
        snake.update()
        food.show()

        # (5) Display score and level
        show_text(f"Score: {score}", scale, scale)
        show_text(f"Level: {level}", 90 - scale, scale)

        # (3) Snake eats food and grows
        if snake.check_eaten():
            food.new_location()
            score += random.randint(1, 5)
            snake.grow()

        # (3,4) Level up and increase speed
        if snake.check_level():
            food.new_location()
            level += 1
            SPEED += 1
            snake.grow()

        # (1) Snake dies when touches itself
        if snake.death():
            score, level = 0, 0
            show_text("Game Over!", 50, 200, 100, defeat_colour)
            pygame.display.update()
            time.sleep(2)
            snake.reset()

        # (1) Border collision / leaving the playing area
        head = snake.history[0]
        if head[0] >= 500: head[0] = 0
        if head[0] < 0: head[0] = 500
        if head[1] >= 500: head[1] = 0
        if head[1] < 0: head[1] = 500

        pygame.display.update()
        clock.tick(SPEED)

gameLoop()