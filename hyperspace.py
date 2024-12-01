import pygame as pg
import random
import math
from settings import *

vec2, vec3 = pg.math.Vector2, pg.math.Vector3

RES = WIDTH, HEIGHT
NUM_STARS = 1000
CENTER = vec2(WIDTH // 2, HEIGHT // 2)
COLORS = 'blue cyan navy white magenta lime gold'.split()
Z_DISTANCE = 40
ALPHA = 200


class Star:
    def __init__(self, app):
        self.screen = WIN
        self.pos3d = self.get_pos3d()
        self.vel = random.uniform(0.05, 0.25)
        self.color = random.choice(COLORS)
        self.screen_pos = vec2(0, 0)
        self.size = 10

    def get_pos3d(self, scale_pos=35):
        angle = random.uniform(0, 2 * math.pi)
        radius = random.randrange(HEIGHT // scale_pos, HEIGHT) * scale_pos
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        return vec3(x, y, Z_DISTANCE)

    def update(self):
        self.pos3d.z -= self.vel
        self.pos3d = self.get_pos3d() if self.pos3d.z < 1 else self.pos3d

        self.screen_pos = vec2(self.pos3d.x, self.pos3d.y) / self.pos3d.z + CENTER
        self.size = (Z_DISTANCE - self.pos3d.z) / (0.2 * self.pos3d.z)
        # rotate xy
        self.pos3d.xy = self.pos3d.xy.rotate(0.3)

    def draw(self):
        s = self.size
        if (-s < self.screen_pos.x < WIDTH + s) and (-s < self.screen_pos.y < HEIGHT + s):
            pg.draw.rect(self.screen, self.color, (*self.screen_pos, self.size, self.size))


class Starfield:
    def __init__(self, app):
        self.stars = [Star(app) for i in range(NUM_STARS)]

    def run(self):
        [star.update() for star in self.stars]
        self.stars.sort(key=lambda star: star.pos3d.z, reverse=True)
        [star.draw() for star in self.stars]

