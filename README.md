## Galaxy Racer
Galaxy Racer is a small game developed using Pygame, where you control a spaceship to avoid obstacles and collect boosters to increase speed.
### How to Play
* **Move the spaceship**: Use the `<-` and `->` keys to move the spaceship left or right.
* **Shoot bullets**: Press `Enter` to shoot bullets at obstacles.
* **Collect boosters**: Grab boosters to increase speed.
* **Avoid collisions**: The game ends if the spaceship collides with an obstacle.
### Installation
#### System Requirements
* Python3
* ``pygame`` library
#### Installation Steps
1. Install Python if not already installed:
```bash
https://www.python.org/downloads/
```
2. Install Pygame library:
```bash
pip install pygame
```
3. Clone or download the source code:
```bash
https://github.com/Dang-Hung-Thinh/game
```
4. Run the game:
```bash
py game.py
```
### Resources
* Images and sounds are located in the `images/` and `sounds/` directories.
* Main source file: `final2.py`
### Explanation
#### 1. Initialize Pygame and Setup
---
```python
import pygame
import random

pygame.init()
```
* Import `pygame` for game development
* Import `random` to generate random positions.
* Initialize Pygame
  
---
#### 2. Setup Game Window
```python
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Racer")
```
* Set the screen size to 800*600
* Create a game window
* Set the title "Galaxy Racer"
---
#### 3. Load Images & Sounds
```python
ship = pygame.image.load("images/ship.png")
ship = pygame.transform.rotate(ship, 0)  # Rotate the ship 0 degrees
obstacle_img = pygame.image.load("images/asteroid.png")
booster_img = pygame.image.load("images/boot.png")
background = pygame.image.load("images/bg.jpg")
```
* Load images for the spaceship, obstacles (asteroids), boosters, and background.
* `pygame.transform.rotate(ship,0)`: Rotates the ship (0 degrees means to change).
```python
crash_sound = pygame.mixer.Sound("sounds/explosion.ogg")
boost_sound = pygame.mixer.Sound("sounds/thrust.ogg")
pygame.mixer.music.load("sounds/game.ogg")
pygame.mixer.music.play(-1)
```
* Load and play sounds:
    * `crash_sound`: When the ship crashes
    * `boost_sound`: When collecting a booster.
    * `game.ogg`: Background music (looped infinitely `-1`).
---
#### 4. Game State Variables
```python
clock = pygame.time.Clock()
score = 0
speed = 5
game_over = False
```
* `clock`: Controls the game speed.
* `score`: Player's score.
* `speed`: Movement speed of obstacles.
* `game_over`: Tracks game over status.
---
#### 5. Player and Object Initialization
```python
ship_x = WIDTH // 2 - 25
ship_y = HEIGHT - 100

obstacles = []
boosters = []
bullets = []
```
* `ship_x`, `ship_y`: Initial position of the ship.
* `obstacles`: List of asteroids.
* `boosters`: List of boosters.
* `bullets`: List of bullets.
##### Generate Obstacles & Boosters
```python
for _ in range(5):
    obstacles.append([random.randint(50, WIDTH - 50), random.randint(-600, -50)])

for _ in range(2):
    boosters.append([random.randint(50, WIDTH - 50), random.randint(-600, -50)])
```
* Generate 5 asteroids at random positions.
* Generate 2 boosters at random positions.
---
#### 6. Game Loop
##### Draw Background
```python
screen.blit(background, (0,0))
```
* Display the background image.
#### Handle Events
```python
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
                bullets.append([ship_x + 25, ship_y])
```
* Exit game when clicking **QUIT**.
* When pressing **Enter**, the ship fires bullets:
  * `score <= 1000`: Fires 1 bullets.
  * `score >  1000`: Fires 2 bullets.
  * `score >  2000`: Fires 3 bullets.
##### Move the ship
```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] and ship_x > 50:
    ship_x -= 7
if keys[pygame.K_RIGHT] and ship_x < WIDTH - 50:
    ship_x += 7
```
* Move the ship **left** or **right**.
##### Move Bullets
```python
for bullet in bullets:
    bullet[1] -= 10  

bullets = [bullet for bullet in bullets if bullet[1] > 0]
```
* Bullets move **upward**.
* Remove bullets when they go off-screen.
##### Move Obstacles
```python
for obs in obstacles:
    obs[1] += speed
    if obs[1] > HEIGHT:
        obs[1] = random.randint(-600, -50)
        obs[0] = random.randint(50, WIDTH - 50)
```
* Assteroids move downward.
* if an asteroid moves off-screen, it respawns at the top.
##### Check Collision with Ship
```python
if abs(ship_x - obs[0]) < 50 and abs(ship_y - obs[1]) < 50:
    crash_sound.play()
    game_over = True
```
* If the ship collides with an asteroid → **Game Over**.
##### Check Bullet Collision with Obstacles
```python
for bullet in bullets[:]:
    for obs in obstacles[:]:
        if abs(bullet[0] - obs[0]) < 30 and abs(bullet[1] - obs[1]) < 30:
            obstacles.remove(obs)
            bullets.remove(bullet)
            crash_sound.play()
            score += 10
            break
```
* If a bullet hits an asteroid → Remove both and increase score.
##### Move Boosters & Check Collection
```python
for boost in boosters:
    boost[1] += speed
    if boost[1] > HEIGHT:
        boost[1] = random.randint(-600, -50)
        boost[0] = random.randint(50, WIDTH - 50)

    if abs(ship_x - boost[0]) < 50 and abs(ship_y - boost[1]) < 50:
        boost_sound.play()
        speed += 1
        boost[1] = random.randint(-600, -50)
        boost[0] = random.randint(50, WIDTH - 50)
```
* If the ship collects a booster → Increase speed.
##### Draw Bullets
```python
for bullet in bullets:
    pygame.draw.rect(screen, (255, 0, 0), (bullet[0], bullet[1], 5, 10))
```
* Draw red bullets.
##### Display Score
```python
score += 1
font = pygame.font.Font(None, 36)
text = font.render(f"Score: {score}", True, (255, 255, 0))
screen.blit(text, (10, 10))
```
* Update the score over time.
##### Handle Game Over
```python
if game_over:
    font = pygame.font.Font(None, 72)
    over_text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (WIDTH//2 - 150, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(3000)
    running = False
```
* Display **"GAME OVER"** and stop the game.
