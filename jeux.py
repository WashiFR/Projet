import os
import random
from main import *
from pfc import *
from wordle import *
from juste_prix import *

#tkinter

continuer = True
while continuer == True:

    os.system('clear')
    print('\033[1;34m'"""  _____ _           _     _                       _                
 / ____| |         (_)   (_)                     (_)             _ 
| |    | |__   ___  _ ___ _ ___   _   _ _ __      _  ___ _   _  (_)
| |    | '_ \ / _ \| / __| / __| | | | | '_ \    | |/ _ \ | | |    
| |____| | | | (_) | \__ \ \__ \ | |_| | | | |   | |  __/ |_| |  _ 
 \_____|_| |_|\___/|_|___/_|___/  \__,_|_| |_|   | |\___|\__,_| (_)
                                                _/ |               
                                               |__/                
"""'\033[0;0m')
    print("\033[1;37m--------------------------------------------------------------------\n\n1. Pierre-Feuille-Ciseaux\n2. Wordle\n3. Juste Prix\n4. Jeu Combat\033[0;0m")
    choix_jeu = input("\033[1;37m\nEntré le numéro correspondant : \033[0;0m")

    if choix_jeu == '1':
        while 1:
            print("\033[1;37m--------------------------------------------------------------------\n\nChoisis un mode de jeu :\n\033[0;0m")
            choix_jeu_2 = input("\033[1;37m1. J1 VS Bot\n2. J1 VS J2\n\nEntré le numéro correspondant : \033[0;0m")
            if choix_jeu_2 == '1':
                os.system("clear")
                jeu_pfc_ia()
                break
            elif choix_jeu_2 == '2':
                os.system("clear")
                jeu_pfc()
                break
            else:
                continue
    elif choix_jeu == '2':
        os.system("clear")
        jeu_wordle()
    elif choix_jeu == '3':
        os.system("clear")
        jeu_juste_prix()
    elif choix_jeu == '4':
        os.system('clear')
        jeu_combat()
        continuer = False
        break
    else:
        continue
    choix_continu = input("\033[1;37m\nVoulez-vous jouer encore ? (o/n)\n\033[0;0m")
    if choix_continu in ["oui","Oui","o","O"]:
        continue
    elif choix_continu in ["non","Non","n","N"]:
        continuer = False
        os.system('clear')
