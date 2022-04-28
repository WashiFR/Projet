from random import randint
import os

p1 = {"PV": 100, "Ki": 100, "Attack": 20, "Special": "Transfo", "Max_PV": 100, "Max_Ki": 200}
p2 = {"PV": 100, "Ki": 100, "Attack": 20, "Special": "Soin", "Max_PV": 100, "Max_Ki": 200}
p3 = {"PV": 100, "Ki": 100, "Attack": 20, "Special": "Boost Attack", "Max_PV": 100, "Max_Ki": 200}
personnages = {"p1": p1, "p2": p2, "p3": p3}

J1 = {}
J2 = {}
Bot = {"PV": 100, "Ki": 100, "Attack": 20, "Max_Ki": 200}

def tour_joueur(dico, dico2, i, y):
# Début de la partie :
    while 1:

        print("J" + y + " PV : " + str(dico2["PV"]) + "\n")
        for cle,val in dico.items():
            print("J" + i + " => " + str(cle), ":", str(val))
        if dico["Special"] == "Transfo":
            attaque = input("\n" + "J" + i + " choisis une action :" + "\n" + "t. Transformation (si PV <= 20)" + "\n" + "a. Attaque (-20 Ki)" + "\n" + "x. Attaque Spécial (-100 ki)" + "\n" + "k. Recharger Ki" + "\n" + "r. Rien" + "\n")
        elif dico["Special"] == "Soin":
            attaque = input("\n" + "J" + i + " choisis une action :" + "\n" + "s. Soin (+50 PV / -40 Ki) " + "\n" + "a. Attaque (-20 Ki)" + "\n" + "x. Attaque Spécial (-100 ki)" + "\n" + "k. Recharger Ki" + "\n" + "r. Rien" + "\n")
        elif dico["Special"] == "Boost Attack":
            attaque = input("\n" + "J" + i + " choisis une action :" + "\n" + "b. Boost attaque (+5 attack / -30 Ki) " + "\n" + "a. Attaque (-20 Ki)" + "\n" + "x. Attaque Spécial (-100 ki)" + "\n" + "k. Recharger Ki" + "\n" + "r. Rien" + "\n")
        else:
            attaque = input("\n" + "J" + i + " choisis une action :" + "\n" + "a. Attaque (-20 Ki)" + "\n" + "x. Attaque Spécial (-100 ki)" + "\n" + "k. Recharger Ki" + "\n" + "r. Rien" + "\n")
        os.system("cls")

# Compétence Transformation : 
        if attaque in "Tt" and dico["Special"] != "Transfo":
            continue
        elif attaque in "Tt" and 20 >= dico["PV"] and dico["Special"] == "Transfo":
            dico["PV"] += 50
            dico["Max_Ki"] += 100
            dico["Ki"] += 50
            dico["Attack"] += 20
            print("J" + i + " s'est transformé ! ")
            break
        elif attaque in "Tt" and 20 <= dico["PV"] and dico["Special"] == "Transfo":
            print("Tu ne peut pas encore te transformer...")
            continue

# Compétence Soin :
        elif attaque in "Ss" and dico["Special"] != "Soin":
            continue
        elif attaque in "Ss" and dico["Special"] == "Soin":
            if dico["PV"] == dico["Max_PV"]:
                print("Tu a atteint ta limite ! " + "\n")
                continue
            else:
                dico["PV"] += 50
                dico["Ki"] -= 40
                if dico["PV"] > dico["Max_PV"]:
                    dico["PV"] = dico["Max_PV"]
                    print("J" + i + " s'est soigné ! " + "\n")
                    break
                else:
                    print("J" + i + " s'est soigné ! " + "\n")
                    break

# Compétence Boost Attack :
        elif attaque in "Bb" and dico["Special"] != "Boost Attack":
            continue
        elif attaque in "Bb" and dico["Special"] == "Boost Attack":
            if dico["Ki"] < 30:
                print("Tu n'a pas assez de ki...")
                continue
            else:
                dico["Ki"] -= 30
                dico["Attack"] += 5
                print("J" + i + " a boosté son attaque !" + "\n")

# Compétence Recharger Ki :
        elif attaque in "Kk":
            if dico["Ki"] == dico["Max_Ki"]:
                print("Tu a atteint ta limite ! " + "\n")
                continue
            else:
                dico["Ki"] += 50
                if dico["Ki"] > dico["Max_Ki"]:
                    dico["Ki"] = dico["Max_Ki"]
                    print("J" + i + " a rechargé son Ki ! " + "\n")
                    break
                else:
                    print("J" + i + " a rechargé son Ki ! " + "\n")
                    break

# Compétence Attaque : 
        elif attaque in "Aa":
            esquive = randint(1, 10)
            if dico["Ki"] >= 20:
                if esquive == 1:
                    dico["Ki"] -= 20
                    print("J" + y + " a esquivé ton attaque ! ")
                    break
                else:
                    coup_critique = randint(1, 10)
                    if coup_critique == 1:
                        dico2["PV"] -= dico["Attack"] + 10
                        dico["Ki"] -= 20
                        print("Coup critique ! " + "\n" + "J" + i + " a attaqué ! " + "\n")
                        break
                    else:
                        dico2["PV"] -= dico["Attack"]
                        dico["Ki"] -= 20
                        print("J" + i + " a attaqué ! " + "\n")
                        break
            else:
                print("Tu n'a plus de Ki pour attaquer... " + "\n")
                continue

# Compétence Rien :
        elif attaque in "Rr":
            print("J" + i + " n'a rien fait... " + "\n")
            break

# Compétence Attaque Spécial : 
        elif attaque in "Xx":
            esquive = randint(1, 10)
            if dico["Ki"] >= 100:
                if esquive == 1:
                    dico["Ki"] -= 100
                    print("J" + y + " a esquivé ton attaque ! ")
                    break
                else:
                    coup_critique = randint(1, 10)
                    if coup_critique == 1:
                        dico2["PV"] -= dico["Attack"] * 3 + 10
                        dico["Ki"] -= 100
                        print("Coup critique ! " + "\n" + "J" + i + " a fait une attaque spécial ! " + "\n")
                        break
                    else:
                        dico2["PV"] -= dico["Attack"] * 3
                        dico["Ki"] -= 100
                        print("J" + i + " a fait une attaque spécial ! " + "\n")
                        break
            else:
                print("Tu n'a plus de Ki pour attaquer... ")
                continue
            
        else:
            continue

# Début du jeu : 
os.system("cls")
mode_de_jeu = input("Choisis un mode de jeu : " + "\n" + "1. J1 vs J2" + "\n" + "2. J1 vs Ordi" +"\n")
os.system("cls")

# Mode de jeu : J1 vs J2 :
if mode_de_jeu == "1":

    while 1:
        for cle, val in personnages.items():
            print(cle, "\n", val)
        choix = input("J1 : Choisis un personnage : ")
        if choix in personnages:
            print("Tu as choisis " + choix)
            suite = input("Es-tu sûr de ton choix ? (o/n) : " + "\n")
            if suite in "Oo ":
                J1 = personnages[choix]
                os.system("cls")
                break
            elif suite in "Nn":
                continue
        else:
            os.system("cls")
            print("Il n'y a pas ce personnage...")
            continue
        os.system("cls")

    while 1:
        for cle, val in personnages.items():
            print(cle, "\n", val)
        choix = input("J2 : Choisis un personnage : ")
        if choix in personnages:
            print("Tu as choisis " + choix)
            suite = input("Es-tu sûr de ton choix ? (o/n) : " + "\n")
            if suite in "Oo ":
                J2 = personnages[choix]
                os.system("cls")
                break
            elif suite in "Nn":
                continue
        else:
            os.system("cls")
            print("Il n'y a pas ce personnage...")
            continue
        os.system("cls")

    while 1:
        tour_joueur(J1, J2, "1", "2")
        if J2["PV"] <= 0:
            print("J2 vainceur ! ")
            break
        tour_joueur(J2, J1, "2", "1")
        if J1["PV"] <= 0:
            print("J1 vainceur ! ")
            break
    
elif mode_de_jeu == "2":

    while 1:
        for cle, val in personnages.items():
            print(cle, "\n", val)
        choix = input("J1 : Choisis un personnage : ")
        if choix in personnages:
            print("Tu as choisis " + choix)
            suite = input("Es-tu sûr de ton choix ? (o/n) : " + "\n")
            if suite in "Oo ":
                J1 = personnages[choix]
                os.system("cls")
                break
            elif suite in "Nn":
                continue
        else:
            os.system("cls")
            print("Il n'y a pas ce personnage...")
            continue
        os.system("cls")

    while 1:
        tour_joueur(J1, Bot, "1", "Ordi")
        if Bot["PV"] <= 0:
            print("J1 vainceur ! ") 
            break
        # Tours de l'Ordi :
        attaque_ordi = randint(1, 3)

# Compétence Ordi : Attaque :
        if attaque_ordi == 1 or 2:
            esquive_j1 = randint(1, 10)
            coup_critique = randint(1, 10)
            if Bot["Ki"] < 20:
                Bot["Ki"] += 50
                print("Ordi a rechargé son ki ! ")
            elif Bot["Ki"] >= 20:
                if esquive_j1 == 1:
                    Bot["Ki"] -= 20
                    print("Tu a esquivé l'attaque ! ")
                else:
                    if coup_critique == 1:
                        J1["PV"] -= 20 + 10
                        Bot["Ki"] -= 20
                        print("Coup critique ! " + "\n" + "Ordi vous a attaqué ! ")
                    else:
                        J1["PV"] -= 20
                        Bot["Ki"] -= 20
                        print("Ordi vous a attaqué ! ")

# Compétence Ordi : Attaque Spécial :
        elif attaque_ordi == 3:
            esquive_j1 = randint(1, 10)
            coup_critique = randint(1, 10)
            if Bot["Ki"] < 100:
                Bot["Ki"] += 50
                print("Ordi a rechargé son ki ! ")
            elif Bot["Ki"] >= 100:
                if esquive_j1 == 1:
                    Bot["Ki"] -= 100
                    print("Tu a esquivé l'attaque spécial ! ")
                else:
                    if coup_critique == 1:
                        J1["PV"] -= 20 * 3 + 10
                        Bot["Ki"] -= 100
                        print("Coup critique ! " + "\n" + "Ordi vous a fait une attaque spécial ! ")
                    else:
                        J1["PV"] -= 20 * 3
                        Bot["Ki"] -= 100
                        print("Ordi vous a fait une attaque spécial ! ")
        
        if J1["PV"] <= 0:
            print("Ordi vainceur ! ")
            break