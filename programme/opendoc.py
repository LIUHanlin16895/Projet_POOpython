"""
# =============================================================================
# opendoc
# =============================================================================
Ouvrir et lire les dossiers

# =============================================================================
# Auteur
# =============================================================================
Hanlin LIU    3971558
Xiaowei CHEN   3971591
Yizen SUN     3970896


# =============================================================================
# Encadrants
# =============================================================================
Thomas Dietenbeck
Florence OSSART

# =============================================================================
# README
# =============================================================================
Si le programme ne réussite pas à lire les dossiers , veuiller modifiler le format 
du dossier ".cvs" à ".txt" dans le programme line 105 et 137, s'il vous plaît.
"""

import random as random
from random import choice
import sys
import time
import os
from abc import ABC , abstractmethod

#%%
chemin = os.getcwd()
#%% lire les informations dans le fichier "Pokemons".

# Construire les tableaus de l'information du Pokemon
pokemon_nom=[]        # Nom de Pokemon
liste_competence=[]   # La compétence de Pokemon
liste_element=[]      # L'élément de Pokemon
niveau_init=[]        # Le niveau initial de Pokemon
niveau_max=[]         # Le niveau maximal de Pokemon
vie_init = []         # La vie initiale de Pokemon
vie_max = []          # La vie maximale de Pokemon
vie_upgrade = []      # La vie augmentée à chaque niveau
energie_init =[]      # L'énergie initiale de Pokemon
energie_max = []      # L'énergie maximale de  Pokemon
energie_upgrade=[]    # L'energie augmentée à chaque niveau
regene_init = []      # La valeur initiale de la régénération
regene_max =[]        # La valeur maximale de la régénération
regene_upgrade=[]     # La régénération augmentée à chaque niveau
resist_init = []      # La résistance initiale de Pokemon
resist_max = []       # La résistance initiale de Pokemons
resist_upgrade=[]     # La résistance augmentée à chaque niveau

# Ouvrir le fichier 'Pokémon', Lire les données.
# =============================================================================
# try: 
#     donnees_pokemon = open(chemin + '/pokemon.txt').readlines()
# except:
#     donnees_pokemon = open(chemin + '/pokemon.csv').readlines()
# =============================================================================
    
donnees_pokemon= open(chemin + '/pokemon.txt').readlines() 

# Récupérer les informations de chaque Pokemon
for i in range(1,len(donnees_pokemon)):
    pokemon_nom.append(donnees_pokemon[i].split('\t')[0])
    liste_element.append(donnees_pokemon[i].split('\t')[3])
    niveau_init.append(donnees_pokemon[i].split('\t')[4].split('-')[0])
    niveau_max.append(int(donnees_pokemon[i].split('\t')[4].split('-')[1]))
    vie_init.append(donnees_pokemon[i].split('\t')[5].split('-')[0])
    vie_max.append(donnees_pokemon[i].split('\t')[5].split('-')[1])
    vie_upgrade.append(int(int(donnees_pokemon[i].split('\t')[5].split('-')[1])-int(donnees_pokemon[i].split('\t')[5].split('-')[0]))/4)
    energie_init.append((donnees_pokemon[i].split('\t')[6].split('-')[0]))
    energie_max.append(donnees_pokemon[i].split('\t')[6].split('-')[1])
    energie_upgrade.append(int(int(donnees_pokemon[i].split('\t')[6].split('-')[1])-int(donnees_pokemon[i].split('\t')[6].split('-')[0]))/4)
    regene_init.append(donnees_pokemon[i].split('\t')[7].split('-')[0])
    regene_max.append(donnees_pokemon[i].split('\t')[7].split('-')[1])
    regene_upgrade.append(int(int(donnees_pokemon[i].split('\t')[7].split('-')[1])-int(donnees_pokemon[i].split('\t')[7].split('-')[0]))/4)
    resist_init.append(donnees_pokemon[i].split('\t')[8].split('-')[0])
    resist_max.append(donnees_pokemon[i].split('\t')[8].split('-')[1])
    resist_upgrade.append(int(int(donnees_pokemon[i].split('\t')[8].split('-')[1])-int(donnees_pokemon[i].split('\t')[8].split('-')[0]))/4)
    liste_competence.append(donnees_pokemon[i].split('\t')[9].replace('[','').replace(']','').split(','))

#%% Le fichier 'defense'

# Construire les tableaux de la compétence défensee
defense_nom = []     # Le nom de la compétence défensee
defense_desc =[]     # La description de la compétence défensee
defense_elem = []    # L'élement de la compétence défensee
defense_soin = []    # La valeur de soin
defense_energie = [] # La valeur d'énergie
defense_cout = []    # La valeur de cour

# Ouvrir le fichier, Lire les données

# =============================================================================
# try: 
#     dossier_defence = open(chemin + '/defense.txt').readlines()
# except:
#     dossier_defence = open(chemin + '/defense.csv').readlines()
# =============================================================================
dossier_defence = open(chemin + '/defense.csv').readlines()

for i in range(len(dossier_defence )):
    dossier_defence [i] = dossier_defence [i].split(';')

# récupérer les informations  
for i in range(1,len(dossier_defence)):
    defense_nom.append(dossier_defence [i][0])
    defense_desc.append(dossier_defence [i][1])
    defense_elem.append(dossier_defence [i][2])
    defense_soin.append(dossier_defence [i][3])
    defense_energie.append(dossier_defence [i][4])
    defense_cout.append(dossier_defence [i][5])
#%% le fichier 'attack '

# Construire les tableaux de la compétence attack
attaque_nom = []    # Le nom
attaque_desc =[]    # La description de la compétence attack
attaque_elem = []   # L'élément de la compétence attack
attaque_puiss = []  # La puissance de la compétence attack
attaque_prec = []   # La precision de la compétence attack
attaque_cout = []   # Le cout de la compétence attack

# Ouvrir le fichier, Lire les données

# =============================================================================
# try: 
#     dossier_attaque = open(chemin + '/attaque.txt').readlines()
# except:
#     dossier_attaque = open(chemin + '/attaque.csv').readlines()
# =============================================================================
    
dossier_attaque = open(chemin + '/attaque.csv').readlines()

for i in range(len(dossier_attaque)):
    dossier_attaque[i] = dossier_attaque[i].split(';')

# récupérer les informations  
for i in range(1,len(dossier_attaque)):
    attaque_nom.append(dossier_attaque[i][0])
    attaque_desc.append(dossier_attaque[i][1])
    attaque_elem.append(dossier_attaque[i][2])
    attaque_puiss.append(int(dossier_attaque[i][3]))
    attaque_prec.append(int(dossier_attaque[i][4]))
    attaque_cout.append(int(dossier_attaque[i][5]))