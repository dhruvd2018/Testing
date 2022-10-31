import pygame
from pygame.locals import *;
from sys import exit;
from random import randint;
from math import sqrt;
from math import atan2;
from math import degrees;
from math import pi;
from math import sin;
from math import cos;
from math import floor;
from math import ceil;
from math import fabs;
from math import pow;
from math import exp;
from math import log;
from math import log10;
from math import log2;
from math import fmod;
from math import hypot;
from math import degrees;
from math import radians;
from math import copysign;
from math import isinf;
from math import isnan;
from math import trunc;
from math import factorial;
from math import gcd;
from math import lcm;
pygame.init();
pygame.display.set_caption("Pong");
screen = pygame.display.set_mode((800, 600), 0, 32);
clock = pygame.time.Clock();
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
# Path: Game.py
class Ball(pygame.sprite.Sprite):
    def __init__(self, speed, angle, position):
        pygame.sprite.Sprite.__init__(self);
        self.image = pygame.Surface((10, 10));
        self.image.fill((255, 255, 255));
        self.rect = self.image.get_rect();
        self.rect.center = position;
        self.speed = speed;
        self.angle = angle;
        self.x = position[0];
        self.y = position[1];
        self.direction = [cos(radians(angle)), sin(radians(angle))];
    def update(self):
        self.x += self.direction[0] * self.speed;
        self.y += self.direction[1] * self.speed;
        self.rect.center = (self.x, self.y);
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.direction[0] *= -1;
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.direction[1] *= -1;
    def collide(self, other):
        if self.rect.colliderect(other.rect):
            self.direction[1] *= -1;
# Path: Game.py
class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self);
        self.image = pygame.Surface((100, 10));
        self.image.fill((255, 255, 255));
        self.rect = self.image.get_rect();
        self.rect.center = position;
    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0];
        if self.rect.left <= 0:
            self.rect.left = 0;
        if self.rect.right >= 800:
            self.rect.right = 800;
# Path: Game.py
ball = Ball(6, 45, (400, 300));
player = Player((400, 580));
ball_group = pygame.sprite.Group();
ball_group.add(ball);
player_group = pygame.sprite.Group();
player_group.add(player);
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
            exit();
    screen.fill((0, 0, 0));
    ball_group.update();
    player_group.update();
    ball_group.draw(screen);
    player_group.draw(screen);
    ball.collide(player);
    pygame.display.update();
    clock.tick(60);
    