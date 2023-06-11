import pygame
import json
import os
import time

pygame.mixer.init()

def voice(lines):
    blocks = os.listdir('audio')
    lines = lines.split(" ")

    check_blocks = lambda line: any(block.lower().startswith(line.lower()) for block in blocks)

    if all(check_blocks(line) for line in lines):
        for line in lines:
            for file in blocks:
                if file.lower().startswith(line.lower()):
                    pygame.mixer.music.load(f'audio/{file}')
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    break