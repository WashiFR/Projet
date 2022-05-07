import pygame
import math
from player import *
from game import Game
pygame.init()

def jeu_combat():

    # générer la fenêtre du jeu
    pygame.display.set_caption("Projet") # changer le titre et l'icon
    screen = pygame.display.set_mode((1080, 700)) # définir la taille de la fenêtre

    # importer et charger l'arrière plan du jeu
    background = pygame.image.load("Projet/assets/bg.jpg") # importer l'image

    # importer les boutons
    play_button = pygame.image.load("Projet/assets/button.png")
    play_button = pygame.transform.scale(play_button, (400, 150))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_width() / 3.33)
    play_button_rect.y = math.ceil(screen.get_height() / 2)

    button_attaque = pygame.image.load("Projet/assets/bouton_attaque.png")
    button_attaque_rect = button_attaque.get_rect()
    button_attaque_rect.x = 0
    button_attaque_rect.y = 510

    button_attaque_spe = pygame.image.load("Projet/assets/bouton_attaque_special.png")
    button_attaque_spe_rect = button_attaque_spe.get_rect()
    button_attaque_spe_rect.x = 260
    button_attaque_spe_rect.y = 510

    button_ki = pygame.image.load("Projet/assets/bouton_ki.png")
    button_ki_rect = button_ki.get_rect()
    button_ki_rect.x = 520
    button_ki_rect.y = 510 

    button_ulti = pygame.image.load("Projet/assets/bouton_ulti.png")
    button_ulti_rect = button_ulti.get_rect()
    button_ulti_rect.x = 780
    button_ulti_rect.y = 510

    # charger le jeu
    game = Game()

    font = pygame.font.Font('Projet/assets/my_custom_font.ttf', 70)
    lunched = True
    choix = True
    choix2 = True
    run = True
    mort = ""
    action_j1 = ''
    action_j2 = ''
    clock = pygame.time.Clock()
    FPS = 30

    # début du jeu
    while lunched:

        # appliquer l'arrière plan du jeu
        screen.blit(background, (0, -300))

        # vérifer si le jeu a commencé ou non
        if game.is_playing:
            
            # choix joueur 1
            while choix:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:

                            if game.text1 == "Tyler1":
                                game.player1 = Tyler1(game, 100, 0, 0, 0, 1, 1)
                                choix = False
                            elif game.text1 == "Bob E":
                                game.player1 = BobEponge(game, 100, 1, 0, 0, 0, 0)
                                choix = False
                            elif game.text1 == "Sardoche":
                                game.player1 = Sardoche(game, 100, 1, 0, 0, 0, 0)
                                choix = False
                            elif game.text1 == "Bob R":
                                game.player1 = BobRazowski(game, 100, 0, 0, 0, 0, 0)
                                choix = False
                            elif game.text1 == "Jotaro":
                                game.player1 = Jotaro(game, 100, 0, 0, 1, 0, 0)
                                choix = False
                            elif game.text1 == 'Risitas':
                                game.player1 = Risitas(game, 100, 1, 0, 0, 0, 1)
                                choix = False

                        elif event.key == pygame.K_BACKSPACE:
                            game.text1 = game.text1[:-1]
                        else:
                            game.text1 += event.unicode

                screen.fill(0)
                text_surf = font.render(game.text1, True, (255, 255, 255))
                screen.blit(background, (0, -300))
                game.update_choix(screen, "1")
                screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))
                pygame.display.flip()

            # choix joueur 2
            while choix2:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:

                            if game.text2 == "Tyler1":
                                game.player2 = Tyler1(game, 700, 1, 0, 1, 0, 0)
                                choix2 = False
                            elif game.text2 == "Bob E":
                                game.player2 = BobEponge(game, 700, 0, 0, 0, 0, 0)
                                choix2 = False
                            elif game.text2 == "Sardoche":
                                game.player2 = Sardoche(game, 700, 0, 0, 0, 1, 0)
                                choix2 = False
                            elif game.text2 == "Bob R":
                                game.player2 = BobRazowski(game, 700, 0, 0, 0, 0, 0)
                                choix2 = False
                            elif game.text2 == "Jotaro":
                                game.player2 = Jotaro(game, 700, 1, 0, 0, 0, 1)
                                choix2 = False
                            elif game.text2 == 'Risitas':
                                game.player2 = Risitas(game, 700, 0, 0, 0, 0, 0)
                                choix2 = False

                        elif event.key == pygame.K_BACKSPACE:
                            game.text2 = game.text2[:-1]
                        else:
                            game.text2 += event.unicode

                screen.fill(0)
                text_surf = font.render(game.text2, True, (255, 255, 255))
                screen.blit(background, (0, -300))
                game.update_choix(screen, "2")
                screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))
                pygame.display.flip()

            # déclancher les instructions de la partie
            screen.fill(0)
            # appliquer l'arrière plan du jeu
            screen.blit(background, (0, -300))

            # afficher les boutons
            if game.tour_j1 == True:

                if game.tour_j1 == True and game.player1.ulti == '':
                    screen.blit(button_attaque, button_attaque_rect)
                    screen.blit(button_attaque_spe, button_attaque_spe_rect)
                    screen.blit(button_ki, button_ki_rect)

                else:
                    screen.blit(button_attaque, button_attaque_rect)
                    screen.blit(button_attaque_spe, button_attaque_spe_rect)
                    screen.blit(button_ki, button_ki_rect)
                    screen.blit(button_ulti, button_ulti_rect)

            elif game.tour_j1 == False:

                if game.tour_j1 == False and game.player2.ulti == '':
                    screen.blit(button_attaque, button_attaque_rect)
                    screen.blit(button_attaque_spe, button_attaque_spe_rect)
                    screen.blit(button_ki, button_ki_rect)

                else:
                    screen.blit(button_attaque, button_attaque_rect)
                    screen.blit(button_attaque_spe, button_attaque_spe_rect)
                    screen.blit(button_ki, button_ki_rect)
                    screen.blit(button_ulti, button_ulti_rect)
            
            # afficher les joueurs
            game.update(screen, game.player1, game.player1.get_name())
            game.update(screen, game.player2, game.player2.get_name())

            # afficher les actions
            if game.tour_j1 == True:
                game.update_text(screen, "1", game.player1, game.text1)
                game.update_text_action(screen, action_j2, "J2", game.player2)
            elif game.tour_j1 == False:
                game.update_text(screen, "2", game.player2, game.text2)
                game.update_text_action(screen, action_j1, "J1", game.player1)

            # mettre à jour l'écran
            pygame.display.flip()

            # tour joueur 1
            if game.tour_j1 == True:

                action_j1 = ''
                game.player1.esquive = False
                game.player1.critique = False

                for event in pygame.event.get():
                    # véirfier que l'event est "fermeture de fenêtre"
                    if event.type == pygame.QUIT:
                        lunched = False
                        pygame.quit() # ferme la fenêtre

                    # detecter si un joueur lache une touche du clavier
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if button_attaque_rect.collidepoint(event.pos):
                            if game.player1.get_ki() >= 20:
                                action_j1 = 'attack'
                                game.player1.attack_player(game.player2)
                                game.tour_j1 = False
                                game.tour_j2 = True

                        elif button_ki_rect.collidepoint(event.pos):
                            if game.player1.get_ki() == game.player1.get_max_ki():
                                continue
                            else:
                                action_j1 = 'recover_ki'
                                game.player1.recover_ki()
                                game.tour_j1 = False
                                game.tour_j2 = True

                        elif button_attaque_spe_rect.collidepoint(event.pos):
                            if game.player1.get_ki() >= 150:
                                action_j1 = 'special'
                                game.player1.attack_special_player(game.player2)
                                if game.text1 == 'Tyler1' and game.player1.esquive == False:
                                    game.play_sound('punchair')
                                elif game.text1 == 'Jotaro' and game.player1.esquive == False:
                                    game.play_sound('oraora')
                                game.tour_j1 = False
                                game.tour_j2 = True

                        elif button_ulti_rect.collidepoint(event.pos):
                            if game.player1.ulti == "Soin":
                                if game.player1.get_pv() == game.player1.get_max_pv() or game.player1.get_ki() < game.player1.get_ulti_cost():
                                    continue
                                else:
                                    action_j1 = 'soin'
                                    game.player1.soin()
                                    game.tour_j1 = False
                                    game.tour_j2 = True

                            elif game.player1.ulti == "Transfo":
                                if game.player1.get_pv() <= game.player1.get_pv_transfo():
                                    action_j1 = 'transfo'
                                    game.player1.transfo()
                                    game.tour_j1 = False
                                    game.tour_j2 = True

                            elif game.player1.ulti == "Peur":
                                if game.player1.get_ki() >= game.player1.get_ulti_cost():
                                    action_j1 = 'peur'
                                    game.player1.peur(game.player2)
                                    game.tour_j1 = False
                                    game.tour_j2 = True

                            elif game.player1.ulti == "Boost":
                                action_j1 = 'boost'
                                if game.player1.get_ki() >= game.player1.get_ulti_cost():
                                    game.player1.boost()
                                    game.tour_j1 = False
                                    game.tour_j2 = True

                # savoir qui est mort
                if game.player2.get_pv() <= 0:
                    mort = "J2"
                    if game.player2.have_animation_dead:
                        game.player2.player_dead_animation = True
                        game.tour_j1 = ''
                        if game.text2 == 'Sardoche':
                            game.play_sound('ctsur')
                    else:
                        game.game_over()

                elif game.player1.get_pv() <= 0:
                    mort = "J1"
                    if game.player1.have_animation_dead:
                        game.player1.player_dead_animation = True
                        game.tour_j1 = ''
                        if game.text1 == 'Sardoche':
                            game.play_sound('ctsur')
                    else:
                        game.game_over()
            
            # tour joueur 2
            elif game.tour_j1 == False:

                action_j2 = ''
                game.player2.esquive = False
                game.player2.critique = False

                for event in pygame.event.get():
                    # véirfier que l'event est "fermeture de fenêtre"
                    if event.type == pygame.QUIT:
                        lunched = False
                        pygame.quit() # ferme la fenêtre

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if button_attaque_rect.collidepoint(event.pos):
                            if game.player2.get_ki() >= 20:
                                action_j2 = 'attack'
                                game.player2.attack_player(game.player1)
                                game.tour_j1 = True
                                game.tour_j2 = False

                        elif button_ki_rect.collidepoint(event.pos):
                            if game.player2.get_ki() == game.player2.get_max_ki():
                                continue
                            else:
                                action_j2 = 'recover_ki'
                                game.player2.recover_ki()
                                game.tour_j1 = True
                                game.tour_j2 = False

                        elif button_attaque_spe_rect.collidepoint(event.pos):
                            if game.player2.get_ki() >= 150:
                                action_j2 = 'special'
                                game.player2.attack_special_player(game.player1)
                                if game.text2 == 'Tyler1' and game.player2.esquive == False:
                                    game.play_sound('punchair')
                                elif game.text2 == 'Jotaro' and game.player2.esquive == False:
                                    game.play_sound('oraora')
                                game.tour_j1 = True
                                game.tour_j2 = False

                        elif button_ulti_rect.collidepoint(event.pos):
                            if game.player2.ulti == "Soin":
                                if game.player2.get_pv() == game.player2.get_max_pv() or game.player2.get_ki() < game.player2.get_ulti_cost():
                                    continue
                                else:
                                    action_j2 = 'soin'
                                    game.player2.soin()
                                    game.tour_j1 = True
                                    game.tour_j2 = False

                            elif game.player2.ulti == "Transfo":
                                if game.player2.get_pv() <= game.player2.get_pv_transfo():
                                    action_j2 = 'transfo'
                                    game.player2.transfo()
                                    game.tour_j1 = True
                                    game.tour_j2 = False

                            elif game.player2.ulti == "Peur":
                                if game.player2.get_ki() >= game.player2.get_ulti_cost():
                                    action_j2 = 'peur'
                                    game.player2.peur(game.player1)
                                    game.tour_j1 = True
                                    game.tour_j2 = False

                            elif game.player2.ulti == "Boost":
                                if game.player2.get_ki() >= game.player2.get_ulti_cost():
                                    action_j2 = 'boost'
                                    game.player2.boost()
                                    game.tour_j1 = True
                                    game.tour_j2 = False

                # savoir qui est mort
                if game.player1.get_pv() <= 0:
                    mort = "J1"
                    if game.player1.have_animation_dead:
                        game.player1.player_dead_animation = True
                        game.tour_j1 = ''
                        if game.text1 == 'Sardoche':
                            game.play_sound('ctsur')
                    else:
                        game.game_over()

                elif game.player2.get_pv() <= 0:
                    mort = "J2"
                    if game.player2.have_animation_dead:
                        game.player2.player_dead_animation = True
                        game.tour_j1 = ''
                        if game.text2 == 'Sardoche':
                            game.play_sound('ctsur')
                    else:
                        game.game_over()
        
        # vérifier si le jeu n'a pas commencé
        else:
            screen.blit(play_button, play_button_rect)

            if mort == "J2":
                game.screen_game_over(screen, "1")
            elif mort == "J1":
                game.screen_game_over(screen, "2")
            
            pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # savoir si la souris est en collision avec le bouton "jouer"
                if play_button_rect.collidepoint(event.pos):
                    # mettre le jeu en mode "lancé"
                    game.is_playing = True
                    game.tour_j1 = True
                    game.tour_j2 = False
                    choix = True
                    choix2 = True
            elif event.type == pygame.QUIT:
                    lunched = False
                    pygame.quit() # ferme la fenêtre
        clock.tick(FPS)