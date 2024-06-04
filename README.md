## Objectif du code :
Ce script a pour but de générer un profil NACA symétrique à 4 chiffres et donner l'épaisseur maximale ainsi que sa position en pourcentage de corde.

## Comment utiliser le code :
L'utilisateur doit seulement rentrer les informations nécéssaires à la génération du profil : 

- le type de profil NACA qu'il souhaite générer (exemple : NACA0012),
- la longueur de la corde du profil ainsi que son unité,
- le nombre de points nécessaires pour générer le graphique,
- et la distribution de ces derniers de façon linéaire ou selon la transformée de GLAUERT.

## Structure du code: 
La structure est composée de plusieurs fonctions qui s'imbriquent les unes aux autes:

### entrees_utilisateur()
Cette fonction permet de recueillir les informations de l'utilisateru afin de générer le profil.\
Elle est composée de boucles "while True" qui permettent de s'assurer que l'utilsateur rentre les paramètres dans les bons formats.\
Elle retourne les paramètres type_de_profil , corde, unite_corde, nombre_de_points et distribution.

### creer_liste_distribution_points(nombre_points)
Cette fonction n'est utilisée que si l'utilisateur choisi d'utiliser la transformée de GLAUERT pour la distribution des points.\
Cette transformation est de la forme 'x_c = 0.5*(1-cos(a))' avec : x_c la coordonnée adimensionnelle des points qui varie de 0 à 1 et a qui varie de 0 à 1.\
Elle retourne le paramètre x_c.

### creer_tableaux_extrados_intrados(corde, t, x_c)
Cette fonction permet de générer le tableau des points de l'intrados et celui des points de l'extrados.\
Les tableaux sont de la taille x_c lignes et 2 colonnes.\
Elle retourne les paramètres : tableau_extrados et tableau_intrados.

### afficher_informations_profil(type_de_profil, corde, unite_corde, tableau_extrados)
Cette fonction afficher à l'utilsateur les informations de son profil (type de profil, corde) et calcul + affiche l'épaisseur maximale du profil ainsi que sa position en pourcentage de corde.\
Elle retourne les paramètres : x_epaisseur_max et y_epaisseur_max.

### afficher_graphique(corde, unite_corde, type_de_profil, x_c, tableau_extrados, tableau_intrados, x_epaisseur_max, y_epaisseur_max)
Cette procédure génère un graphique avec le profil de l'utilisateur ainsi que le point d'épaisseur maximale.

### profil_naca()
C'est la fonction principale qui appelle successivement les fonctions citées plus haut pour remplir l'objectif du script.
