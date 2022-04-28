import os
import random

def jeu_juste_prix():
    plus = None
    nb_tentatives = 7
    prix = random.randint(1, 1000)
    while nb_tentatives != 0:
        print('\033[1;34m'"""       _           _         _____      _      
      | |         | |       |  __ \    (_)     
      | |_   _ ___| |_ ___  | |__) | __ ___  __
  _   | | | | / __| __/ _ \ |  ___/ '__| \ \/ /
 | |__| | |_| \__ \ ||  __/ | |   | |  | |>  < 
  \____/ \__,_|___/\__\___| |_|   |_|  |_/_/\_\
\033[0;0m\n"""'\n\033[1;37m--------------------------------------------------------------------\n\033[0;0m')
        if plus == True:
            print("\033[1;37mC'est plus !\033[0;0m")
        elif plus == False:
            print("\033[1;37mC'est moins !\033[0;0m")
        print("\033[1;37mNombres de tentatives :",nb_tentatives,"\033[0;0m")
        prix_joueur = input("\033[1;37mDevinez le prix : \033[0;0m")
        if prix_joueur in "abcdefghijklmnopqrstuvwxyz":
            os.system("clear")
            continue
        elif int(prix_joueur) < prix:
            os.system("clear")
            nb_tentatives -= 1
            plus = True
            continue
        elif int(prix_joueur) > prix:
            os.system("clear")
            nb_tentatives -= 1
            plus = False
            continue
        elif int(prix_joueur) == prix:
            print("\033[1;37mBravo ! Vous avez trouvé le bon prix !\033[0;0m")
            break
    if nb_tentatives == 0:
        print('\033[1;34m'"""       _           _         _____      _      
      | |         | |       |  __ \    (_)     
      | |_   _ ___| |_ ___  | |__) | __ ___  __
  _   | | | | / __| __/ _ \ |  ___/ '__| \ \/ /
 | |__| | |_| \__ \ ||  __/ | |   | |  | |>  < 
  \____/ \__,_|___/\__\___| |_|   |_|  |_/_/\_\
\033[0;0m\n"""'\n')
        print("\033[1;37mPerdu !")