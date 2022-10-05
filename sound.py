import imp
import pygame
import os

path = os.path.dirname(os.path.abspath(__file__))

class SoundManager:

    def __init__(self):
        self.sounds = {
            'ayhelp': pygame.mixer.Sound(path + '/assets/sounds/ayhelp.ogg'),
            'ctsur': pygame.mixer.Sound(path + '/assets/sounds/ctsur.ogg'),
            'punchair': pygame.mixer.Sound(path + '/assets/sounds/punchair.ogg'),
            'yesyes': pygame.mixer.Sound(path + '/assets/sounds/yesyes.ogg'),
            'oraora': pygame.mixer.Sound(path + '/assets/sounds/oraora.ogg'),
            'issou': pygame.mixer.Sound(path + '/assets/sounds/issou.ogg')
        }

    def play(self, name):
        self.sounds[name].play()