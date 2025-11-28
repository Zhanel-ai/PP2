import pygame
import sys
import random
import psycopg2

pygame.init()

# --- ЭКРАН ---
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

BLACK, WHITE, GREEN, RED, ORANGE = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0), (255, 165, 0)

# --- ЗМЕЙКА ---
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [10, 0]

# --- ЕДА ---
food = {'pos': [0, 0], 'weight': 1, 'spawn_time': 0}
food_spawn = True
food_counter = 0

# --- ПРОГРЕСС ---
score = 0
level = 1
paused = False

fps = pygame.time.Clock()

# ================================
#     БАЗА ДАННЫХ
# ================================
def connect_db():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres", 
        user="zhanel",      
        password=""            
    )


def get_or_create_user(username):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return user_id


def get_last_progress(user_id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT score, level
        FROM user_score
        WHERE user_id = %s
        ORDER BY id DESC LIMIT 1
    """, (user_id,))

    row = cur.fetchone()
    cur.close()
    conn.close()

    return row if row else (0, 1)


def save_progress(user_id, score, level):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO user_score (user_id, score, level)
        VALUES (%s, %s, %s)
    """, (user_id, score, level))

    conn.commit()
    cur.close()
    conn.close()

    print(f"[SAVED] user={user_id} score={score} level={level}")


# ================================
#     ЛОГИКА ИГРЫ
# ================================
def check_collision(pos):
    x, y = pos
    # Столкновение с границами
    if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
        return True
    # Столкновение с собой
    if pos in snake_pos[1:]:
        return True
    return False


def get_random_food():
    """Создание еды"""
    global food_counter

    while True:
        pos = [
            random.randrange(0, SCREEN_WIDTH // 10) * 10,
            random.randrange(0, SCREEN_HEIGHT // 10) * 10
        ]

        if pos not in snake_pos:
            weight = 2 if food_counter >= 2 else 1
            food_counter = 0 if weight == 2 else food_counter + 1
            return {'pos': pos, 'weight': weight, 'spawn_time': pygame.time.get_ticks()}


# ================================
#       СТАРТ ИГРЫ
# ================================
player_name = input("Enter your name: ").strip()
player_id = get_or_create_user(player_name)

score, level = get_last_progress(player_id)
print(f"Welcome, {player_name}! Continuing from Level {level}, Score {score}.")

# Основной цикл
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(player_id, score, level)
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_speed[1] == 0:
                    snake_speed = [0, -10]
                elif event.key == pygame.K_DOWN and snake_speed[1] == 0:
                    snake_speed = [0, 10]
                elif event.key == pygame.K_LEFT and snake_speed[0] == 0:
                    snake_speed = [-10, 0]
                elif event.key == pygame.K_RIGHT and snake_speed[0] == 0:
                    snake_speed = [10, 0]
                elif event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        save_progress(player_id, score, level)

        if not paused:
            new_head = [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]]
            snake_pos.insert(0, new_head)

            if check_collision(new_head):
                save_progress(player_id, score, level)
                pygame.quit()
                sys.exit()

            if new_head == food['pos']:
                score += food['weight']
                if score % 5 == 0:
                    level += 1
                food_spawn = True
            else:
                snake_pos.pop()

            if food_spawn:
                food = get_random_food()
                food_spawn = False

            if pygame.time.get_ticks() - food['spawn_time'] > 10000:
                food_spawn = True

        # ----- РЕНДЕР -----
        screen.fill(BLACK)

        for pos in snake_pos:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

        food_color = RED if food['weight'] == 1 else ORANGE
        pygame.draw.rect(screen, food_color, pygame.Rect(food['pos'][0], food['pos'][1], 10, 10))

        font = pygame.font.SysFont('arial', 20)
        screen.blit(font.render(f"Score: {score}  Level: {level}", True, WHITE), [5, 5])

        if paused:
            screen.blit(font.render("PAUSED", True, WHITE),
                        [SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2])

        pygame.display.flip()
        fps.tick(10 + level)

except SystemExit:
    pygame.quit()