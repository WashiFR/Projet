import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'ayhelp': pygame.mixer.Sound('Projet/assets/sounds/ayhelp.ogg'),
            'ctsur': pygame.mixer.Sound('Projet/assets/sounds/ctsur.ogg'),
            'punchair': pygame.mixer.Sound('Projet/assets/sounds/punchair.ogg'),
            'yesyes': pygame.mixer.Sound('Projet/assets/sounds/yesyes.ogg'),
            'oraora': pygame.mixer.Sound('Projet/assets/sounds/oraora.ogg'),
            'issou': pygame.mixer.Sound('Projet/assets/sounds/issou.ogg')
        }

    def play(self, name):
        self.sounds[name].play()
