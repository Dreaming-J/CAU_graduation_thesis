import pygame


def play():
    pygame.mixer.init()
    pygame.mixer.music.load("./data/beep.mp3")
    pygame.mixer.music.play()
