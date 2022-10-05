import imp
import pygame
from player import *
from sound import SoundManager
import os

path = os.path.dirname(os.path.abspath(__file__))

# seconde class qui va représenter le jeu
class Game:

    def __init__(self):
        self.is_playing = False
        self.tour_j1 = True
        self.tour_j2 = False
        self.text1 = ""
        self.text2 = ""
        self.sound_manager = SoundManager()
        self.font = pygame.font.Font(path + '/assets/my_custom_font.ttf', 25)

    def a_qui_le_tour(self):
        if self.tour_j2 == True:
            self.tour_j1 = False
        elif self.tour_j2 == False:
            self.tour_j1 = True

    def update(self, screen, player, sprite_name):
        if player.player_dead_animation:
            player.update_dead_animation()
        elif player.player_attack_animation:
            player.update_attack_animation()
        elif player.player_ulti_animation:
            player.update_ulti_animation()
        elif player.player_animation:
            player.update_animation()
        else:
            player.image = pygame.image.load(path + f'/assets/{sprite_name}.png')
            if player.image_sens == 1:
                player.image = pygame.transform.flip(player.image, 1, 0)
        # appliquer l'image de mon joueur
        screen.blit(player.image, player.rect)

        # actualiser la barre de vie et de ki du joueur
        player.update_health_bar(screen)
        player.update_ki_bar(screen)

    def play_sound(self, name_sound):
        self.sound_manager.play(name_sound)

    def update_text(self, screen, x, player, text):
        # afficher le texte sur l'écran
        text = self.font.render("Tour joueur " + x + " (" + text + "): ", 1, (255, 255, 255))
        screen.blit(text, (20, 20))
        text1 = self.font.render("Attaque : " + str(player.get_attack()) + " / 20 ki", 1, (255, 255, 255))
        screen.blit(text1, (20, 60))
        text2 = self.font.render("Recharger ki : +50 ki", 1, (255, 255, 255))
        screen.blit(text2, (20, 90))
        text3 = self.font.render("Attaque Spécial : " + str(player.get_attack()*2.5) + " / 150 ki", 1, (255, 255, 255))
        screen.blit(text3, (20, 120))
        text4 = self.font.render(player.ulti_text, 1, (255, 255, 255))
        screen.blit(text4, (20, 150))

    def text_action(self, screen, texte):
        text = self.font.render(texte, 1, (255, 255, 255))
        screen.blit(text, (420, 230))

    def update_text_action(self, screen, action, j, player):
        if player.critique:
            text = self.font.render("Coup critique !", 1, (255, 255, 255))
            screen.blit(text, (420, 260))
        elif player.esquive:
            text = self.font.render("Vous avez esquivé l'attaque !", 1, (255, 255, 255))
            screen.blit(text, (420, 260))
        
        if action == 'attack':
            self.text_action(screen, j + " vous a attaqué")
        elif action == 'recover_ki':
            self.text_action(screen, j + " a rechargé son ki")
        elif action == 'special':
            self.text_action(screen, j + " vous a fait une attaque spécial")
        elif action == 'soin':
            self.text_action(screen, j + " s'est soigné")
        elif action == 'peur':
            self.text_action(screen, j + " a réduis votre attaque")
        elif action == 'boost':
            self.text_action(screen, j + " a augmenté son attaque")
        elif action == 'transfo':
            self.text_action(screen, j + " s'est transformé")

    def update_choix(self, screen, i):
        text = self.font.render("Joueur " + i + " choisis un personnage (écrit): ", 1, (255, 255, 255))
        screen.blit(text, (20, 20))
        text = self.font.render("- Tyler1", 1, (255, 255, 255))
        screen.blit(text, (20, 60))
        text = self.font.render("- Bob E", 1, (255, 255, 255))
        screen.blit(text, (20, 90))
        text = self.font.render("- Sardoche", 1, (255, 255, 255))
        screen.blit(text, (20, 120))
        text = self.font.render("- Bob R", 1, (255, 255, 255))
        screen.blit(text, (20, 150))
        text = self.font.render("- Jotaro", 1, (255, 255, 255))
        screen.blit(text, (20, 180))
        text = self.font.render("- Risitas", 1, (255, 255, 255))
        screen.blit(text, (20, 210))

    def game_over(self):
        self.is_playing = False

    def screen_game_over(self, screen, i):
        font = pygame.font.Font(path + '/assets/my_custom_font.ttf', 70) 
        text = font.render("Joueur " + i + " vainqueur ! ", 1, (255, 255, 255))
        screen.blit(text, (200, 200))