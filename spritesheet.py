import pygame as pg
from math import floor


class SpriteSheet:

    def __init__(self, sheet: pg.Surface, image_size: tuple[int, int], delay=240, speed=240):
        self.sheet = sheet
        self.image_size = image_size
        self.images = []
        self.frame = 0
        self.time = 0
        self.delay = delay
        self.speed = speed

        for i in range(floor(self.sheet.get_width() / image_size[0])):
            image = pg.Surface(self.image_size, pg.SRCALPHA)
            image.blit(self.sheet, (0, 0), pg.Rect((i * self.image_size[0], 0), self.image_size))
            self.images.append(image)

        self.total_frames = len(self.images)
        self.image = self.images[0]

    def get_frame(self) -> pg.Surface:
        self.time += 1
        if self.time == self.speed:
            self.image = self.images[self.frame]
            self.frame += 1
            self.time = 0

            if self.frame == self.total_frames:
                self.frame = 0

        return self.image

    def get_frame_number(self) -> int:
        return self.frame
