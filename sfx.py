
import os
import random

import pygame

pygame.mixer.pre_init(44100, -16, 64, 512)
pygame.init()


class SFXManager:

    def __init__(self, path=f'data{os.sep}sfx', num_channels=96):
        self.path = path
        self.sounds = {}
        self.music = {}
        self.paused = False
        self.queue = []
        for file in os.listdir(f'{self.path}{os.sep}sounds'):
            if '.' not in file:
                self.sounds[file] = [pygame.mixer.Sound(f'{self.path}{os.sep}sounds{os.sep}{file}{os.sep}{sound}') for sound in os.listdir(f'{self.path}{os.sep}sounds{os.sep}{file}') if sound[0] != '.']
        for file in os.listdir(f'{self.path}{os.sep}music'):
            if '.' not in file:
                self.music[file] = [music for music in os.listdir(f'{self.path}{os.sep}music{os.sep}{file}') if music[0] != '.']
        self.num_channels = num_channels

    def play(self, name, loops=0, maxtime=0, fade_ms=0):
        try:
            random.choice(self.sounds[name]).play(loops, maxtime, fade_ms)
        except KeyError:
            pass

    def start_music(self):
        if self.queue:
            pygame.mixer.music.load(self.queue[0])
            pygame.mixer.music.play()

    def update(self):
        if pygame.mixer.music.get_busy() and not self.paused:
            if len(self.queue) > 1:
                del self.queue[0]
                pygame.mixer.music.load(self.queue[0])
            elif len(self.queue) == 1:
                del self.queue[0]

    def pause_music(self):
        pygame.mixer.music.pause()
        self.paused = True

    def unpause_music(self):
        pygame.mixer.music.unpause()
        self.paused = False

    def stop(self, name):
        for sound in self.sounds[name]:
            sound.stop()

    def new_sound(self, path):
        self.sounds[path] = [pygame.mixer.Sound(sound) for sound in os.listdir(path) if sound[0] != '.']

    def add_queue(self, music):
        self.queue.append(music)

    @staticmethod
    def stop_all():
        pygame.mixer.stop()

    @property
    def num_channels(self):
        return pygame.mixer.get_num_channels()

    @num_channels.setter
    def num_channels(self, num):
        pygame.mixer.set_num_channels(num)
