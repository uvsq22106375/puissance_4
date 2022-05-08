#############################################
# groupe MIASHS 7
# GOREAU THELMA
# VIGNERON THOMAS
# SOW MAHMOUD
# LIMOUZIN MATTHIEU
# https://github.com/uvsq22106375/puissance_4
#############################################

# import des modules
import tkinter as tk
import random as rd

# variables globales
H = 600  # hauteur
W = 700  # largeur
m = 6  # nb lignes
n = 7  # nb colonnes
grille = []
l_coup = []  # coordonnées des clics successifs
global prenom1
fin = False
retour = False
colonne_impossible = False
charger_partie = False
joueur1 = True  # permet changement joueur, joueur1 = True
partie_finie = False
une_manche = True
fin_manche = False


# création liste à deux dimensions
# 0 : case vide
# 1 : case avec un pion jaune
# 2 : case avec un pion rouge
for i in range(m):
    grille.append([0]*n)


# fonctions

def creation_grille():
    """créer une grille de puissance 4 avec m lignes et n colonnes"""
    for i in range(m):
        for j in range(n):
            canvas.create_oval(W/n*j, H/m*i, W/n*(j+1), H/m*(i+1), 
                               fill="Dodgerblue3", outline="Dodgerblue2")
            canvas.create_oval(W/n*j+5, H/m*i+5, W/n*(j+1)-5, H/m*(i+1)-5, 
                               fill="white", outline="blue")


def choix_joueur():
    """choisit aléatoirement le premier des deux joueurs qui va jouer"""
    global premier_joueur, deuxieme_joueur, prenom1, prenom2
    prenom1 = input("prénom du joueur 1 ?")
    prenom2 = input("prénom du joueur 2 ?")
    premier_joueur = rd.choice([prenom1, prenom2])
    if premier_joueur == prenom1:
        deuxieme_joueur = prenom2
    else:
        deuxieme_joueur = prenom1


def affiche_joueur():
    """affiche qui doit commencer"""
    choix_joueur()
    label_joueur.config(text=premier_joueur + " commence à jouer")


def choix_partie():
    """Demande à l'utilisateur s'il veut charger la partie précédente
       ou bien en faire une nouvelle et appelle la 
       fonction adéquate en conséquence"""
    global premier_joueur, deuxieme_joueur
    choix = input("taper charger ou nouvelle: ")
    if choix == "charger":
        charger()
        premier_joueur, deuxieme_joueur = liste[1], liste[2]
    if choix == "nouvelle":
        affiche_joueur()


def trouver_colonne(clic_x):
    """retourne la colonne sur laquelle le jeton va apparaître"""
    colonne = clic_x // 100
    return colonne 


def trouver_ligne(colonne):
    """retourne la ligne sur laquelle le jeton va apparaître"""
    chgt_ligne = m-1
    for i in range(m):  # vérifie si la case est libre
        if grille[chgt_ligne][colonne] == 0:
            ligne = chgt_ligne
        else:
            chgt_ligne -= 1
    return ligne


def gestion_clic(event):
    """affiche le jeton dans la grille si cela est possible"""
    global joueur1, fin, ligne, colonne, retour
    global colonne_impossible, partie_finie, nb_parties
    if fin:   # 4 pions déjà alignés ou grille pleine
        return
    if partie_finie:  # chargement partie déjà terminée
        label_gagnant.config(text="La partie est déjà terminée, commencer une nouvelle partie")
        return
    if 0 < event.x < W and 0 < event.y < H:
        clic_x = event.x
        colonne = trouver_colonne(clic_x)
        ligne = trouver_ligne(colonne)
        if joueur1:
            canvas.create_oval(colonne*100+5, ligne*100+5, colonne*100+100-5,
                               ligne*100+100-5, fill="gold")
            grille[ligne][colonne] = 1
            joueur1 = not joueur1
            if retour:   # joueur clique sur le bouton retour
                retour = False     
            label_joueur.config(text="À " + deuxieme_joueur + " de jouer")      
        else:
            canvas.create_oval(colonne*100+5, ligne*100+5,
                               colonne*100+100-5, ligne*100+100-5, fill="red")
            grille[ligne][colonne] = 2
            joueur1 = not joueur1
            if retour:
                retour = False
            label_joueur.config(text="À " + premier_joueur + " de jouer") 
    alignement(ligne, colonne)
    dernier_coup()
    grille_pleine()


def alignement(ligne, colonne):
    """détecte alignement de 4 pions à partir du dernier pion posé"""
    global id_joueur
    id_joueur = grille[ligne][colonne]

    # vertical 
    # compteur qui part de 1 et qui compte le nombre de pion de même\
    # couleur par rapport au dernier pion posé
    cpt = 1  
    while (ligne + cpt < 6) and (grille[ligne+cpt][colonne] == id_joueur):
        cpt += 1
        if cpt == 4:
            fin_du_jeu()

    # horizontal (gauche et droite)
    cpt = 1
    while (colonne - cpt >= 0 and 
           grille[ligne][colonne - cpt] == id_joueur):  # gauche
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
    while (colonne + cpt < 7 and 
           grille[ligne][colonne + cpt] == id_joueur):  # droite
        cpt += 1
        if cpt == 4:
            fin_du_jeu()

    # 2 diagonales (montante vers la droite ou la gauche)
    # montante vers la droite
    cpt = 1
    while (colonne - cpt >= 0 and ligne + cpt < 6 and
           grille[ligne + cpt][colonne - cpt] == id_joueur):  # bas gauche
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
    while (colonne + cpt < 7 and ligne - cpt >= 0 and 
           grille[ligne-cpt][colonne + cpt] == id_joueur):  # haut droite
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
    # montante vers la gauche
    cpt = 1
    while (colonne + cpt < 7 and ligne + cpt < 6 and 
           grille[ligne + cpt][colonne + cpt] == id_joueur):  # bas droite
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
    while (colonne - cpt >= 0 and ligne - cpt >= 0 and 
           grille[ligne - cpt][colonne - cpt] == id_joueur):  # haut gauche
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
        

def colonne_pleine(colonne):
    """vérifie si la colonne que le joueur a choisie est pleine ou non"""
    global colonne_impossible
    nb_col = 0
    for i in range(m):
        if grille[i][colonne] == 1 or grille[i][colonne] == 2:
            nb_col += 1
    if nb_col == m:
        colonne_impossible = True


def grille_pleine():
    global nb_pions
    """vérifie si la grille est pleine ou non"""
    nb_pions = 0
    for i in range(m):
        for j in range(n): 
            if grille[i][j] == 1 or grille[i][j] == 2:
                nb_pions += 1
    if nb_pions == n*m:
        fin_du_jeu_nul()


def fin_du_jeu():
    """affiche quel joueur à gagner et arrête le jeu """
    global fin, une_manche
    if une_manche == False:
        fin = False
        score()
    if une_manche:
        if id_joueur == 1:
            label_gagnant.config(text=premier_joueur + " a gagné", font="20", 
                                 padx=20)
        elif id_joueur == 2:
            label_gagnant.config(text=deuxieme_joueur + " a gagné ", font="20", 
                                 padx=20)
        label_joueur.config(text="")
        fin = True


def fin_du_jeu_nul():
    """affiche qu'il n'y a aucun joueur et arrête le jeu"""
    global fin
    fin = True
    label_gagnant.config(text="Il n'y a aucun gagnant", font="20")


def dernier_coup():
    """rajoute dans une liste les coordonnées du dernier coup """
    l_coup.extend([ligne, colonne])


def retour_1():
    """annule le dernier coup et change le numéro dans la grille"""
    global retour, joueur1
    grille[l_coup[-2]][l_coup[-1]] = 0
    canvas.create_oval(l_coup[-1]*100+5, l_coup[-2]*100+5,
                       l_coup[-1]*100+100-5, l_coup[-2]*100+100-5, fill="white")
    joueur1 = not joueur1
    if joueur1:
        label_joueur.config(text="À " + premier_joueur + " de jouer") 
    else:
        label_joueur.config(text="À " + deuxieme_joueur + " de jouer") 
    del l_coup[-1]
    del l_coup[-1]
    retour = True


def sauvegarde():
    """ Ecrit dans le fichier sauvegarde.txt: la grille, le joueur qui doit jouer 
        quand on charge la partie le prénom des deux joueurs et True si 
        le jeu est terminé """ 
    global joueur_commence
    if joueur1:
        joueur_commence = premier_joueur  # joueur qui commence si on charge la partie
    else:
        joueur_commence = deuxieme_joueur
    fic = open("sauvegarde.txt", "w")
    for i in range(m):
        fic.write(str(grille[i]) + "\n")
    fic.write(joueur_commence + "," + premier_joueur + "," + deuxieme_joueur)
    if fin:
        fic.write(",True")
    fic.close() 


def charger():
    """Lit le fichier sauvegarde.txt, récupère la grille 
       et met à jour l'affichage de la grille)"""
    global charger_partie, premier_joueur, deuxieme_joueur
    global liste, grille2, grille, partie_finie
    grille1 = []  # liste qui contient tous les nombres de la grille
    grille2 = []  # liste qui contient les sous listes de nombres
    fic = open("sauvegarde.txt", "r")
    n_ligne = 0
    while True:
        ligne = fic.readline()
        n_ligne += 1
        if ligne == "":
            break
        for i in ligne:
            if i == "0" or i == "1" or i == "2":
                grille1.append(int(i))
        if n_ligne > 6:
            liste = ligne.split(",")   
            # liste contient joueur qui commence, 1er et 2eme joueur\
            # True si partie déjà finie

    for i in range(m):
        grille2.extend([[grille1[i] for i in range(n)]])
        for j in range(n):
            del grille1[0]
    fic.close()
    label_joueur.config(text="À " + liste[0] + " de jouer")
    for i in range(m):
        for j in range(n):
            if grille2[i][j] == 1:  
                canvas.create_oval(j*100+5, i*100+5, j*100+100-5,
                                   i*100+100-5, fill="gold")
            elif grille2[i][j] == 2:
                canvas.create_oval(j*100+5, i*100+5, j*100+100-5,
                                   i*100+100-5, fill="red")
    grille = grille2
    if len(liste) == 4:
        if liste[3] == "True":
            partie_finie = True


def set_match():
    """affiche label score si l'utilisateur 
       choisit de faire une compétition"""
    global label_score1, label_score2, label_manches
    global score1, score2, une_manche, nb_manches, nb_parties
    une_manche = input("jeu en une seule manche ? taper oui ou non: ")
    if une_manche == "non":
        nb_manches = input("Taper le nombre de manches: ")
        score1, score2 = 0, 0
        label_score1 = tk.Label(racine, text="score de " + premier_joueur +
                                ":" + str(score1), font="20")
        label_score2 = tk.Label(racine, text="score de " + deuxieme_joueur +
                                ":" + str(score2), font="20")
        label_manches = tk.Label(racine, text="nombre de manches: " +
                                 nb_manches)
        label_score1.grid(column=1, row=4)
        label_score2.grid(column=1, row=5) 
        label_manches.grid(column=1, row=3)
        une_manche = False
        nb_parties = 0


def score():
    """gère l'affichage des scores et renouvelle grille"""
    global grille, une_manche, nb_manches, score1, score2
    global nb_parties, premier_joueur, deuxieme_joueur, joueur1
    nb_parties += 1
    label_manches.config(text="nombre de manches: " + str(nb_manches))
    if id_joueur == 1:
        score1 += 1
        label_score1.config(text="score de " + premier_joueur + ":" +
                            str(score1))
        if score1 == int(nb_manches):
            une_manche = True
            fin_du_jeu()
    elif id_joueur == 2:
        score2 += 1
        label_score2.config(text="score de " + deuxieme_joueur + ":" +
                            str(score2))
        if score2 == int(nb_manches):
            une_manche = True
            fin_du_jeu()
    grille = []
    for i in range(m):
        grille.append([0]*n)
    if nb_parties % 2 == 0:
        joueur1 = True
    else:
        joueur1 = False
    creation_grille()
    change_premier_joueur()


def change_premier_joueur():
    """change le premier joueur qui joue à chaque manche gagnée"""
    if nb_parties % 2 == 0:
        label_joueur.config(text=premier_joueur + " commence à jouer")
    else:
        label_joueur.config(text=deuxieme_joueur + " commence à jouer")


######################
# programme principal
######################


# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, height=H, width=W, bg="blue")
bouton_retour = tk.Button(racine, command=retour_1, text="retour")
bouton_sauvegarde = tk.Button(racine, command=sauvegarde, text="sauvegarde")
label_joueur = tk.Label(racine, text=" puissance 4 ", padx=20, pady=20,
                        borderwidth=5, font=("helvetica", "20")) 
label_gagnant = tk.Label(racine)


# positionnement des widgets
racine.grid()
canvas.grid(rowspan=10)
bouton_retour.grid(column=1, row=8)
bouton_sauvegarde.grid(column=1, row=9, columnspan=2)
label_joueur.grid(column=1, row=0)
label_gagnant.grid(column=1, row=2)


# appel des fonctions
creation_grille()
choix_partie()
set_match()


# gestions clic
canvas.bind("<Button-1>", gestion_clic)


# boucle principale
racine.mainloop()
