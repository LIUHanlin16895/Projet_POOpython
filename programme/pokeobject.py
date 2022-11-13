"""
# =============================================================================
# pokeobject
# =============================================================================
Contient les objects de pokémon N°1, N°2, N°3

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
from opendoc import*
from pokemon import Pokemon
from compobject import*

#%% Instanciation de la liste des Pokémon
"""
l'instanciation de pokemon, cet ensemble de pokemon est utilisé par "vous", c'est à dire le dresseur.
"""
pokemon_object = []
for k in range(len(pokemon_nom)):
    pokemon_object.append(Pokemon(pokemon_nom[k], liste_element[k], niveau_init[k], 0, (vie_init[k]), energie_init[k], regene_init[k], resist_init[k], liste_competence[k], None))
    pokemon_object[k].name = pokemon_nom[k]

#Instanciation de chaque Pokémon
Pikachu = pokemon_object[0]
Raichu = pokemon_object[1]
Roucool = pokemon_object[2]
Roucoups = pokemon_object[3]
Roucarnage = pokemon_object[4]
Carapuce = pokemon_object[5]
Carabaffe = pokemon_object[6]
Tortank = pokemon_object[7]
Psykokwak = pokemon_object[8]
Akwakwak = pokemon_object[9]
Ptitard = pokemon_object[10]
Tetarte = pokemon_object[11]
Tartard = pokemon_object[12]
Salameche = pokemon_object[13]
Reptincel = pokemon_object[14]
Dracaufeu = pokemon_object[15]
Goupix = pokemon_object[16]
Feunard = pokemon_object[17]
Ponyta = pokemon_object[18]
Galopa = pokemon_object[19]
Bulbizarre = pokemon_object[20]
Herbizarre = pokemon_object[21]
Florizarre = pokemon_object[22]
Sabelette = pokemon_object[23]
Sablaireau = pokemon_object[24]
Nidoran = pokemon_object[25]
Nidorina = pokemon_object[26]
Nidoqueen = pokemon_object[27]

#Définir les compétences de pokemon et leur "object" de "apres_evolution".
Pikachu.competence, Pikachu.apres_evolution = [Eclair,Tonnerre, CageEclair], Raichu
Raichu.competence = [Eclair,Tonnerre, CageEclair, FatalFoudre, PileDuracell]
Roucool.competence, Roucool.apres_evolution= [BecVrille,Vol, Picpic], Roucoups
Roucoups.competence, Roucoups.apres_evolution = [BecVrille,Vol, Picpic, CruAiles], Roucarnage
Roucarnage.competence = [BecVrille,Vol, Picpic, CruAiles, Tornade]
Carapuce.competence, Carapuce.apres_evolution = [BullesdO,Ecume, Surf], Carabaffe
Carabaffe.competence,Carabaffe.apres_evolution  = [BullesdO,Ecume, Surf, Cascade], Tortank
Tortank.competence = [BullesdO,Ecume, Surf, Cascade, Hydrocanon]
Psykokwak.competence, Psykokwak.apres_evolution = [OndeBoreale, PinceMasse,PoingGlace ], Akwakwak
Akwakwak.competence = [OndeBoreale, PinceMasse,PoingGlace ]
Ptitard.competence, Ptitard.apres_evolution = [BullesdO, Ecume, OndeBoreale], Tetarte
Tetarte.competence, Tetarte.apres_evolution = [BullesdO, Ecume, OndeBoreale, PoingGlace], Tartard
Tartard.competence = [BullesdO, Ecume, OndeBoreale, PoingGlace, FontainedeVie]
Salameche.competence, Salameche.apres_evolution = [CrocsFeu, PoingFeu, Flammeche], Reptincel
Reptincel.competence, Reptincel.apres_evolution = [CrocsFeu, PoingFeu, Flammeche, Deflagration], Dracaufeu
Dracaufeu.competence = [CrocsFeu, PoingFeu, Flammeche, Deflagration, LanceFlammes]
Goupix.competence, Goupix.apres_evolution = [PoingFeu, FeuSacre, CrocsFeu], Feunard
Feunard.competence =[PoingFeu, FeuSacre, CrocsFeu, RouedeFeu,Aurore ]
Ponyta.competence, Ponyta.apres_evolution = [Canicule, PiedBruleur, Boutefeu], Galopa
Galopa.competence = [Canicule, PiedBruleur, Boutefeu, RouedeFeu, Sangchaud]
Bulbizarre.competence, Bulbizarre.apres_evolution = [Fulmigraine,CanonGraine, BalleGraine], Herbizarre
Herbizarre.competence, Herbizarre.apres_evolution = [Fulmigraine,CanonGraine, BalleGraine, FouetLianes], Florizarre
Florizarre.competence = [Fulmigraine,CanonGraine, BalleGraine, FouetLianes, LameFeuille]
Sabelette.competence, Sabelette.apres_evolution = [JetPierres,LamedeRoc, RocBoulet ], Sablaireau
Sablaireau.competence = [JetPierres,LamedeRoc, RocBoulet, Tomberoche, Racines ]
Nidoran.competence, Nidoran.apres_evolution = [Roulade,Martobois, Eboulement ], Nidorina
Nidorina.competence, Nidorina.apres_evolution = [Roulade,Martobois, Eboulement, Tomberoche ], Nidoqueen
Nidoqueen.competence = [Roulade,Martobois, Eboulement, Tomberoche, PhotoSynthese ]

#Etablir un ensemble des pokemon
pokemon_object = [Pikachu, Raichu, Roucool,Roucoups, Roucarnage, Carapuce, Carabaffe,\
                  Tortank,Psykokwak, Akwakwak,  Ptitard,Tetarte, Tartard, Salameche,Reptincel,Dracaufeu,\
                      Goupix, Feunard,Ponyta, Galopa, Bulbizarre, Herbizarre, Florizarre, Sabelette, Sablaireau, Nidoran, Nidorina, Nidoqueen ]
TousPokemons = pokemon_object

#Classification des pokemons par rapport à leur niveau initiale
PokeNiveau1 = [Pikachu, Roucool, Carapuce,Psykokwak,Ptitard,Salameche,Goupix,Ponyta, Bulbizarre,Sabelette,Nidoran]
PokeNiveau6 = [Raichu,Roucoups, Carabaffe,Akwakwak,Tetarte,Reptincel,Feunard,Galopa,Herbizarre,Sablaireau,Nidorina]
PokeNiveau10 = [Roucarnage,Tortank,Tartard,Dracaufeu,Florizarre,Nidoqueen]
#%% L'instanciation d'un Pokémon sauvage
"""
Cet ensemble de pokemon N°2 est utilisé dans le combat Joueur contre pokemon, comme les pokemons sauvages
"""
pokemon_object_N2 = []
for k in range(len(pokemon_nom)):
    pokemon_object_N2.append(Pokemon(pokemon_nom[k], liste_element[k], niveau_init[k], 0, (vie_init[k]), energie_init[k], regene_init[k], resist_init[k], liste_competence[k], None))
    pokemon_object_N2[k].name = pokemon_nom[k]

Pikachu_N2 = pokemon_object_N2[0]
Raichu_N2 = pokemon_object_N2[1]
Roucool_N2 = pokemon_object_N2[2]
Roucoups_N2 = pokemon_object_N2[3]
Roucarnage_N2 = pokemon_object_N2[4]
Carapuce_N2 = pokemon_object_N2[5]
Carabaffe_N2 = pokemon_object_N2[6]
Tortank_N2 = pokemon_object_N2[7]
Psykokwak_N2 = pokemon_object_N2[8]
Akwakwak_N2 = pokemon_object_N2[9]
Ptitard_N2 = pokemon_object_N2[10]
Tetarte_N2 = pokemon_object_N2[11]
Tartard_N2 = pokemon_object_N2[12]
Salameche_N2 = pokemon_object_N2[13]
Reptincel_N2 = pokemon_object_N2[14]
Dracaufeu_N2 = pokemon_object_N2[15]
Goupix_N2 = pokemon_object_N2[16]
Feunard_N2 = pokemon_object_N2[17]
Ponyta_N2 = pokemon_object_N2[18]
Galopa_N2 = pokemon_object_N2[19]
Bulbizarre_N2 = pokemon_object_N2[20]
Herbizarre_N2 = pokemon_object_N2[21]
Florizarre_N2 = pokemon_object_N2[22]
Sabelette_N2 = pokemon_object_N2[23]
Sablaireau_N2 = pokemon_object_N2[24]
Nidoran_N2 = pokemon_object_N2[25]
Nidorina_N2 = pokemon_object_N2[26]
Nidoqueen_N2 = pokemon_object_N2[27]

Pikachu_N2.competence, Pikachu_N2.apres_evolution = [Eclair,Tonnerre, CageEclair], Raichu_N2
Raichu_N2.competence = [Eclair,Tonnerre, CageEclair, FatalFoudre, PileDuracell]
Roucool_N2.competence, Roucool_N2.apres_evolution= [BecVrille,Vol, Picpic], Roucoups_N2
Roucoups_N2.competence, Roucoups_N2.apres_evolution = [BecVrille,Vol, Picpic, CruAiles], Roucarnage_N2
Roucarnage_N2.competence = [BecVrille,Vol, Picpic, CruAiles, Tornade]
Carapuce_N2.competence, Carapuce_N2.apres_evolution = [BullesdO,Ecume, Surf], Carabaffe_N2
Carabaffe_N2.competence,Carabaffe_N2.apres_evolution  = [BullesdO,Ecume, Surf, Cascade], Tortank_N2
Tortank_N2.competence = [BullesdO,Ecume, Surf, Cascade, Hydrocanon]
Psykokwak_N2.competence, Psykokwak_N2.apres_evolution = [OndeBoreale, PinceMasse,PoingGlace ], Akwakwak_N2
Akwakwak_N2.competence = [OndeBoreale, PinceMasse,PoingGlace ]
Ptitard_N2.competence, Ptitard_N2.apres_evolution = [BullesdO, Ecume, OndeBoreale], Tetarte_N2
Tetarte_N2.competence, Tetarte.apres_evolution = [BullesdO, Ecume, OndeBoreale, PoingGlace], Tartard_N2
Tartard_N2.competence = [BullesdO, Ecume, OndeBoreale, PoingGlace, FontainedeVie]
Salameche_N2.competence, Salameche_N2.apres_evolution = [CrocsFeu, PoingFeu, Flammeche], Reptincel_N2
Reptincel_N2.competence, Reptincel_N2.apres_evolution = [CrocsFeu, PoingFeu, Flammeche, Deflagration], Dracaufeu_N2
Dracaufeu_N2.competence = [CrocsFeu, PoingFeu, Flammeche, Deflagration, LanceFlammes]
Goupix_N2.competence, Goupix_N2.apres_evolution = [PoingFeu, FeuSacre, CrocsFeu], Feunard_N2
Feunard_N2.competence =[PoingFeu, FeuSacre, CrocsFeu, RouedeFeu,Aurore ]
Ponyta_N2.competence, Ponyta_N2.apres_evolution = [Canicule, PiedBruleur, Boutefeu], Galopa_N2
Galopa_N2.competence = [Canicule, PiedBruleur, Boutefeu, RouedeFeu, Sangchaud]
Bulbizarre_N2.competence, Bulbizarre_N2.apres_evolution = [Fulmigraine,CanonGraine, BalleGraine], Herbizarre_N2
Herbizarre_N2.competence, Herbizarre_N2.apres_evolution = [Fulmigraine,CanonGraine, BalleGraine, FouetLianes], Florizarre_N2
Florizarre_N2.competence = [Fulmigraine,CanonGraine, BalleGraine, FouetLianes, LameFeuille]
Sabelette_N2.competence, Sabelette_N2.apres_evolution = [JetPierres,LamedeRoc, RocBoulet ], Sablaireau_N2
Sablaireau_N2.competence = [JetPierres,LamedeRoc, RocBoulet, Tomberoche, Racines ]
Nidoran_N2.competence, Nidoran_N2.apres_evolution = [Roulade,Martobois, Eboulement ], Nidorina_N2
Nidorina_N2.competence, Nidorina_N2.apres_evolution = [Roulade,Martobois, Eboulement, Tomberoche ], Nidoqueen_N2
Nidoqueen_N2.competence = [Roulade,Martobois, Eboulement, Tomberoche, PhotoSynthese ]

#Etablir un ensemble des pokemon
pokemon_object_N2 = [Pikachu_N2, Raichu_N2, Roucool_N2,Roucoups_N2, Roucarnage_N2, Carapuce_N2, Carabaffe_N2,\
                  Tortank_N2,Psykokwak_N2, Akwakwak_N2,  Ptitard_N2,Tetarte_N2, Tartard_N2, Salameche_N2,Reptincel_N2,Dracaufeu_N2,\
                      Goupix_N2, Feunard_N2,Ponyta_N2, Galopa_N2, Bulbizarre_N2, Herbizarre_N2, Florizarre_N2, Sabelette_N2, Sablaireau_N2, Nidoran_N2, Nidorina_N2, Nidoqueen_N2 ]
TousPokemons_N2 = pokemon_object_N2

#%% L'instanciation d'un Pokémon de dresseur 2
"""
Cet ensemble de pokemon N°3 est utilisé par le dresseur "adversaire" dans le Combat Joueur contre Joueur.
"""
pokemon_object_N3 = []
for k in range(len(pokemon_nom)):
    pokemon_object_N3.append(Pokemon(pokemon_nom[k], liste_element[k], niveau_init[k], 0, (vie_init[k]), energie_init[k], regene_init[k], resist_init[k], liste_competence[k], None))
    pokemon_object_N3[k].name = pokemon_nom[k]

Pikachu_N3 = pokemon_object_N3[0]
Raichu_N3 = pokemon_object_N3[1]
Roucool_N3 = pokemon_object_N3[2]
Roucoups_N3 = pokemon_object_N3[3]
Roucarnage_N3 = pokemon_object_N3[4]
Carapuce_N3 = pokemon_object_N3[5]
Carabaffe_N3 = pokemon_object_N3[6]
Tortank_N3 = pokemon_object_N3[7]
Psykokwak_N3 = pokemon_object_N3[8]
Akwakwak_N3 = pokemon_object_N3[9]
Ptitard_N3 = pokemon_object_N3[10]
Tetarte_N3 = pokemon_object_N3[11]
Tartard_N3 = pokemon_object_N3[12]
Salameche_N3 = pokemon_object_N3[13]
Reptincel_N3 = pokemon_object_N3[14]
Dracaufeu_N3 = pokemon_object_N3[15]
Goupix_N3 = pokemon_object_N3[16]
Feunard_N3 = pokemon_object_N3[17]
Ponyta_N3 = pokemon_object_N3[18]
Galopa_N3 = pokemon_object_N3[19]
Bulbizarre_N3 = pokemon_object_N3[20]
Herbizarre_N3 = pokemon_object_N3[21]
Florizarre_N3 = pokemon_object_N3[22]
Sabelette_N3 = pokemon_object_N3[23]
Sablaireau_N3 = pokemon_object_N3[24]
Nidoran_N3 = pokemon_object_N3[25]
Nidorina_N3 = pokemon_object_N3[26]
Nidoqueen_N3 = pokemon_object_N3[27]

Pikachu_N3.competence, Pikachu_N3.apres_evolution = [Eclair,Tonnerre, CageEclair], Raichu_N3
Raichu_N3.competence = [Eclair,Tonnerre, CageEclair, FatalFoudre, PileDuracell]
Roucool_N3.competence, Roucool_N3.apres_evolution= [BecVrille,Vol, Picpic], Roucoups_N3
Roucoups_N3.competence, Roucoups_N3.apres_evolution = [BecVrille,Vol, Picpic, CruAiles], Roucarnage_N3
Roucarnage_N3.competence = [BecVrille,Vol, Picpic, CruAiles, Tornade]
Carapuce_N3.competence, Carapuce_N3.apres_evolution = [BullesdO,Ecume, Surf], Carabaffe_N3
Carabaffe_N3.competence,Carabaffe_N3.apres_evolution  = [BullesdO,Ecume, Surf, Cascade], Tortank_N3
Tortank_N3.competence = [BullesdO,Ecume, Surf, Cascade, Hydrocanon]
Psykokwak_N3.competence, Psykokwak_N3.apres_evolution = [OndeBoreale, PinceMasse,PoingGlace ], Akwakwak_N3
Akwakwak_N3.competence = [OndeBoreale, PinceMasse,PoingGlace ]
Ptitard_N3.competence, Ptitard_N3.apres_evolution = [BullesdO, Ecume, OndeBoreale], Tetarte_N3
Tetarte_N3.competence, Tetarte.apres_evolution = [BullesdO, Ecume, OndeBoreale, PoingGlace], Tartard_N3
Tartard_N3.competence = [BullesdO, Ecume, OndeBoreale, PoingGlace, FontainedeVie]
Salameche_N3.competence, Salameche_N3.apres_evolution = [CrocsFeu, PoingFeu, Flammeche], Reptincel_N3
Reptincel_N3.competence, Reptincel_N3.apres_evolution = [CrocsFeu, PoingFeu, Flammeche, Deflagration], Dracaufeu_N3
Dracaufeu_N3.competence = [CrocsFeu, PoingFeu, Flammeche, Deflagration, LanceFlammes]
Goupix_N3.competence, Goupix_N3.apres_evolution = [PoingFeu, FeuSacre, CrocsFeu], Feunard_N3
Feunard_N3.competence =[PoingFeu, FeuSacre, CrocsFeu, RouedeFeu,Aurore ]
Ponyta_N3.competence, Ponyta_N3.apres_evolution = [Canicule, PiedBruleur, Boutefeu], Galopa_N3
Galopa_N3.competence = [Canicule, PiedBruleur, Boutefeu, RouedeFeu, Sangchaud]
Bulbizarre_N3.competence, Bulbizarre_N3.apres_evolution = [Fulmigraine,CanonGraine, BalleGraine], Herbizarre_N3
Herbizarre_N3.competence, Herbizarre_N3.apres_evolution = [Fulmigraine,CanonGraine, BalleGraine, FouetLianes], Florizarre_N3
Florizarre_N3.competence = [Fulmigraine,CanonGraine, BalleGraine, FouetLianes, LameFeuille]
Sabelette_N3.competence, Sabelette_N3.apres_evolution = [JetPierres,LamedeRoc, RocBoulet ], Sablaireau_N3
Sablaireau_N3.competence = [JetPierres,LamedeRoc, RocBoulet, Tomberoche, Racines ]
Nidoran_N3.competence, Nidoran_N3.apres_evolution = [Roulade,Martobois, Eboulement ], Nidorina_N3
Nidorina_N3.competence, Nidorina_N3.apres_evolution = [Roulade,Martobois, Eboulement, Tomberoche ], Nidoqueen_N3
Nidoqueen_N3.competence = [Roulade,Martobois, Eboulement, Tomberoche, PhotoSynthese ]

#Etablir un ensemble des pokemon
pokemon_object_N3 = [Pikachu_N3, Raichu_N3, Roucool_N3,Roucoups_N3, Roucarnage_N3, Carapuce_N3, Carabaffe_N3,\
                  Tortank_N3,Psykokwak_N3, Akwakwak_N3,  Ptitard_N3,Tetarte_N3, Tartard_N3, Salameche_N3,Reptincel_N3,Dracaufeu_N3,\
                      Goupix_N3, Feunard_N3,Ponyta_N3, Galopa_N3, Bulbizarre_N3, Herbizarre_N3, Florizarre_N3, Sabelette_N3, Sablaireau_N3, Nidoran_N3, Nidorina_N3, Nidoqueen_N3 ]
TousPokemons_N3 = pokemon_object_N3    

#Classification des pokemons par rapport à leur niveau initiale
PokeNiveau1_N3 = [Pikachu_N3, Roucool_N3, Carapuce_N3,Psykokwak_N3,Ptitard_N3,Salameche_N3,Goupix_N3,Ponyta_N3, Bulbizarre_N3,Sabelette_N3,Nidoran_N3]
PokeNiveau6_N3 = [Raichu_N3,Roucoups_N3, Carabaffe_N3,Akwakwak_N3,Tetarte_N3,Reptincel_N3,Feunard_N3,Galopa_N3,Herbizarre_N3,Sablaireau_N3,Nidorina_N3]
PokeNiveau10_N3 = [Roucarnage_N3,Tortank_N3,Tartard_N3,Dracaufeu_N3,Florizarre_N3,Nidoqueen_N3]