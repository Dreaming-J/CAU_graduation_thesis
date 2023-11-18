import pygame


def play(name="beep"):
    pygame.mixer.init()
    pygame.mixer.music.load("./data/{}.mp3".format(name))
    pygame.mixer.music.play()
