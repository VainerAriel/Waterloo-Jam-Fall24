from settings import *


class Animation:
    def __init__(self, fs, arr, type):
        self.frame = 0
        self.frame_speed = fs
        self.count_frames = fs
        self.image_arr = arr
        self.type = type
        self.finished_anim = False
        self.run_anim = True if type == 0 else False

    def draw(self, display, pos, direc):
        display.blit(self.image_arr[0 if direc == 1 else 1][self.frame], pos)

    def update(self, half=0):
        if self.run_anim:
            self.count_frames -= 1
            if self.count_frames == 0:
                self.count_frames = self.frame_speed
                if self.type == 0:
                    self.frame = (self.frame + 1) % len(self.image_arr)
                else:
                    if self.frame < (len(self.image_arr) - 1)//2 if half == 1 else (len(self.image_arr) - 1):
                        self.frame += 1


    def start(self):
        self.run_anim = True

    def reset(self):
        self.run_anim = False
        self.finished_anim = False
        self.frame = 0
