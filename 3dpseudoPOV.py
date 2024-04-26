import pygame
import sys
import math

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 32
FOV = math.pi / 3
HALF_WIDTH = WINDOW_WIDTH // 2
HALF_HEIGHT = WINDOW_HEIGHT // 2
PLAYER_SPEED = 0.30
ROTATION_SPEED = 0.05
MAP_WIDTH = 10
MAP_HEIGHT = 10
MAP = [
    "##########",
    "#......#.#",
    "#.######.#",
    "#........#",
    "##########",
]

# Colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("3D First Person Perspective")

# Player class
class Player:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def rotate(self, angle):
        self.angle += angle

    def move(self, distance, walls):
        dx = math.cos(self.angle) * distance
        dy = math.sin(self.angle) * distance
        new_x = self.x + dx
        new_y = self.y + dy
        if not self.is_wall(new_x, new_y, walls):
            self.x = new_x
            self.y = new_y

    def cast_ray(self, angle, walls):
        x, y = self.x, self.y
        dx = math.cos(angle)
        dy = math.sin(angle)
        max_distance = 255
        while True:
            x += dx
            y += dy
            if self.is_wall(int(x), int(y), walls):
                distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
                wall_height = WINDOW_HEIGHT / (distance * math.cos(self.angle - angle))
                return min(int(distance), max_distance), BLUE, min(wall_height, WINDOW_HEIGHT)

    def is_wall(self, x, y, walls):
        return walls[int(y // TILE_SIZE)][int(x // TILE_SIZE)] == '#'


# Main function
def main():
    player = Player(100, 100, 0)
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.rotate(-ROTATION_SPEED)
        if keys[pygame.K_RIGHT]:
            player.rotate(ROTATION_SPEED)
        if keys[pygame.K_UP]:
            player.move(PLAYER_SPEED, MAP)
        if keys[pygame.K_DOWN]:
            player.move(-PLAYER_SPEED, MAP)

        window.fill(GRAY)

        for x in range(WINDOW_WIDTH):
            angle = player.angle - FOV / 2 + x * FOV / WINDOW_WIDTH
            distance, color, wall_height = player.cast_ray(angle, MAP)
            pygame.draw.rect(window, color, (x, HALF_HEIGHT - wall_height / 2, 1, wall_height))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
