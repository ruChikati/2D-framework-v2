
import os

import pygame

import general_funcs as funcs


class Font:

    def __init__(self, file, bar_colour=(128, 128, 128), colourkey=(0, 0, 0)):
        self.fnt_img = pygame.image.load(file).convert()
        self.fnt_img.set_colorkey(colourkey)
        self.bar_colour = bar_colour
        self.imgs = []
        self.dist = [0]
        for i in range(self.fnt_img.get_width()):
            if self.fnt_img.get_at((i, 0)) == self.bar_colour:
                self.dist.append(i)

        for i in range(len(self.dist)):
            if i:
                img = funcs.clip(self.fnt_img, self.dist[i - 1], 0, self.dist[i] - self.dist[i - 1], self.fnt_img.get_height())
                img.set_colorkey(colourkey)
                self.imgs.append(img)

        self.chars = {char: img for char, img in zip(['!', ',', '-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], self.imgs)}
        self.chars[' '] = pygame.Surface((5, self.fnt_img.get_height()))

    def __getitem__(self, text):
        num_lines = 1
        if not isinstance(text, str):
            raise TypeError('font can only take strings as text')
        imgs = []
        for char in text:
            if char not in ['\n', ' ', '!', ',', '-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                raise TypeError('text contains invalid character: ' + char)
            if char == '\n':
                num_lines += 1
            else:
                imgs.append([self.chars[char], num_lines])

        return_img = pygame.Surface((sum(img[0].get_width() for img in imgs), max(img[0].get_height() for img in imgs) * num_lines))
        x = 0
        for img in imgs:
            return_img.blit(img[0], (x, -img[0].get_height() + img[0].get_height() * img[1]))
            x += img[0].get_width()
        return return_img

    def render(self, text):
        num_lines = 1
        if not isinstance(text, str):
            raise TypeError('font can only take strings as text')
        imgs = []
        for char in text:
            if char not in ['\n', ' ', '!', ',', '-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';',
                            '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                raise TypeError('text contains invalid character: ' + char)
            if char == '\n':
                num_lines += 1
            else:
                imgs.append([self.chars[char], num_lines])

        return_img = pygame.Surface(
            (sum(img[0].get_width() for img in imgs), max(img[0].get_height() for img in imgs) * num_lines))
        x = 0
        for img in imgs:
            return_img.blit(img[0], (x, -img[0].get_height() + img[0].get_height() * img[1]))
            x += img[0].get_width()
        return return_img


SysFont = pygame.font.SysFont


class FontManager:

    def __init__(self, path=f'data{os.sep}fonts', bar_colour=(128, 128, 128), colourkey=(0, 0, 0)):
        self.path = path
        self.fonts = {file.split('.')[0]: Font(path + os.sep + file, bar_colour, colourkey) for file in os.listdir(path) if file[0] != '.'}

    def __getitem__(self, item):
        return self.fonts[item]
