# Numworks Program
Ce repo git est là pour mettre à disposition plusieurs programmes tels que des applications, fonctions, ...

Vous pouvez aussi retrouvez les application sur mon profil numworks:
https://my.numworks.com/python/itzrayanis/

## Applications:
### [Paint](https://my.numworks.com/python/itzrayanis/paint) 
Application de dessin avancé.
#### Commandes:
- Flèches directionnels pour bouger le curseur
- OK pour écrire
- BACKSPACE pour effacer
- SHIFT BACKSPACE pour quitter (Valider)
- TOOLBOX pour accéder au menu de configuration de la taille du curseur, couleur et fond (Utiliser les flèches directionnels et OK pour valider)

## Fonction
### Dialog
Permet de pouvoir afficher des info ou mneu de sélection.

Fonctions:
- `info(text)` -> Affiche un texte, OK pour continuer
- `dialog(text)` -> Affihce un texte avec deux otpions, OUI pour valider, NON pour refuser
- `menu(options)` -> Permet d'afficher un menu, selection avec les flèches directionnelles et OK pour valider, format des options: `["option 1","option 2"]` 3 options maximum (support actuelle). 

Pour les fonctions `dialog` et `menu` un nombre vous sera retourné selon le choix, pour `dialog` OUI vous retournera 1 et NON 0, pour le menu cela sera de 0 à 2 du premier au dernier choix.
