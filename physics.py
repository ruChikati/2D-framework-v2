
from general_funcs import Vector2


class VerletObject:

    def __init__(self, curr_pos: Vector2, prev_pos: Vector2, accel: Vector2):
        self.pos = curr_pos
        self.prev_pos = prev_pos
        self.accel = accel

    def update(self, dt: float):
        vel = self.pos - self.prev_pos
        self.prev_pos = self.pos
        self.pos += vel + self.accel * dt * dt
        self.accel = Vector2(0, 0)

    def accelerate(self, acc: Vector2):
        self.accel += acc


class PhysicsSolver:

    gravity = Vector2(0, 10)

    def __init__(self, objects: list[VerletObject] | tuple[VerletObject]):
        self.objs = objects

    def update(self, dt: float):
        for obj in self.objs:
            obj.accelerate(PhysicsSolver.gravity)
            obj.update(dt)
