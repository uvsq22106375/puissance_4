#############################################
# groupe 7 MIASHS TD1
# GOREAU Thelma
# VIGNERON Thomas
# SOW Mahmoud
# LIMOUZIN Matthieu
# https://github.com/uvsq22106375/puissance_4
#############################################


                                        PROJET PUISSANCE 4:

REGLES DU JEU:

- Ce jeu se joue à deux joueurs et se déroule sur un tableau à 7 colonnes et 6 lignes soit 42 cellules. 
- A chaque tour, chaque joueur place un jeton dans la colonne de son choix et celui-ci tombe jusqu’à la première case disponible. 
- Le premier joueur qui réussit à aligner quatre jetons de sa couleur à l’horizontale, verticale ou en diagonale gagne. Si personne n’y arrive, c'est-à-dire que toutes les cases de la grille de jeu sont remplies sans alignement, alors la partie se finit et il y a égalité

COMMENT JOUER:

- Interaction avec l'utilisateur
    - Le programme demande à l'utilisateur s'il veut charger une partie déjà existante ou bien en démarrer une nouvelle:
        - demarrer une nouvelle partie: taper "nouvelle" dans l'invite de commande
        - charger une partie: taper "charger" dans l'invite de commande
    - Le programme demande ensuite à l'utilisateur les prénoms des deux joueurs:
        - taper les deux prénoms dansl'invite de commande
    - Le programme demande ensuite à l'utilisateur s'il veut faire une partie en une manche gagnante ou plus:
        - une seule manche: taper "oui"
        - plusieurs manches: taper "non"
    - Si l'utilisateur choisit de faire une partie en plusieurs manches (il a tapé "non"), le programme demande le nombre de manches voulues:
        - taper le nombre de manches
        - le premier joueur à atteindre ce nombre est le gagnant

- Jeu sur la grille
    - tour à tour, chaque joueur clique sur la grille
    - le pion tombe dans la colonne où le joueur à cliquer et dans la ligne disponible (où il n'y a pas déjà un pion)

GESTION DES BOUTONS:

- Sauvegarde d'une partie
    - Chaque fois que le joueur clique sur le bouton "sauvegarde", le fichier "sauvegarde.txt" enregistre:
        - la grille et les pions déjà présent dans cette dernière
        - le joueur qui devra jouer en premier lorsque l'utilisateur tapera "charger"
        - le premier joueur à avoir jouer
        - le deuxième joueur à avoir jouer
        - si la partie chargée est déjà terminée
- annuler le coup précédent:
    - si le joueur veut annuler son coup (et même ceux d'avant) alors il lui suffit d'appuyer sur le bouton "retour"











