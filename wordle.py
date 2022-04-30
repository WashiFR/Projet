import os
import random

def jeu_wordle():
    trop = None
    nb_tentatives = 7
    liste_mots = ['ABATS','ABIME','ABOIE','ACCRO','ADMIT']
    liste_mauvais_mots = []
    bon_mot = liste_mots[random.randint(0, len(liste_mots)-1)]
    liste_bon_mot = [i for i in bon_mot]
    liste = []
    for i in range(0, len(liste_bon_mot)):
            liste.append('.')
    while nb_tentatives != 0:
        print('\033[1;34m'""" __          __           _ _
 \ \        / /          | | |     
  \ \  /\  / /__  _ __ __| | | ___ 
   \ \/  \/ / _ \| '__/ _` | |/ _ 
    \  /\  / (_) | | | (_| | |  __/
     \/  \/ \___/|_|  \__,_|_|\___|
\033[0;0m\n"""'\n\033[1;37m--------------------------------------------------------------------\n\033[0;0m')
        if trop == True:
            print("\033[1;37mTrop de caractères !\033[0;0m")
        elif trop == False:
            print("\033[1;37mPas assez de caractères !\033[0;0m")
        print("\033[1;37mNombres de tentatives :",nb_tentatives,"\n\n"+''.join(liste),'\n\n'+'\n'.join(liste_mauvais_mots),'\033[0;0m')
        mot = input('\n')
        if mot.upper() == bon_mot:
            print('\033[1;37mMot trouvé !\033[0;0m')
            break
        elif len(mot) < len(liste_bon_mot):
            os.system('clear')
            trop = False
            continue
        elif len(mot) > len(liste_bon_mot):
            os.system('clear')
            trop = True
            continue
        else:
            liste_mauvais_mots.append(mot.upper())
            nb_tentatives -= 1
            liste_mot = [i for i in mot]
            for i in range(len(liste_bon_mot)):
                if liste_mot[i].upper() == liste_bon_mot[i].upper():
                    liste[i] = liste_mot[i].upper()
            os.system('clear')
            continue
    if nb_tentatives == 0:
        print('\033[1;34m'""" __          __           _ _
 \ \        / /          | | |     
  \ \  /\  / /__  _ __ __| | | ___ 
   \ \/  \/ / _ \| '__/ _` | |/ _ 
    \  /\  / (_) | | | (_| | |  __/
     \/  \/ \___/|_|  \__,_|_|\___|
\033[0;0m\n"""'\n')
        print("\033[1;37mPerdu !\033[0;0m")
