# On ouvre le ficher texte
fichier_texte = open("Laby.txt", "r")# r = on lit le texte
print(fichier_texte)

map1 = []
ligne_map = []
compteur=0
for lignes in fichier_texte:
    ligne_map = []
    # On lit chaque charactere du fichier
    for charactere in lignes:
        if charactere != "\n" :
            ligne_map.append(charactere)
            #print(ligne_map)
    map1.append(ligne_map)
    #print("map1",compteur)
    #print(map1)
    compteur=compteur+1

# Nombre de ligne
nb_ligne=15
nb_colonne=15

# Dimention fenetre
longueur_fenetre = 600
hauteur_fenetre = 600

# Dimention case
longueur_case = longueur_fenetre // nb_ligne
hauteur_case = hauteur_fenetre // nb_colonne

position_mur = (0,0)
position_pixel_mort = (0,0)

position_perso_map_V=0
position_perso_map_H=0

position_objet_map_V=0
position_objet_map_H=0

position_pixel_gagnez = (0, 0)
position_pixel_mort = (0, 0)

