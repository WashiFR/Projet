# Changer le path (répertoire fichiers)

N'ayant pas trouvé de moyen de détecter le path de l'utilisateur, ou encore de mettre le path une fois puis de le réutiliser (cela engendre des erreurs), il vous faudra changer le path vous-même pour avoir accès aux images. Pour cela copié le lien de votre répertoire où ce trouve le fichier des images que vous avez installés. Cela devrait ressemblé à quelque chose comme ça :

> C:/Users/user/OneDrive/Documents/VSCode/Python/Projet/assets/
>
> Python/Projet/assets/
>
> *Vous n'aurez pas exactement les mêmes nom, ceci est juste un exemple.*

**<span style="color:red">Attention : Ne modifiez pas les noms des images, comme par exemple `bg.jpg`, `button.png`. Ajouter juste votre path devant. De plus si dans le paths il n'y a que le nom du dossier écrit, mettez aussi que le nom du dossier dans lequel vous avez mis vos fichiers.</span>**

Voici les endroit où mettre votre path dans le fichier :

* `test.py` :
* ligne 6
* `main.py` :
  * ligne 14, 17, 23, 28, 33, 38, 46
* `animation.py` :
  * ligne 37, 107, 127, 140, 158
* `game.py` :
  * ligne 15, 33, 106
* `player.py` :
  * ligne 25
* `sound.py` :
  * ligne 7, 8, 9, 10, 11, 12

# Installer Pygame

Pour installer pygame il suffit d'écrire `pip install pygame` dans votre terminal de commande.

Si cela ne marche pas, rendez-vous sur le site de <a href="https://www.pygame.org/wiki/GettingStarted">Pygame</a> pour résoudre le problème ou trouver une autre méthode d'installation qui marche pour vous.

## Exécuter le programme

Pour exécuter le programme, il faut lancer le fichier `jeux.py`, pour cela vous pouvez :

* utiliser la flèche en haut à droite ;

* utiliser le raccourci `Ctrl+F5` en étant dans le fichier ;

* écrire dans le terminal de commande `py jeux.py`.
