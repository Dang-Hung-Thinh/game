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
```python
import pygame
import random

pygame.init()
```
* Import `pygame` for game development
* Import `random` to generate random positions.
* Initialize Pygame
  
  ---

