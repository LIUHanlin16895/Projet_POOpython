"""
# =============================================================================
# Interface
# =============================================================================
Contient la fonction "interfaceConnexion"

# =============================================================================
# Auteur
# =============================================================================
Xiaowei CHEN  3971591
Yizen SUN     3970896
Hanlin LIU    3971558

# =============================================================================
# Encadrants
# =============================================================================
Thomas Dietenbeck
Florence OSSART

# =============================================================================
# README
# =============================================================================

"""
import random as random
from random import choice
import sys
import time
import os
from abc import ABC , abstractmethod

#%%
from compobject import*
from pokeobject import*
from opendoc import*
from pokemon import Competence, CompetenceAttaque, CompetenceDefence
from pokemon import Pokemon
from dresseur import Dresseur, IA
from dresseur import Combat, CombatJCJ, CombatJcE
from dresseur import quitter, creerNouveauDresseur, chosirPokemon, aleatoire
#%% Page d'accueil    
def interfaceConnexion():
    """
    La fonciton de la page d'accueil, comme son nom, il affiche le menu du jeu et nous permet de 
    faire plusieurs opérations, ainsi que la réalisation de la fonction après sélection.
    "Nouveau Jeu" permet de commancer un nouveaux jeu: instancier le dresseur.
    "Chargez votre jeu" permet de continuer le jeu: récupérer un dresseur souvgardé.
    """
    print('# - - - - - - - - - - - - - - - - - - - #')
    print('#        Bienvenue dans POOkemon!       #')
    print('#  Le jeu de Pokemon Oriente Object :D  #')
    print('#                                       #')
    print('#           0.Nouveau Jeu               #')
    print('#           1.Chargez votre jeu         #')
    print('#           2.Exit                      #')
    print('# - - - - - - - - - - - - - - - - - - - #')
    tousVosPokemons = []   #Créer une liste qui contient tous les pokémons possédés par le dresseur
    flag = True
    while True:
        opera = input("\nQu'est-ce que voulez vous faire ? (0-2):")
        # Voici l'opération pour créer un nouveau dresseur de jeu.
        # Nous entrons le nom du joueur, et sélectionnons le Pokémon initial.
        if opera == "0":
            nom = input("Saisissez votre nom:")
            print('Votre nom est:{}'.format(nom)), time.sleep(0.3) 
            print("{} est né!".format(nom)), print('')
            while True:
                opera2 = input("Pour l'instant, nous pouvons vous fournir six Pokémons initiaux de Niveau 1, vous pouvez(0-1) :\
                               \n\n0. Choisissez votre 6 Pokémons initiaux par vous-même. \
                                  \n1. Nous vous fournissons aléatoirement six Pokémons initiaux")
                if opera2 == "0":
                    deck, tousVosPokemons  = chosirPokemon(TousPokemons)   # Le joueur choisit 6 Pokémon soi-même
                    flag = False
                    return nom, deck, tousVosPokemons
                elif opera2 =="1":
                    deck, tousVosPokemons = aleatoire(TousPokemons)        # Il obtient six Pokémon au hasard.
                    flag = False
                    return nom, deck, tousVosPokemons
                else:
                    print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
            if not flag:break
        #Afin de recharger un dresseur, on vérifie d'abord le dossier "save" existe et nous avons déja souvgarder un dressuer.     
        elif opera == "1":
            if os.path.exists(chemin + "/save"):           # On vérifie d'abord le dossier "save" existe
                if not os.listdir(chemin + "/save") == []: # On vérifie que nous avons déja souvgarder un dressuer.
                    print("Ici votre comptes sauvgardés :") 
                    for fichier in os.listdir(chemin + "/save/"):
                        print (fichier[0:-4])
                    while True:
                        nom = input("Tapez votre nom:\n")
                        if not os.path.isfile(chemin + "/save/" + nom + ".txt"):
                            print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
                        else :                             # On récupérer les informations du dresseur et des pkémons possédés
                            lire_save = open(chemin + "/save/" + nom + ".txt").readlines()
                            pokemon_nom_save = []
                            pokemon_niveau_save = []
                            pokemon_exp_save = []
                            for i in range(3,len(lire_save)):
                                pokemon_nom_save.append(lire_save[i].split(' ')[0])
                                pokemon_niveau_save.append(lire_save[i].split(' ')[1])
                                pokemon_exp_save.append(lire_save[i].split(' ')[2])
                                for j in pokemon_object:
                                    if j.nom == pokemon_nom_save[i-3]:
                                        code1 = pokemon_nom_save.index(j.nom)
                                        j.niveau = int(pokemon_niveau_save[code1])
                                        j.exp = int(pokemon_exp_save[code1])
                                        code2 = pokemon_nom.index(j.nom)
                                        j.vie = int(vie_init[code2]) + float(vie_upgrade[code2]) * (j.niveau - int(niveau_init[code2]))
                                        j.vie_max = j.vie
                                        j.energie = int(energie_init[code2]) + float(energie_upgrade[code2]) * (j.niveau - int(niveau_init[code2]))
                                        j.energie_max = j.energie
                                        j.regene = int(regene_init[code2]) + float(regene_upgrade[code2]) * (j.niveau - int(niveau_init[code2]))
                                        j.resist = int(resist_init[code2]) + float(resist_upgrade[code2]) * (j.niveau - int(niveau_init[code2]))
                                        tousVosPokemons.append(j)
                            deck = []
                            for i in range(0,3):
                                deck.append(tousVosPokemons[pokemon_nom_save.index(lire_save[i].replace("\n",''))]) 
                            break
                    print("Bienvenue,",nom,"!\n"), time.sleep(0.3)
                    return nom, deck, tousVosPokemons
                    break
                else :
                    print("Dossier vide ! Commencez un nouveau jeux!")
                    time.sleep(0.3)
            else:
                print("Aucun compte sauvgardé ! Ressayez!")
                time.sleep(0.3)

        #quitter le jeu
        if opera == "2": quitter()
        else:
            print("\n-------------------\nInvalide! Ressayer!\n-------------------\n")
