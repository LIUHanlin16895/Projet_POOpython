"""
# =============================================================================
# Projet Programmation Orientée Objet - POOkemon
# =============================================================================
14/01/2022

# =============================================================================
# Auteurs
# =============================================================================
Parcours SAR
Hanlin LIU    3971558  hanlin.liu@etu.sorbonne-universite.fr
Xiaowei CHEN  3971591
Yizen SUN     3970896

# =============================================================================
# Encadrants
# =============================================================================
Florence OSSART
Thomas Dietenbeck

# =============================================================================
# README
# =============================================================================

0.En raison du problème de l'ordinateur d'un de nos membres, nous essayons de convertir 
la fichier "defence" et "attaque" en format ".csv", et ça marche.

Vous pouvez trouver les codes qui importent ces deux fichiers ".cvs" dans 
le fichier "opendoc" line "106" et "138", s'il vous plaît.

1.Pour les options proposés, nous avons choisit à réaliser la fonction d'évolution.

2.Afin de faciliter votre test pour l'augmentation de niveau, nous essayons de augement 
la valeur de l'expérience quand le pokmeon gagner l'expérience. (Parce qu'on trouve c'est vraiment très lent)

Si vous voulez le modofier, c'est dans le fichier "pokemon" line "179" et "188", s'il vous plaît.

3.Enfin,si le programme rencontre un bug, vous pouvez essayer le programme "ProgrammeTousEnsemble"
qui contient tous les class et les fonctions dedans ensemble.

"""
#%%Importer les bibliotheques utilisés
import random as random
from random import choice
import sys
import time
import os
from abc import ABC , abstractmethod
#%% Importer les dossier
from compobject import*
from pokeobject import*
from opendoc import*
from pokemon import Pokemon
from pokemon import Competence, CompetenceAttaque, CompetenceDefence
from dresseur import Dresseur, IA
from dresseur import Combat, CombatJCJ, CombatJcE
from dresseur import quitter, creerNouveauDresseur, chosirPokemon, aleatoire
from interface import interfaceConnexion

#%% Programme principal
nom, deck, tousVosPokemons= interfaceConnexion() # Exécuter l'écran d'accueil et récupérer les informations du dresseur
player=Dresseur(nom,deck,tousVosPokemons)        # Instancier le dresseur 

while True:
    time.sleep(0.5)
    player.menu()