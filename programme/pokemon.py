"""
# =============================================================================
# pokemon
# =============================================================================
Contient:
la class "Pokemon"
les class "Competence, CompetenceAttaque, CompetenceDefence"

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
#%%

class Pokemon:
    def __init__(self, nom, elem, niveau, exp, vie, energie, regene, resist, competence, apres_evolution):
        self.__nom = nom     # le nom du Pokemon
        self.__elem = elem   # l'élement du Pokemon
        self.__niveau = int(niveau)           # Le niveau du Pokemon 
        self.__niveau_max = self.__niveau + 5 # Le niveau maximal actuel du Pokemon
        self.__exp = int(exp)                 # L'expérience du Pokemon
        self.__vie = int(vie)                 # La vie du Pokemon
        self.__energie = int(energie)  # L'énergie du Pokemon
        self.__regene = int(regene)    # La régénération du Pokemon
        self.__resist = int(resist)    # La résistance du Pokemon
        self.__competence = competence # Les compétences du Pokemon
        
        # "self._apres_evolution" est un object, qui représente le Pokémon évolué du Pokémon actuel.
        # Si ce Pokémon ne peut pas continuer à évoluer, alors "self._apres_evolution" = None.
        self.__apres_evolution = apres_evolution 
        # Obtenir la position du Pokémon dans la liste de tous les pokémons
        self.__numero = pokemon_nom.index(self.__nom)   
        
        # Conserver la valeur de vie maximale et d'énergie maximale 
        # Il sert à restaurer la vie et l'énergie à maximum avant le Cambat
        self.__vie_max = int(vie)         # La vie maximale du Pokemon 
        self.__energie_max = int(energie) # L'energie maximale du Pokemon
        
    @property
    def nom (self): return  self.__nom
    @property
    def elem (self): return  self.__elem
    @property
    def niveau (self): return  self.__niveau
    @property 
    def exp (self) : return self.__exp
    @property
    def vie (self): return  self.__vie
    @property
    def energie (self): return  self.__energie
    @property 
    def regene (self) : return self.__regene
    @property
    def resist (self): return  self.__resist
    @property
    def competence(self): return self.__competence
    @property
    def vie_max(self) : return self.__vie_max
    @property
    def energie_max(self) : return self.__energie_max
    @property 
    def apres_evolution(self): return self.__apres_evolution
    @property 
    def numero(self): return self.__numero
    
    @vie.setter
    def vie (self, vie): self.__vie = vie
    @energie.setter 
    def energie(self, energie) : self.__energie = energie
    @vie_max.setter
    def vie_max (self, vie_max): self.__vie_max = vie_max
    @energie_max.setter 
    def energie_max(self, energie_max) : self.__energie_max = energie_max
    @regene.setter 
    def regene(self, regene) : self.__regene = regene
    @resist.setter 
    def resist(self, resist) : self.__resist = resist
    @competence.setter
    def competence(self, competence):self.__competence = competence
    @exp.setter
    def exp(self, exp): self.__exp = exp
    @niveau.setter 
    def niveau(self,niveau): self.__niveau = niveau 
    @apres_evolution.setter 
    def apres_evolution(self, apres_evolution): self.__apres_evolution = apres_evolution
    
# =============================================================================
#     #Cette fonction permet de comparer l'objet pokémon
#     def __eq__(self, other):
#         if not isinstance(other,Pokemon): return False
#         if self is other:                 return True
# =============================================================================
        
    # La fonction permet d'afficher le nom de chaque compétence qui sert à la fonction "__str__".
    def nomCompetence(self):
        nomCompetence = "[" 
        nomCompetence+= ", ".join(i.nom for i in self.__competence)
        nomCompetence += "]"
        return nomCompetence
    
    # La fonciton pour afficher les informations de Pokémon
    def __str__(self):
        res = "{0} (LvI {1}, Exp {2}/100, {3}):Vie {4}/{5}, Energis {6}/{7} (+{8}), Resistance {9}, avec competence: {10} "\
                .format(self.__nom, self.__niveau, self.__exp, self.__elem, self.__vie, self.__vie_max, self.__energie, \
                        self.__energie_max, self.__regene, self.__resist, self.nomCompetence())
        return res
    
    def augementerNiveau(self):
        """
        Cette fonction permet d'augementer le niveau du pokémon, de même, il augemente la vie, l'énergie, etc. du Pokémon
        si l'expérience du Pokémon atteint maximal. On vérifie l'expérience atteint 100 et le pokémon peut continuer à 
        augmenter son niveau. Si le niveau atteint niveau max, il faut évoluer!
        """
        if self.__exp >= 100 and self.__niveau <= self.__niveau_max : 
            self.__niveau += 1  # le niveau plus 1
            self.__exp = 0      # l'expérience réinitialiser à zéro
            self.__vie_max += vie_upgrade[self.__numero] # Augmentation de la vie maximale
            self.__vie = self.__vie_max   # Augmentation de la vie 
 
            self.__energie_max += energie_upgrade[self.__numero] # Augmentation de l'énergie maximale 
            self.__energie = self.__energie_max                  # Augmentation de l'énergie
            self.__regene += regene_upgrade[self.__numero]       # Augmentation de la régénération maximale
            self.__resist += resist_upgrade[self.__numero]       # Augmentation de la résistance maximale
            print("{0} est upgrade ! pour l'instant son niveau est {1}".format(self.__nom, self.__niveau))
    
    # La fonction pour set damage
    def setDamage(self, dmg):
        """
        La fonction sert de prendre des dégâts et déduire son propre vie.
        l'entrée "dmg" représente le dégat
        """
        self.__vie -= dmg  # déduire son vie
        # Si la vie est inférieure à 0, la vie est zéro
        if self.__vie < 0: self.__vie = 0 
    
    def sethealing(self, healing):
        """
        La fonction pour restaurer la vie, l'entrée "healing" représente la valeur de régénération de vie
        """
        self.__vie += healing 
        # Si la vie de Pokémon est superieur à la vie maximale, la vie = la vie maximale
        if self.__vie > self.__vie_max:  self.__vie = self.__vie_max 
    
    def setRegenEnergie(self, regene) :
        """
        Même que la fonction précédente, cette fonciton sert à la régénération de l'énergie
        """
        self.__energie += regene 
        if self.__energie > self.__energie_max: self.__energie = self.__energie_max 

    def gangerExperienceJCE(self, pokemonvaincus):
        """
        Selon la formule, calculer l'expérience gagnée, l'entrée "pokemonvaincus" représente le pokémon vaincu.
        De plus, afin de mieux ressentir l'effet de l'augementation de niveau, nous avons 
        légèrement modifié la valeur de la formule. 
        """
        exp_gagner = round((200 + pokemonvaincus.niveau - self.__niveau)/3)
        self.__exp +=  exp_gagner  # mettre à jour l'expérience
        print("{0} a gagné exp: {1}. Son experience actuel est {2}".format(self.__nom, exp_gagner,  self.__exp)) 
    
   
    def gangerExperienceJCJ(self, playervaincus):
        """
        De même, cette fonction sert à gagner l'expérience dans mode Cambat JCJ
        """
        exp_gagner =  round(200 + (playervaincus.deck[0].niveau + playervaincus.deck[1].niveau \
                                + playervaincus.deck[2].niveau)/3 - self.__niveau)
        self.__exp +=  exp_gagner # mettre à jour la nouvelle l'expérience
        print("{0} a gagné exp: {1}. Son experience actuel est {2}".format(self.__nom, exp_gagner,  self.__exp)) 
    # La methode pour les Pokémon utilisent des compétences 
    def utiliserCompet(self, competence, pokemon2):
        """
        Fonciton pour utiliser la conmétence, l'entrée "competence" représente la compétence utilisé, 
        "pokemon2" représente la cible de la compétence d'attaque.
        On détermine d'abord si l'énergie est suffiante pour cette compétence, si non,print "Pas assez d'énergie" 
        et passer son tour. Si oui, on l'utilise en fonciton son type (Attque ou défence). 
        """
        if competence.cout > self.__energie:  # Vérifiez si la compétence peut être utilisée
            print("Pas assez d'énergie ! Veuillez attendre la regénération d'énergie")
        else: 
            self.__energie = self.__energie - competence.cout # L'énergie moins le coût de compétence
            if isinstance(competence, CompetenceAttaque):     # Vérifier si la compétence est une compétence d'attaque
                degat = competence.utilisation(pokemon2.resist, self.__elem, self.__niveau) # Si oui, calculer le dégat
                pokemon2.setDamage(degat)                     # Set le dégat à la cible
                print(" ")                                    # Afficher les informations 
                print("{0} a utilisé {1}".format(self.nom,  competence.nom))
                print("{0} avez fait le dégat de {1} à {2}".format(self.__nom, degat, pokemon2.nom))
                print("Pour l'instant, la vie de {0} est {1}".format(pokemon2.nom,pokemon2.vie ))
            else: # Vérifier si la compétence est une compétence defense
                soin, energie = competence.utilisation()      # Calculer la valeur de la régénération de vie ou/et d'énergie.
                self.setRegenEnergie(energie)                 # Régénérer l'énergie
                self.sethealing(soin)                         # Régénérer la vie
                print("{0} a utilisé {1}".format(self.nom,  competence.nom)) # Afficher les informations 
                print("{0} a fait traitement de {1}, et obtenu energie de {2}".format(self.__nom, soin, energie))
                print("Pour l'instant sa vie est {0}, son énergie est {1}".format(self.__vie, self.__energie))
                
                
#%% La classe de Competence （Abstract）    
class Competence(ABC):
    """
    Cette class est la class arbitraire. Dans cette class, il s'agit principalement d'initialiser
    les variables communes et les méthodes communes.
    Il déclare deux fonctions arbitraire: "utilisation" qui permet d'utiliser la compétence et 
    "__eq__" permet d'identifier un compétence.
    """
    # Initialiser les variables
    def __init__(self, nom, description, element, cout):
        """
        Les principales variables de compétence sont le nom, la description,l'élément de la compétence 
        et le cout de la compétence.
        """
        self.__nom = nom
        self.__description = description
        self.__element = element
        self.__cout = cout
          
    @property    
    def nom(self):         return self.__nom
    @property    
    def cout(self):        return self.__cout
    @property    
    def description(self): return self.__description
    @property    
    def element(self):     return self.__element    
    
    # Fonction d'affichage des informations
    def __str__(self): 
        res  = "{0}: {1} {2}, cout : {3}".format(self.__nom, self.__description,self.__element,  self.__cout)
        return res
    
    @abstractmethod 
    def utilisation (self):pass
    @abstractmethod 
    def __eq__ (self):     pass

#%% La classe de CompetenceAttaque
class CompetenceAttaque(Competence):
    """
    La class "CompetenceAttaque" est une class hérite de la class "Competence". Sauf les variables communs, 
    Ses variables privés sont " puissance" et "precision".
    Dans cette class, on redéfinit la fonction "__str__" et déclare la fonction "utilisation" et "__eq__". 
    """
    def __init__(self, nom, description, element, cout, puissance, precision):
        super().__init__(nom, description, element, cout)
        self.__puissance = puissance
        self.__precision = precision
    
    @property
    def puissance(self): return self.__puissance
    @property
    def precision(self): return self.__precision
     
    def __str__(self):
        res = super().__str__()
        res += ", puissance: {0}, precision : {1}".format(self.__puissance, self.__precision)
        return res
    
    def __eq__(self, other):
        if not isinstance(other,CompetenceAttaque): return False
        if self is other:                           return True
        
    # Utilisation des compétences
    def utilisation(self, resist_assailli, elem_Pokemon, niveau_Pokemon): 
        """
        En fonction du caiher de charge, cette fonction permet de calculer le dégat de la compétence attaque.
        Dans un premièr temps, on détermine la réussite de l’attaque, si Miss, on passe directement ce tour.
        Si l'attaque réussie, on calcule les dégats infligés par cette compétence d'attaque.
        
        les entrées:" resist_assailli" représente la résistance du pokémon assailli.
        "elem_Pokemon" représente l'élément du pokémon assailli, "niveau_Pokemon" représente le niveau du pokémon assaillant.
        Enfin, cette fonction return la valeur de dégat(Si Miss, dégat = 0)
        """
        tirage = random.randint(0, 101)
        if tirage > self.__precision:
            print("!!!!!MISS !!!!!")
            degat =  0          # Si Miss, dégat = 0
        else : 
            if self.element == "Air" :
                if elem_Pokemon == "Air":   b = 1
                elif elem_Pokemon == "Eau": b = 1.5
                elif elem_Pokemon == "Feu": b = 0.5
                else:                       b = 1
            elif self.element == "Eau":
                if elem_Pokemon == "Air":   b = 1
                elif elem_Pokemon == "Eau": b = 1
                elif elem_Pokemon == "Feu": b = 0.5
                else:                       b = 1.5
            elif self.element == "Feu":
                if elem_Pokemon == "Air":   b = 0.5
                elif elem_Pokemon == "Eau": b = 1
                elif elem_Pokemon == "Feu": b = 1
                else:                       b = 1.5
            else:
                if elem_Pokemon == "Air":   b = 1.5
                elif elem_Pokemon == "Eau": b = 0.5
                elif elem_Pokemon == "Feu": b = 1
                else:                       b = 1
            cm = b*random.uniform(0.85,1)
            numerateur = self.__puissance * (4 * niveau_Pokemon + 2)
            degat = round(((numerateur/resist_assailli)+2) * cm)
        return degat
#%% La classe de CompetenceDefence   
class CompetenceDefence(Competence):
    """
    Cette classe est une sous-classe de Compétence, de même, sauf les varibles communs, 
    ses varibles privés sont "soin" et "energie" qui représentent la régénération de la vie et l'énergie
    """
    def __init__(self, nom, description, element, soin, energie, cout): 
        super().__init__(nom, description, element, cout)
        self.__soin = soin
        self.__energie = energie
    
    @property
    def soin(self):    return self.__soin
    @property
    def energie(self): return self.__energie
    
    def __str__(self):
        res = super().__str__()
        res += ", soin: {0}, energie : {1}".format(self.__soin, self.__energie)
        return res
    
    def __eq__(self, other):
        if not isinstance(other,CompetenceDefence): return False
        if self is other:                           return True
   
    # Utiliser les compétences
    def utilisation(self):
        """
        Lors de l’utilisation d’une compétence défense par un Pokemon, on génère un nombre aléatoire compris entre 
        les 2 valeurs données pour déterminer la quantité de vie ou d’énergie restaurée par la compétence.
        """
        soin = random.randint(self.__soin[0], (self.__soin[1]))
        energie = random.randint(self.__energie[0], (self.__energie[1]))
        return soin, energie

