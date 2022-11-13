"""
# =============================================================================
# compobject
# =============================================================================
Contient les objects des compétences attaques et defenses

# =============================================================================
# Auteur
# =============================================================================
Xiaowei CHEN  3971591
Yizen SUN     3970896
Hanlin LIU    3971558

# =============================================================================
# Encadrants
# =============================================================================
Florence OSSART
Thomas Dietenbeck

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
from pokemon import Competence, CompetenceAttaque, CompetenceDefence
#%% Instanciation de CompétenceAttaque
"""
l'instanciation de compétence attaque.
"""
attaque_object = []
for k in range(len(attaque_nom)):
    attaque_object.append(CompetenceAttaque(attaque_nom[k], attaque_desc[k], attaque_elem[k], attaque_cout[k], attaque_puiss[k], attaque_prec[k]))
    attaque_object[k].name = attaque_nom[k]

#Instanciation de chaque CompétenceAttaques
BecVrille = attaque_object[0]
CageEclair = attaque_object[1]
CruAiles = attaque_object[2]
Eclair = attaque_object[3]
FatalFoudre =  attaque_object[4]
Picpic = attaque_object[5]
Pique = attaque_object[6]
PoingEclair = attaque_object[7]
Tonnerre = attaque_object[8]
Tornade = attaque_object[9]
Vol = attaque_object[10]
Blizzard = attaque_object[11]
BullesdO = attaque_object[12]
Cascade = attaque_object[13]
Claquoir = attaque_object[14]
Ecume = attaque_object[15]
Hydrocanon = attaque_object[16]
LaserGlace = attaque_object[17]
OndeBoreale = attaque_object[18]
PinceMasse = attaque_object[19]
PistoletaO = attaque_object[20]
PoingGlace = attaque_object[21]
Surf = attaque_object[22]
Deflagration = attaque_object[23]
Flammeche = attaque_object[24]
LanceFlammes = attaque_object[25]
PoingFeu = attaque_object[26]
Boutefeu = attaque_object[27]
Canicule = attaque_object[28]
CrocsFeu = attaque_object[29]
FeuSacre = attaque_object[30]
Surchauffe = attaque_object[31]
PiedBruleur = attaque_object[32]
RouedeFeu = attaque_object[33]
JetPierres = attaque_object[34]
BalleGraine = attaque_object[35]
CanonGraine = attaque_object[36]
FouetLianes = attaque_object[37]
Fulmigraine = attaque_object[38]
LameFeuille = attaque_object[39]
Martobois = attaque_object[40]
Eboulement = attaque_object[41]
LamedeRoc = attaque_object[42]
RocBoulet = attaque_object[43]
Roulade = attaque_object[44]
Tomberoche = attaque_object[45]
#%% Instanciation de CompetenceDefence 
"""
l'instanciation de compétence défense.
"""
Atterrissage = CompetenceDefence(defense_nom[0], defense_desc[0], defense_elem[0], [20,50], [0,0], 10)
PileDuracell = CompetenceDefence(defense_nom[1], defense_desc[1], defense_elem[1], [0,0], [30,60], 0)
AnneauHydro = CompetenceDefence(defense_nom[2], defense_desc[2], defense_elem[2], [30,50], [0,0], 20)
FontainedeVie = CompetenceDefence(defense_nom[3], defense_desc[3], defense_elem[3], [10,30], [0,0], 10)
Aurore = CompetenceDefence(defense_nom[4], defense_desc[4], defense_elem[4], [5,25], [0,0], 5)
Sangchaud = CompetenceDefence(defense_nom[5], defense_desc[5], defense_elem[5], [10,50], [0,0], 10)
PhotoSynthese = CompetenceDefence(defense_nom[6], defense_desc[6], defense_elem[6], [0,0], [30,60], 0)
Racines = CompetenceDefence(defense_nom[7], defense_desc[7], defense_elem[7], [30,50], [30,60], 20)