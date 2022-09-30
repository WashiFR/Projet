# Projet
Un Pierre-Feuille-Ciseau en Tkinter que j'ai faits puis auquel j'ai ajouté mon jeu de combat en python fait pour le projet de fin d'année de première en NSI.

[TOC]

# Changer le path (répertoire fichiers)

N'ayant pas trouvé de moyen de détecter le path de l'utilisateur, ou encore de mettre le path une fois puis de le réutiliser (cela engendre des erreurs), il vous faudra changer le path vous-même pour avoir accès aux images. Pour cela copié le lien de votre répertoire où ce trouve les fichiers que vous avez installés. Cela devrait ressemblé à quelque chose comme ça :

> C:/Users/user/OneDrive/Documents/VSCode/Python/Projet/assets/
>
> *Vous n'aurez pas exactement les mêmes nom, ceci est juste un exemple.*

**<span style="color:red">Attention : Ne modifiez pas les noms des images, comme par exemple `bg.jpg`, `button.png`. Ajouter juste votre path devant.</span>**

Voici les endroit où mettre votre path dans le fichier :

* `test.py` :

  ![image-20220930101557555](C:\Users\loris\AppData\Roaming\Typora\typora-user-images\image-20220930101557555.png)

* `main.py` :

  ![image-20220930101728819](C:\Users\loris\AppData\Roaming\Typora\typora-user-images\image-20220930101728819.png)

# Installer Pygame

Pour installer pygame il suffit d'écrire `pip install pygame` dans votre terminal de commande.

Si cela ne marche pas, rendez-vous sur le site de <a href="https://www.pygame.org/wiki/GettingStarted">Pygame</a> pour résoudre le problème ou trouver une autre méthode d'installation qui marche pour vous.

## Exécuter le programme

Pour exécuter le programme, il faut lancer le fichier `jeux.py`, pour cela vous pouvez :

* utiliser la flèche en haut à droite ;

  ![image-20220930092731662](C:\Users\loris\AppData\Roaming\Typora\typora-user-images\image-20220930092731662.png)

* utiliser le raccourci `Ctrl+F5` en étant dans le fichier ;

* écrire dans le terminal de commande `py jeux.py`.
