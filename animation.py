import pygame
import game
import player
from random import randint
import os

# permet de trouver l'ndroit où se trouve le fichier
current_path = os.path.dirname(os.path.abspath(__file__))

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        if sprite_name == 'tyler1' or sprite_name == 'jotaro':
            self.nb_repet_ulti = 3
        elif sprite_name == 'risitas':
            self.nb_repet_ulti = 2
        self.nb_ulti = 0

        if sprite_name == 'jotaro':
            self.nb_repet_attack = 3
        else:
            self.nb_repet_attack = 1
        self.nb_attack = 0

        self.current_image = 0
        self.current_image_dead = 0
        self.current_image_attack = 0
        self.current_image_ulti = 0

        self.player_animation = False
        self.player_dead_animation = False
        self.player_attack_animation = False
        self.player_ulti_animation = False

        self.images = animations.get(sprite_name)
        self.images_dead = animations_dead.get(sprite_name)
        self.images_attack = animations_attack.get(sprite_name)
        self.images_ulti = animations_ulti.get(sprite_name)
        
        self.image = pygame.image.load(current_path + f'/assets/{sprite_name}.png')

    def animate(self):
        self.current_image += 1

        if self.current_image >= len(self.images):
            self.current_image = 0
        
        self.image = self.images[self.current_image]
        if self.animation_sens == 1:
            self.image = pygame.transform.flip(self.image, 1, 0)

    def dead_animate(self):
        self.game.tour_j1 = ''
        self.current_image_dead += 1

        if self.current_image_dead >= len(self.images_dead):
            self.game.game_over()
            self.current_image_dead = 0
        
        self.image = self.images_dead[self.current_image_dead]
        if self.animation_dead_sens == 1:
            self.image = pygame.transform.flip(self.image, 1, 0)

    def attack_animate(self):
        self.game.tour_j1 = ''
        self.current_image_attack += 1

        if self.current_image_attack >= len(self.images_attack):
            self.current_image_attack = 0
            self.nb_attack += 1
        
        if self.nb_attack == self.nb_repet_attack:
            self.player_attack_animation = False
            self.game.a_qui_le_tour()
            if self.game.tour_j2 == True:
                self.game.player1.special_player(self.game.player2)
            elif self.game.tour_j2 == False:
                self.game.player2.special_player(self.game.player1)
            self.nb_attack = 0
            
        self.image = self.images_attack[self.current_image_attack]

        if self.animation_attack_sens == 1:
            self.image = pygame.transform.flip(self.image, 1, 0)

    def ulti_animate(self):
        self.game.tour_j1 = ''
        self.current_image_ulti += 1

        if self.current_image_ulti >= len(self.images_ulti):
            self.current_image_ulti = 0
            self.nb_ulti += 1
        
        if self.nb_ulti == self.nb_repet_ulti:   
            self.player_ulti_animation = False
            self.game.a_qui_le_tour()
            if self.game.tour_j2 == True:
                self.game.player1.ultimate()
            elif self.game.tour_j2 == False:
                self.game.player2.ultimate()
            self.nb_ulti = 0
        
        self.image = self.images_ulti[self.current_image_ulti]
        if self.animation_ulti_sens == 1:
            self.image = pygame.transform.flip(self.image, 1, 0)

def load_animation_images(sprite_name):
    images = []
    
    path = current_path + f'/assets/{sprite_name}/{sprite_name}'
    
    for num in range(1, 1):
        image_path = path + " (" + str(num) + ').gif'
        image_load = pygame.image.load(image_path)
        image_transform = pygame.transform.scale(image_load, (400, 300))
        images.append(image_transform)

    return images

def load_dead_animation_images(sprite_name):
    images_dead = []

    if sprite_name == 'tyler1':
        i = 74
    elif sprite_name == 'sardoche':
        i = 172
    elif sprite_name == 'risitas':
        i = 43
    
    path = current_path + f'/assets/{sprite_name}_dead/{sprite_name}_dead'
    
    for num in range(1, i):
        image_path = path + " (" + str(num) + ').gif'
        image_load = pygame.image.load(image_path)
        image_transform = pygame.transform.scale(image_load, (400, 300))
        images_dead.append(image_transform)

    return images_dead

def load_attack_animation_images(sprite_name):
    images_attack = []
    
    path = current_path + f'/assets/{sprite_name}_attack/{sprite_name}_attack'

    if sprite_name == 'tyler1':
        i = 137
    elif sprite_name == 'jotaro':
        i = 10
    
    for num in range(1, i):
        image_path = path + " (" + str(num) + ').gif'
        image_load = pygame.image.load(image_path)
        image_transform = pygame.transform.scale(image_load, (400, 300))
        images_attack.append(image_transform)

    return images_attack

def load_ulti_animation_images(sprite_name):
    images_ulti = []
    
    path = current_path + f'/assets/{sprite_name}_ulti/{sprite_name}_ulti'

    if sprite_name == 'jotaro':
        i = 40
    elif sprite_name == 'tyler1':
        i = 84
    elif sprite_name == 'risitas':
        i = 57
    
    for num in range(1, i):
        image_path = path + " (" + str(num) + ').gif'
        image_load = pygame.image.load(image_path)
        image_transform = pygame.transform.scale(image_load, (400, 300))
        images_ulti.append(image_transform)

    return images_ulti

animations = {
}

animations_dead = {
    'tyler1': load_dead_animation_images('tyler1'),
    'sardoche': load_dead_animation_images('sardoche'),
    'risitas': load_dead_animation_images('risitas')
}

animations_attack = {
    'tyler1': load_attack_animation_images('tyler1'),
    'jotaro': load_attack_animation_images('jotaro')
}

animations_ulti = {
    'jotaro': load_ulti_animation_images('jotaro'),
    'tyler1': load_ulti_animation_images('tyler1'),
    'risitas': load_ulti_animation_images('risitas')
}