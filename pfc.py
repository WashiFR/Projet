import os
import random

def jeu_pfc(): 

    pierre = ["pierre","P","p"]
    feuille = ["feuille","F","f"]
    ciseaux = ["ciseaux","C","c"]
    j1 = ''
    j2 = ''
    while j1 not in ["pierre","feuille","ciseaux","p","P","c","C","f","F"]:
        os.system('clear')
        print('\033[1;34m'""" _____ _                           ______         _ _ _              _____ _                           
|  __ (_)                         |  ____|       (_) | |            / ____(_)                          
| |__) |  ___ _ __ _ __ ___ ______| |__ ___ _   _ _| | | ___ ______| |     _ ___  ___  __ _ _   ___  __
|  ___/ |/ _ \ '__| '__/ _ \______|  __/ _ \ | | | | | |/ _ \______| |    | / __|/ _ \/ _` | | | \ \/ /
| |   | |  __/ |  | | |  __/      | | |  __/ |_| | | | |  __/      | |____| \__ \  __/ (_| | |_| |>  < 
|_|   |_|\___|_|  |_|  \___|      |_|  \___|\__,_|_|_|_|\___|       \_____|_|___/\___|\__,_|\__,_/_/\_\
\033[0;0m\n"""'\n\033[1;37m--------------------------------------------------------------------\n\033[0;0m')
        j1 = input("\033[1;37mJoueur 1 choisis :\n- Pierre (P)\n- Feuille (F)\n- Ciseaux (C)\n\nEntré la lettre : \033[0;0m")
    os.system("clear")
    while j2 not in ["pierre","feuille","ciseaux","p","P","c","C","f","F"]:
        os.system('clear')
        print('\033[1;34m'""" _____ _                           ______         _ _ _              _____ _                           
|  __ (_)                         |  ____|       (_) | |            / ____(_)                          
| |__) |  ___ _ __ _ __ ___ ______| |__ ___ _   _ _| | | ___ ______| |     _ ___  ___  __ _ _   ___  __
|  ___/ |/ _ \ '__| '__/ _ \______|  __/ _ \ | | | | | |/ _ \______| |    | / __|/ _ \/ _` | | | \ \/ /
| |   | |  __/ |  | | |  __/      | | |  __/ |_| | | | |  __/      | |____| \__ \  __/ (_| | |_| |>  < 
|_|   |_|\___|_|  |_|  \___|      |_|  \___|\__,_|_|_|_|\___|       \_____|_|___/\___|\__,_|\__,_/_/\_\
\033[0;0m\n"""'\n\033[1;37m--------------------------------------------------------------------\n\033[0;0m')
        j2 = input("\033[1;37mJoueur 2 choisis :\n- Pierre (P)\n- Feuille (F)\n- Ciseaux (C)\n\nEntré la lettre : \033[0;0m")
    if j1 in pierre and j2 in feuille or j1 in feuille and j2 in ciseaux or j1 in ciseaux and j2 in pierre:
        print("\033[1;37m--------------------------------------------------------------------\nJ1 :",j1,"\n""J2 :",j2,"\n\n""Joueur 2 a gagné ! \033[0;0m")
    elif j2 in pierre and j1 in feuille or j2 in feuille and j1 in ciseaux or j2 in ciseaux and j1 in pierre:
        print("\033[1;37m--------------------------------------------------------------------\nJ1 :",j1,"\n""J2 :",j2,"\n\n""Joueur 1 a gagné ! \033[0;0m")
    elif j1.upper() == j2.upper():
        print("\033[1;37m--------------------------------------------------------------------\nJ1 :",j1,"\n""J2 :",j2,"\n\nEgalité ! \033[0;0m")



def jeu_pfc_ia():
    pierre = ["pierre","P","p"]     #1
    feuille = ["feuille","F","f"]   #2
    ciseaux = ["ciseaux","C","c"]   #3
    j1 = ''
    ia = random.randint(1,3)
    if ia == 1:
        ia = 'pierre'
    elif ia == 2:
        ia = 'feuille'
    else:
        ia = 'ciseaux'
    while j1 not in ["pierre","feuille","ciseaux","p","P","c","C","f","F"]:
        os.system('clear')
        print('\033[1;34m'""" _____ _                           ______         _ _ _              _____ _                           
|  __ (_)                         |  ____|       (_) | |            / ____(_)                          
| |__) |  ___ _ __ _ __ ___ ______| |__ ___ _   _ _| | | ___ ______| |     _ ___  ___  __ _ _   ___  __
|  ___/ |/ _ \ '__| '__/ _ \______|  __/ _ \ | | | | | |/ _ \______| |    | / __|/ _ \/ _` | | | \ \/ /
| |   | |  __/ |  | | |  __/      | | |  __/ |_| | | | |  __/      | |____| \__ \  __/ (_| | |_| |>  < 
|_|   |_|\___|_|  |_|  \___|      |_|  \___|\__,_|_|_|_|\___|       \_____|_|___/\___|\__,_|\__,_/_/\_\
\033[0;0m\n"""'\n\033[1;37m--------------------------------------------------------------------\n\033[0;0m')
        j1 = input("\033[1;37mJoueur 1 choisis :\n- Pierre (P)\n- Feuille (F)\n- Ciseaux (C)\n\nEntré la lettre : \033[0;0m")
    os.system("clear")
    print('\033[1;34m'""" _____ _                           ______         _ _ _              _____ _                           
|  __ (_)                         |  ____|       (_) | |            / ____(_)                          
| |__) |  ___ _ __ _ __ ___ ______| |__ ___ _   _ _| | | ___ ______| |     _ ___  ___  __ _ _   ___  __
|  ___/ |/ _ \ '__| '__/ _ \______|  __/ _ \ | | | | | |/ _ \______| |    | / __|/ _ \/ _` | | | \ \/ /
| |   | |  __/ |  | | |  __/      | | |  __/ |_| | | | |  __/      | |____| \__ \  __/ (_| | |_| |>  < 
|_|   |_|\___|_|  |_|  \___|      |_|  \___|\__,_|_|_|_|\___|       \_____|_|___/\___|\__,_|\__,_/_/\_\
\033[0;0m\n"""'\n')
    if j1 in pierre and ia in feuille or j1 in feuille and ia in ciseaux or j1 in ciseaux and ia in pierre:
        print("\033[1;37m--------------------------------------------------------------------\nJ1 :",j1,"\n""IA :",ia,"\n\n""Joueur IA a gagné ! \033[0;0m")
    elif ia in pierre and j1 in feuille or ia in feuille and j1 in ciseaux or ia in ciseaux and j1 in pierre:
        print("\033[1;37m--------------------------------------------------------------------\nJ1 :",j1,"\n""IA :",ia,"\n\n""Joueur 1 a gagné ! \033[0;0m")
    else:
        print("\033[1;37m--------------------------------------------------------------------\nJ1 :",j1,"\n""J2 :",ia,"\n\nEgalité ! \033[0;0m")
