from tkinter import *
from main import jeu_combat
import random
import os

# permet de trouver l'ndroit où se trouve le fichier
path = os.path.dirname(os.path.abspath(__file__))

ft = ("Courrier", 20)
bg = '#211946'
fg = 'white'

choix1 = ''
choix2 = ''

def set_choix1(valeur):
    global choix1
    choix1 = valeur

def set_choix2(valeur):
    global choix2
    choix2 = valeur

def effacer():
    for widget in frame.winfo_children():
        widget.pack_forget()

def choix_jeu():
    text = Label(frame, text='Choisis un jeu en cliquant sur un bouton :\n', font=ft, bg=bg, fg=fg).pack()
    bouton_pfc = Button(frame, text='Pierre-Feuille-Ciseaux', font=ft, bg=fg, command=lambda:[effacer(), parametre_pfc()]).pack(fill=X)
    bouton_jeu_combat = Button(frame, text='Jeu de combat', font=ft, bg=fg, command=lambda:[page.destroy(), jeu_combat()]).pack(fill=X)

def parametre_pfc():
    text = Label(frame, text='Choisis ton mode de jeu\n', font=ft, bg=bg, fg=fg).pack()
    bouton_1 = Button(frame, text='J1 vs IA', font=ft, bg=fg, command=lambda:[effacer(), choix_pfc_1()]).pack(fill=X)
    bouton_2 = Button(frame, text='J1 vs J2', font=ft, bg=fg, command=lambda:[effacer(), choix_pfc_2()]).pack(fill=X)

def choix_pfc_1():
    text = Label(frame, text='Choisis ton action en cliquant sur un bouton :\n', font=ft, bg=bg, fg=fg).pack()
    bouton_p = Button(frame, image=pierre, command=lambda:[effacer(), pfc_1('Pierre')]).pack(padx= 15, side=LEFT)
    bouton_f = Button(frame, image=feuille, command=lambda:[effacer(), pfc_1('Feuille')]).pack(padx= 15, side=LEFT)
    bouton_c = Button(frame, image=ciseaux, command=lambda:[effacer(), pfc_1('Ciseaux')]).pack(padx= 15, side=LEFT)

def pfc_1(choix):
    liste_choix = ['Pierre','Feuille','Ciseaux']
    choix_bot = liste_choix[random.randint(0, 2)]
    if choix == 'Pierre' and choix_bot == 'Ciseaux' or choix == 'Feuille' and choix_bot == 'Pierre' or choix == 'Ciseaux' and choix_bot == 'Feuille':
        text = Label(frame, text='Joueur 1 : '+choix+'\nJoueur IA : '+choix_bot+'\n\nJoueur 1 a gagné !\n', font=ft, bg=bg, fg=fg).pack()
    elif choix == 'Pierre' and choix_bot == 'Feuille' or choix == 'Feuille' and choix_bot == 'Ciseaux' or choix == 'Ciseaux' and choix_bot == 'Pierre':
        text = Label(frame, text='Joueur 1 : '+choix+'\nJoueur IA : '+choix_bot+'\n\nJoueur IA a gagné !\n', font=ft, bg=bg, fg=fg).pack()
    else:
        text = Label(frame, text='Joueur 1 : '+choix+'\nJoueur IA : '+choix_bot+'\n\nEgalité !\n', font=ft, bg=bg, fg=fg).pack()
    
    bouton_rejouer = Button(frame, text='Rejouer', font=ft, bg=fg, command=lambda:[effacer(), choix_pfc_1()]).pack(side=LEFT)
    bouton_quitter = Button(frame, text='Quitter', font=ft, bg=fg, command=lambda:[effacer(), choix_jeu()]).pack(side=RIGHT)

def choix_pfc_2():
    if choix1 == '':
        text = Label(frame, text='Joueur 1 choisis ton action en cliquant sur un bouton :\n', font=ft, bg=bg, fg=fg).pack()
        bouton_p = Button(frame, image=pierre, command=lambda:[effacer(), set_choix1('Pierre'), choix_pfc_2()]).pack(padx= 30, side=LEFT)
        bouton_f = Button(frame, image=feuille, command=lambda:[effacer(), set_choix1('Feuille'), choix_pfc_2()]).pack(padx= 30, side=LEFT)
        bouton_c = Button(frame, image=ciseaux, command=lambda:[effacer(), set_choix1('Ciseaux'), choix_pfc_2()]).pack(padx= 30, side=LEFT)
    if choix1 != '':
        text = Label(frame, text='Joueur 2 choisis ton action en cliquant sur un bouton :\n', font=ft, bg=bg, fg=fg).pack()
        bouton_p = Button(frame, image=pierre, command=lambda:[effacer(), set_choix2('Pierre'), pfc_2(choix1, choix2)]).pack(padx= 30, side=LEFT)
        bouton_f = Button(frame, image=feuille, command=lambda:[effacer(), set_choix2('Feuille'), pfc_2(choix1, choix2)]).pack(padx= 30, side=LEFT)
        bouton_c = Button(frame, image=ciseaux, command=lambda:[effacer(), set_choix2('Ciseaux'), pfc_2(choix1, choix2)]).pack(padx= 30, side=LEFT)

def pfc_2(choix1, choix2):
    if choix1 == 'Pierre' and choix2 == 'Ciseaux' or choix1 == 'Feuille' and choix2 == 'Pierre' or choix1 == 'Ciseaux' and choix2 == 'Feuille':
        text = Label(frame, text='Joueur 1 : '+choix1+'\nJoueur 2 : '+choix2+'\n\nJoueur 1 a gagné !\n', font=ft, bg=bg, fg=fg).pack()
    elif choix1 == 'Pierre' and choix2 == 'Feuille' or choix1 == 'Feuille' and choix2 == 'Ciseaux' or choix1 == 'Ciseaux' and choix2 == 'Pierre':
        text = Label(frame, text='Joueur 1 : '+choix1+'\nJoueur 2 : '+choix2+'\n\nJoueur 2 a gagné !\n', font=ft, bg=bg, fg=fg).pack()
    else:
        text = Label(frame, text='Joueur 1 : '+choix1+'\nJoueur 2 : '+choix2+'\n\nEgalité !\n', font=ft, bg=bg, fg=fg).pack()
    set_choix1('')
    set_choix2('')
    bouton_rejouer = Button(frame, text='Rejouer', font=ft, bg=fg, command=lambda:[effacer(), choix_pfc_2()]).pack(side=LEFT)
    bouton_quitter = Button(frame, text='Quitter', font=ft, bg=fg, command=lambda:[effacer(), choix_jeu()]).pack(side=RIGHT)

page = Tk()
page.title('Projet')
page.geometry('720x480')
page.configure(bg=bg)

pierre = PhotoImage(file=path+'/assets/pierre.png')
feuille = PhotoImage(file=path+'/assets/feuille.png')
ciseaux = PhotoImage(file=path+'/assets/ciseaux.png')

frame = Frame(page, bg=bg)
choix_jeu()
frame.pack(expand=YES)

page.mainloop()