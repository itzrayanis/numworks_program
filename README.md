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
- BACKSPACE pour effacer (SHIFT pour clear)
- MENU pour quitter (Valider)
- TOOLBOX pour accéder au menu de configuration (Utiliser les flèches directionnels et OK pour valider)

L'application propose une configuration de la taille du curseur, la couleur d'écriture ainsi que le fond, actuellement
l'application met a disposition trois palette de chacune 36 couleurs. (Soit un total de 108 couleurs).


<details>
<summary>Modifier le script de l'application</summary>

<br>
Modifier le script de l'application peut être interrésant pour changer les limites par défauts. <br><br>
Vous pouvez modifier les variables suivantes:
<ul>
<li> `taille_min` et `taille_max` dans la def `scale_menu` pour pouvoir modifier les limites de la taille du curseur (Il est recommandé de mettre un multiple de 2 en limite). </li>
<li> `color_choices` au début du script pour ajouter vos propres couleurs dans une palette ou alors créer votre propre palette.</li>
<li> `ttc` cette variable permet de régler le temps d'attente pour pouvoir appuyer sur un bouton après en avoir appuyé sur un, celle ci permet donc d'éviter de faire deux fois la même action quand on appuie sur un bouton. (Il est tous de même recommandé de ne pas changer cette variable ou alors au minimum 0.15).</li>
</ul>
</details>

## Fonction
### Dialog
Permet de pouvoir afficher des info ou mneu de sélection.

Fonctions:
- `info(text)` -> Affiche un texte, OK pour continuer
- `dialog(text)` -> Affihce un texte avec deux otpions, OUI pour valider, NON pour refuser
- `menu(options)` -> Permet d'afficher un menu, selection avec les flèches directionnelles et OK pour valider, format des options: `["option 1","option 2"]` 3 options maximum (support actuelle). 

Pour les fonctions `dialog` et `menu` un nombre vous sera retourné selon le choix, pour `dialog` OUI vous retournera 1 et NON 0, pour le menu cela sera de 0 à 2 du premier au dernier choix.
