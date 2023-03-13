
import pygame

from general_funcs import Vector2
from physics import VerletObject


class Entity(VerletObject):

    def __init__(self, x, y, w, h, name, anims=None):
        super().__init__(Vector2(x, y), Vector2(x, y), Vector2(0, 0))
        self.w = w
        self.h = h
        self.anims = anims if anims is not None else {}
        self.rect = pygame.Rect(x, y, w, h)
        self.name = name
        self.action = 'idle'
        self.img = self.anims[self.action].play(1.)

    def update(self, dt):
        vel = self.pos - self.prev_pos
        self.prev_pos = self.pos
        self.pos += vel + self.accel * dt * dt
        self.accel = Vector2(0, 0)
        self.img = self.anims[self.action].play(dt)
