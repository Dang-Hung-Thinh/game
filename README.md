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

