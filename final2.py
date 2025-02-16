import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Racer")

# Load hình ảnh
ship = pygame.image.load("images/ship.png")
ship = pygame.transform.rotate(ship, 0)  # Xoay tàu về 0 độ
obstacle_img = pygame.image.load("images/asteroid.png")
booster_img = pygame.image.load("images/boot.png")
background = pygame.image.load("images/bg.jpg")

# Âm thanh
crash_sound = pygame.mixer.Sound("sounds/explosion.ogg")
boost_sound = pygame.mixer.Sound("sounds/thrust.ogg")
pygame.mixer.music.load("sounds/game.ogg")
pygame.mixer.music.play(-1)

# Cấu hình game
clock = pygame.time.Clock()
score = 0
speed = 5
game_over = False

# Vị trí ban đầu của tàu
ship_x = WIDTH // 2 - 25
ship_y = HEIGHT - 100

# Danh sách chướng ngại vật & boosters
obstacles = []
boosters = []
bullets = []

# Hàm tạo chướng ngại vật
for _ in range(5):
    obstacles.append([random.randint(50, WIDTH - 50), random.randint(-600, -50)])

for _ in range(2):
    boosters.append([random.randint(50, WIDTH - 50), random.randint(-600, -50)])

# Game Loop
running = True
while running:
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if score > 2000:
                    bullets.append([ship_x + 10, ship_y])
                    bullets.append([ship_x + 25, ship_y])
                    bullets.append([ship_x + 40, ship_y])
                elif score > 1000:
                    bullets.append([ship_x + 15, ship_y])
                    bullets.append([ship_x + 35, ship_y])
                else:
                    bullets.append([ship_x + 25, ship_y])  # Bắn đạn từ vị trí tàu
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_x > 50:
        ship_x -= 7
    if keys[pygame.K_RIGHT] and ship_x < WIDTH - 50:
        ship_x += 7
    
    # Di chuyển đạn
    for bullet in bullets:
        bullet[1] -= 10  # Đạn bay lên trên
    
    bullets = [bullet for bullet in bullets if bullet[1] > 0]  # Xóa đạn khi ra khỏi màn hình
    
    # Di chuyển chướng ngại vật
    for obs in obstacles:
        obs[1] += speed
        if obs[1] > HEIGHT:
            obs[1] = random.randint(-600, -50)
            obs[0] = random.randint(50, WIDTH - 50)
        screen.blit(obstacle_img, (obs[0], obs[1]))
        
        # Kiểm tra va chạm
        if abs(ship_x - obs[0]) < 50 and abs(ship_y - obs[1]) < 50:
            crash_sound.play()
            game_over = True
    
    # Kiểm tra đạn va chạm mục tiêu
    for bullet in bullets[:]:
        for obs in obstacles[:]:
            if abs(bullet[0] - obs[0]) < 30 and abs(bullet[1] - obs[1]) < 30:
                obstacles.remove(obs)
                bullets.remove(bullet)
                crash_sound.play()
                score += 10
                break
    
    # Di chuyển boosters
    for boost in boosters:
        boost[1] += speed
        if boost[1] > HEIGHT:
            boost[1] = random.randint(-600, -50)
            boost[0] = random.randint(50, WIDTH - 50)
        screen.blit(booster_img, (boost[0], boost[1]))
        
        # Kiểm tra ăn booster
        if abs(ship_x - boost[0]) < 50 and abs(ship_y - boost[1]) < 50:
            boost_sound.play()
            speed += 1
            boost[1] = random.randint(-600, -50)
            boost[0] = random.randint(50, WIDTH - 50)
    
    # Hiển thị tàu
    screen.blit(ship, (ship_x, ship_y))
    
    # Hiển thị đạn
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 0, 0), (bullet[0], bullet[1], 5, 10))
    
    # Hiển thị điểm số
    score += 1
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 0))
    screen.blit(text, (10, 10))
    
    # Kiểm tra game over
    if game_over:
        font = pygame.font.Font(None, 72)
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (WIDTH//2 - 150, HEIGHT//2))
        pygame.display.update()
        pygame.time.delay(3000)
        running = False
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
