import pygame
import animation
from random import randint

# créer une première class qui va représenter le joueur
class AllPlayer(animation.AnimateSprite):

    def __init__(self, game, name):
        super().__init__(name)
        self.rect = self.image.get_rect()
        self.name = name
        self.game = game
        self.critique = False
        self.chance_crit = 10
        self.esquive = False
        self.chance_esquive = 10
        self.have_animation_attack = False
        self.have_animation_dead = False
        self.pv = 100
        self.max_pv = 100
        self.ki = 100
        self.max_ki = 200
        self.attack = 20
        self.rect.y = 300
        self.font = pygame.font.Font('Projet/assets/my_custom_font.ttf', 10)

    def get_name(self):
        return self.name

    def get_pv(self):
        return self.pv

    def get_max_pv(self):
        return self.max_pv

    def get_ki(self):
        return self.ki

    def get_max_ki(self):
        return self.max_ki

    def get_chance_crit(self):
        return self.chance_crit

    def get_chance_esquive(self):
        return self.chance_esquive

    def get_attack(self):
        return self.attack
    
    def get_ulti_cost(self):
        return self.ulti_cost

    def damage(self, damage):
        self.pv -= damage

    def attack_player(self, target_player):
        esquive = randint(0, target_player.get_chance_esquive())
        critique = randint(0, target_player.get_chance_crit())
        if esquive == 1:
            self.esquive = True
        else:
            if critique == 1:
                self.critique = True
                target_player.damage(self.attack + 10)
            else:
                target_player.damage(self.attack)
        self.ki -= 20

    def special_player(self, target_player):
        critique = randint(0, target_player.get_chance_crit())
        if critique == 1:
            self.critique = True
            target_player.damage(self.attack * 2.5 + 10)
        else:
            target_player.damage(self.attack * 2.5)
        self.ki -= 150

    def attack_special_player(self, target_player):
        if self.have_animation_attack:
            esquive = randint(0, target_player.get_chance_esquive())
            if esquive == 1:
                self.ki -= 150
                self.esquive = True
            else:
                self.player_attack_animation = True
        
        elif self.have_animation_attack == False:
            esquive = randint(0, target_player.get_chance_esquive())
            if esquive == 1:
                self.ki -= 150
                self.esquive = True
            else:
                self.special_player(target_player)

    def recover_ki(self):
        self.ki += 50
        if self.ki > self.max_ki:
            self.ki = self.max_ki
    
    def update_animation(self):
        self.animate()

    def update_dead_animation(self):
        self.dead_animate()

    def update_attack_animation(self):
        self.attack_animate()

    def update_ulti_animation(self):
        self.ulti_animate()

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y - 15, 200, 10])
        if self.pv <= self.max_pv/5:
            pygame.draw.rect(surface, (215, 20, 20), [self.rect.x + 50, self.rect.y - 15, (self.pv/self.max_pv)*200, 10])
        elif self.pv <= self.max_pv/2:
            pygame.draw.rect(surface, (238, 111, 12), [self.rect.x + 50, self.rect.y - 15, (self.pv/self.max_pv)*200, 10])
        else:
            pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y - 15, (self.pv/self.max_pv)*200, 10])
        text = self.font.render(str(self.pv) + " / " + str(self.max_pv), 1, (255, 255, 255))
        surface.blit(text, (self.rect.x + 125, self.rect.y - 18))

    def update_ki_bar(self, surface):
        # dessiner notre barre de ki
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y - 5, 200, 10])
        pygame.draw.rect(surface, (0, 93, 255), [self.rect.x + 50, self.rect.y - 5, (self.ki/self.max_ki)*200, 10])
        text = self.font.render(str(self.ki) + " / " + str(self.max_ki), 1, (255, 255, 255))
        surface.blit(text, (self.rect.x + 125, self.rect.y - 8))

class BobEponge(AllPlayer):

    def __init__(self, game, x, image_sens, animation_sens, animations_attack_sens, animations_dead_sens, animations_ulti_sens):
        super().__init__(game, 'bob')
        self.rect.x = x # définir la position du joueur
        self.image_sens = image_sens
        self.animation_sens = animation_sens
        self.animation_attack_sens = animations_attack_sens
        self.animation_dead_sens = animations_dead_sens
        self.animation_ulti_sens = animations_ulti_sens
        self.pv_transfo = self.pv/self.max_pv*20
        self.ulti_text = "Transfo : si PV <= " + str(self.pv_transfo)
        self.ulti = "Transfo"

    def get_pv_transfo(self):
        return self.pv_transfo

    def transfo(self):
        self.name = 'bob_muscle'
        self.pv += 50
        self.ki += 100
        self.max_ki += 100
        self.attack += 10
        self.ulti_text = ""
        self.ulti = ""

class Tyler1(AllPlayer):

    def __init__(self, game, x, image_sens, animation_sens, animations_attack_sens, animations_dead_sens, animations_ulti_sens):
        super().__init__(game, "tyler1")
        self.chance_esquive = 0
        self.rect.x = x # définir la position du joueur
        self.image_sens = image_sens
        self.animation_sens = animation_sens
        self.animation_attack_sens = animations_attack_sens
        self.animation_dead_sens = animations_dead_sens
        self.animation_ulti_sens = animations_ulti_sens
        self.ulti_text = "AyHelp ! : +70 PV / 100 Ki"
        self.ulti = "Soin"
        self.ulti_cost = 100
        self.have_animation_attack = True
        self.have_animation_dead = True

    def soin(self):
        self.player_ulti_animation = True
        self.game.play_sound('ayhelp')

    def ultimate(self):
        self.pv += 70
        self.ki -= self.ulti_cost
        if self.pv > self.max_pv:
            self.pv = self.max_pv


class Sardoche(AllPlayer):

    def __init__(self, game, x, image_sens, animation_sens, animations_attack_sens, animations_dead_sens, animations_ulti_sens):
        super().__init__(game, 'sardoche')
        self.rect.x = x # définir la position du joueur
        self.image_sens = image_sens
        self.animation_sens = animation_sens
        self.animation_attack_sens = animations_attack_sens
        self.animation_dead_sens = animations_dead_sens
        self.animation_ulti_sens = animations_ulti_sens
        self.pv_transfo = self.pv/self.max_pv*20
        self.ulti_text = "Transfo : si PV <= " + str(self.pv_transfo)
        self.ulti = "Transfo"
        self.have_animation_dead = True

    def get_pv_transfo(self):
        return self.pv_transfo

    def transfo(self):
        self.name = 'sardoche_rage'
        if self.image_sens == 1:
            self.image_sens = 0
        else:
            self.image_sens = 1
        self.pv += 50
        self.ki += 100
        self.max_ki += 100
        self.attack += 10
        self.ulti_text = ""
        self.ulti = ""

class BobRazowski(AllPlayer):

    def __init__(self, game, x, image_sens, animation_sens, animations_attack_sens, animations_dead_sens, animations_ulti_sens):
        super().__init__(game, 'bob_razowski')
        self.rect.x = x # définir la position du joueur
        self.image_sens = image_sens
        self.animation_sens = animation_sens
        self.animation_attack_sens = animations_attack_sens
        self.animation_dead_sens = animations_dead_sens
        self.animation_ulti_sens = animations_ulti_sens
        self.ulti_text = "Peur : ennemie -5 d'attaque / 30 Ki"
        self.ulti = "Peur"
        self.ulti_cost = 30

    def peur(self, target_player):
        self.ki -= self.ulti_cost
        if target_player.attack > 10:
            target_player.attack -= 5

class Jotaro(AllPlayer):

    def __init__(self, game, x, image_sens, animation_sens, animations_attack_sens, animations_dead_sens, animations_ulti_sens):
        super().__init__(game, 'jotaro')
        self.rect.x = x # définir la position du joueur
        self.image_sens = image_sens
        self.animation_sens = animation_sens
        self.animation_attack_sens = animations_attack_sens
        self.animation_dead_sens = animations_dead_sens
        self.animation_ulti_sens = animations_ulti_sens
        self.ulti_text = "yes yes...YES ! : +5 attaque / 30 Ki"
        self.ulti = "Boost"
        self.ulti_cost = 30
        self.have_animation_attack = True

    def boost(self):
        self.player_ulti_animation = True
        self.game.play_sound('yesyes')

    def ultimate(self):
        self.attack += 5
        self.ki -= self.ulti_cost

class Risitas(AllPlayer):

    def __init__(self, game, x, image_sens, animation_sens, animations_attack_sens, animations_dead_sens, animations_ulti_sens):
        super().__init__(game, 'risitas')
        self.rect.x = x # définir la position du joueur
        self.image_sens = image_sens
        self.animation_sens = animation_sens
        self.animation_attack_sens = animations_attack_sens
        self.animation_dead_sens = animations_dead_sens
        self.animation_ulti_sens = animations_ulti_sens
        self.ulti_text = "ISSOU ! : +5 attaque / 30 Ki"
        self.ulti = "Boost"
        self.ulti_cost = 30
        self.have_animation_dead = True

    def boost(self):
        self.player_ulti_animation = True
        self.game.play_sound('issou')

    def ultimate(self):
        self.attack += 5
        self.ki -= self.ulti_cost