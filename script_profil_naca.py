# ================================================================================================
# Auteur: Adrien HUYGHEBAERT
# Date: 1 juin 2024
# Générer un profil NACA symétriques à 4 chiffres (NACA00XX)
# ================================================================================================

# Importation des modules

import numpy as np
import matplotlib.pyplot as plt
from math import *


# ================================================================================================
# Fonction qui demande les caractéristiques du profil et du tracé à l'utilisateur :
# corde, nom du profil NACA (exemple NACA00XX)
# répartition des points selon la corde (uniforme ou selon la transformée de GLAUERT)
# nombre de points le long de la corde pour le tracé.

# Les boucles while True permettent de s'assurer que l'utilisateur rentre les paramètres dans les bons formats.

def entrees_utilisateur():
    print("Quel type de profil NACA symétrique à 4 chiffres voulez-vous afficher ?")
    while True:
        type_de_profil = input("Veuillez rentrer votre profil au format 'NACA00XX' (exemple : 'NACA0012') :\n")
        if len(type_de_profil) == 8 and type_de_profil.startswith('NACA') and type_de_profil[4:].isdigit():
            break
        else:
            print("Le format n'est pas bon. Veuillez réessayer.")

    while True:
        try:
            corde = float(input("\nVeuillez rentrer la corde de votre profil (en chiffres) :\n"))
            break
        except ValueError:
            print("Le format n'est pas bon. Veuillez réessayer.")

    while True:
        try:
            nombre_points = int(input("\nCombien de points souhaitez-vous le long de la corde ? \n"))
            if nombre_points > 0 and isinstance(nombre_points, int):
                break
        except ValueError:
            print("Le format n'est pas bon. "
                  "Veuillez entrer un nombre entier et supérieur à 0.")

    print(f"\nPour vos {nombre_points} points, souhaitez-vous avoir une distribution linéaire\n"
          f"ou bien selon la transformée de GLAUERT ?\n"
          f"Cette transformation est de la forme 'x_c = 0.5*(1-cos(a))' avec :\n"
          f"a qui varie de 0 à 1 et x_c la coordonnée adimensionnelle des points qui varie de 0 à 1.\n")
    while True:
        distribution = input("Veuillez rentrer 'lineaire' ou 'glauert' pour choisir votre distribution : \n")
        if distribution in ['lineaire', 'glauert']:
            break
        else:
            print("Rentrée invalide. Veuillez réessayer.")

    return type_de_profil, corde, nombre_points, distribution


# ================================================================================================
# Fonction qui créée la liste des points x_c si la distribution selon la tranformée de GLAUERT est choisie

def creer_liste_distribution_points(nombre_points):
    theta = np.linspace(0, pi, nombre_points)
    x_c = [(0.5 * (1 - cos(angles_theta))) for angles_theta in theta]

    return x_c


# ================================================================================================
# Fonction qui créée les tableau des points pour l'extrados et de l'intrados du profil

def creer_tableaux_extrados_intrados(corde, t, x_c):
    # Initialisation des tableaux (x_c lignes et 2 colonnes en float)
    tableau_extrados = np.zeros((len(x_c), 2), float)
    tableau_intrados = np.zeros((len(x_c), 2), float)

    for i in range(len(x_c)):
        y = 5 * t * (0.2969 * sqrt(x_c[i]) - 0.1260 * x_c[i] - 0.3516 * x_c[i] ** 2
                     + 0.2843 * (x_c[i]) ** 3 - 0.1038 * (x_c[i]) ** 4)
        x_reel = x_c[i] * corde
        tableau_extrados[i] = [x_reel, y * corde]
        tableau_intrados[i] = [x_reel, - y * corde]

    return tableau_extrados, tableau_intrados


# ================================================================================================
# Fonction qui affiche les informations relatives au profil :
# nom du profil, épaisseur maximale et position selon la corde.

def afficher_informations_profil(type_de_profil):
    print(f"")


# ================================================================================================
# Fonction principale

def profil_naca():
    type_de_profil, corde, nombre_points, distribution = entrees_utilisateur()

    # Récupération des deux derniers chiffres du profil NACA
    # qui correspondent à l'épaisseur maximale du profil.
    # t correspond a son pourcentage.
    t = int(type_de_profil[-2:]) / 100

    if distribution == 'glauert':
        x_c = creer_liste_distribution_points(nombre_points)
    else:
        x_c = np.linspace(0, 1, nombre_points)

    tableau_extrados, tableau_intrados = creer_tableaux_extrados_intrados(corde, t, x_c)


# ================================================================================================
# Appel de la fonction princpale

profil_naca()
