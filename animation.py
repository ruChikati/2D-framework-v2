
import os

import pygame

import general_funcs as funcs


class FileTypeError(Exception):

    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f'{self.type} type files cannot be processed by the code'


class LengthError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Animation:

    def __init__(self, path):
        self.path = path
        self.frame_paths = os.listdir(self.path)
        self.frame = 0
        self.frame_paths.sort()
        self.rotation = 0
        self.paused = False
        try:
            self.config = funcs.read_json(f'{self.path}{os.sep}config.json')
        except FileNotFoundError:
            self.config = {'frames': [5] * len(self.frame_paths), 'speed': 1., 'loop': False, 'offset': [0, 0], 'centre': False}
            funcs.write_json(f'{self.path}{os.sep}config.json', self.config)
        self.frame_durations = funcs.sum_list(self.config['frames'])
        self.frames = []
        for frame in self.frame_paths:
            if frame.split('.')[-1] == 'png':
                frame = pygame.image.load(f'{self.path}{os.sep}{frame}').convert_alpha()
                frame.set_colorkey((1, 1, 1))
                self.frames.append(frame)
            elif frame.split('.')[-1] == 'json':
                pass
            else:
                raise FileTypeError(frame.split('.')[-1])
        if len(self.frames) > len(self.frame_paths) + 1:
            self.config['frames'] += [5] * (len(self.frames) - len(self.frame_paths))
        elif len(self.frames) < (len(self.frame_paths) - 1):
            raise LengthError('Not enough frames in animation')
        self._get_img()

    def _get_img(self):
        if len(self.frames) != len(self.frame_durations):
            raise LengthError('frame_durations does not have the same length as frames in ' + self.path + '\'s animation')
        for frame, t in zip(self.frames, self.frame_durations):
            if t > self.frame:
                self.img = frame
                break
        if self.frame_durations[-1] < self.frame:
            self.img = self.frames[-1]

    def render(self, surf, pos, offset=(0, 0)):
        pass

    def play(self, dt, fps=60):
        if not self.paused:
            self.frame += dt * fps * self.config['speed']
        if self.config['loop']:
            while self.frame > self.duration:
                self.frame -= self.duration
        self._get_img()

    def rewind(self, index=0):
        self.frame = index

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False

    @property
    def duration(self):
        return sum(self.config['frames'])


class AnimationManager:

    def __init__(self, path=f'data{os.sep}anims'):
        self.path = path
        self.anims = {}
        for directory in os.listdir(path):
            if directory[0] != '.':
                self.anims[directory] = Animation(f'{path}{os.sep}{directory}')

    def new(self, path):
        self.anims[path.split(os.sep)[-1]] = Animation(path)
