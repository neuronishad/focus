import pygame

pygame.init()


class MP3:

    def __init__(self, mp3):
        self._sound = pygame.mixer.Sound(mp3)
        self._sound.set_volume(0.5)

    def play(self):
        self._sound.play()

    def stop(self):
        self._sound.stop()
